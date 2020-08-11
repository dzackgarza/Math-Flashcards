#!/usr/bin/env python3
"""Ankdown: Convert Markdown files into anki decks.

This is a hacky script that I wrote because I wanted to use
aesthetically pleasing editing tools to make anki cards, instead of
the (somewhat annoying, imo) card editor in the anki desktop app.

The math support is via MathJax, which is more full-featured (and
much prettier) than Anki's builtin LaTeX support.

The markdown inputs should look like this:

```
First Card Front ![alt_text](local_image.png)

%

First Card Back: \\(\\text{TeX inline math}\\)

%

first, card, tags

---

Second Card Front:

\\[\\text{TeX Math environment}\\]

%

Second Card Back (note that tags are optional)
```

Ankdown can be configured via yaml. A possible configuration file might look like this:

```yaml
recur_dir: ~/ankdown_cards
pkg_arg: ~/ankdown_cards.apkg
card_model_name: CustomModelName
card_model_css: ".card {font-family: 'Crimson Pro', 'Crimson Text', 'Cardo', 'Times', 'serif'; text-align: left; color: black; background-color: white;}"
dollar: True
```

A configuration can also be passed as a string: `"{dollar: True, card_model_name: CustomModelName, card_model_css: \".card {text-align: left;}\"}"`

Usage:
    ankdown.py [-r DIR] [-p PACKAGENAME] [--highlight] [--config CONFIG_STRING] [--configFile CONFIG_FILE_PATH]

Options:
    -h --help     Show this help message
    --version     Show version

    -r DIR        Recursively visit DIR, accumulating cards from `.md` files.

    -p PACKAGE    Instead of a .txt file, produce a .apkg file. recommended.

    --highlight   Enable syntax highlighting for code

    --config CONFIG_STRING   ankdown configuration as YAML string

    --configFile CONFIG_FILE_PATH path to ankdown configuration as YAML file
"""


import hashlib
import os
import re
import tempfile
import textwrap

from shutil import copyfile

import misaka
import genanki
import yaml

from docopt import docopt

import houdini as h
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name


class HighlighterRenderer(misaka.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(
            h.escape_html(text.strip()))


renderer = HighlighterRenderer()
highlight_markdown = misaka.Markdown(renderer, extensions=("fenced-code", "math"))


VERSION = "0.7.1"

# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
CARD_MATHJAX_CONTENT = textwrap.dedent(r"""
<script>
MathJax.Hub.Config({
TeX: {
    Macros: {
        NN: ['{\\mathbb {N}}'],
        RR: ['{\\mathbb{R}}', 0],
        DD: ['{\\mathbb{D}}', 0],
        ZZ: ['{\\mathbb{Z}}', 0],
        CC: ['{\\mathbb{C}}', 0],
        QQ: ['{\\mathbb{Q}}', 0],
        CC: ['{\\mathbb{C}}', 0],
        RP: ['{\\mathbb{RP}}', 0],
        CP: ['{\\mathbb{CP}}', 0],
        HP: ['{\\mathbb{HP}}', 0],
        OP: ['{\\mathbb{OP}}', 0],
        FF: ['{\\mathbb{F}}', 0],
        GF: ['{\\mathbb{GF}}', 0],
        PP: ['{\\mathbb{P}}', 0],
        Af: ['{\\mathbb{A}}', 0],
        MM: ['{\\mathbb{M}}', 0],
        TT: ['{\\mathbb{T}}', 0],
        Sp: ['{\\mathbb{S}}', 0],
        KK: ['{\\mathbb{K}}', 0],
        Gr: ['{\\text{Gr}}', 0],
        GL: ['{\\text{GL}}', 0],
        liegl: ['{\\mathfrak{gl}}', 0],
        lieg: ['{\\mathfrak{g}}', 0],
        lieb: ['{\\mathfrak{b}}', 0],
        lieh: ['{\\mathfrak{h}}', 0],
        lien: ['{\\mathfrak{n}}', 0],
        ind: ['{\\mathrm{Ind}}', 0],
        SL: ['{\\text{SL}}', 0],
        liesl: ['{\\mathfrak{sl}}', 0],
        SP: ['{\\text{SP}}', 0],
        liesp: ['{\\mathfrak{sp}}', 0],
        SO: ['{\\text{SO}}', 0],
        lieso: ['{\\mathfrak{so}}', 0],
        OO: ['{\\mathcal{O}}', 0],
        mm: ['{\\mathfrak{m}}', 0],
        pr: ['{\\mathfrak{p}}', 0],
        dual: ['^\\vee', 0, ''],
        Tr: ['\\mathrm{Tr}', 0],
        spanof: ['\\mathrm{span}', 0],
        divides: ['{~\\Bigm| ~}', 0],
        notdivides: ['{~\\not\\Bigm| ~}', 0],
        sym: ['\\mathrm{Sym}', 0],
        aut: ['\\mathrm{Aut}', 0],
        grad: ['\\mathrm{grad}', 0],
        sign: ['\\mathrm{sign}', 0],
        spec: ['{\\mathrm{Spec}}', 0],
        Gal: ['{\\mathrm{Gal}}', 0],
        suchthat: ['{~\\mathrel{\\Big|}~}', 0],
        uniformlyconverges: ['\\rightrightarrows', 0],
        mapsvia: ['\\xrightarrow{#1}', 1],
        converges: ['\\overset{#1}', 1],
        generators: ['\\left\\langle{#1}\\right\\rangle', 1],
        theset: ['\\left\\\{ #1 \\right\\\}', 1],
        too: ['{\\xrightarrow{#1}}', 1, ''],
        norm: ['{\\lVert #1 \\rVert}', 1],
        restrictionof: ['{\\left.{#1}\\right|_{#2}}', 2],
        inner: ['{\\left\\langle {#1},~{#2} \\right\\rangle}', 2],
        correspond: ['{\\theset{\\substack{#1}}}', 1],
        realpart: ['{\\mathcal{Re}({#1})}', 1],
        dd: ['{\\frac{\\partial #1}{\\partial #2}}', 2],
        stirling: ['\\genfrac\\{\\}{0pt}{}{#1}{#2}', 2],
        thevector: ['{\\left\[ {#1} \\right\]}', 1],
        gens: ['{\\left\< {#1} \\right\>}', 1],
        qty: ['{\\left( {#1} \\right)}', 1],
        intersect: ['\\bigcap', 0],
        union: ['\\bigcup', 0],
        coker: ['\\mathrm{coker}', 0],
        rank: ['\\mathrm{rank}', 0],
        tensor: ['\\otimes', 0],
        semidirect: ['\\rtimes', 0],
        pt: ['\\{\\text{pt}\\}', 0],
        bd: ['{\\del}', 0],
        wait: ['{\\,\\cdot\\,}', 0],
        selfmap: ['{\\circlearrowleft}', 0],
        Tor: ['\\text{Tor}', 0],
        tor: ['\\text{Tor}', 0],
        ext: ['\\text{Ext}', 0],
        actson: ['\\curvearrowright', 0],
        actsonl: ['\\curvearrowleft', 0],
        disjoint: ['{\\coprod}', 0],
        dash: ['{\\hbox{-}}', 0],
        bigast: ['{\\mathop{\\Large \\ast}}', 0],
        from: ['\\leftarrow', 0],
        covers: ['\\twoheadrightarrow', 0],
        Zp: ['\\mathbb{Z}_{(p)}', 0],
        Qp: ['\\mathbb{Q}_{(p)}', 0],
        ZpZ: ['\\mathbb{Z}/p\\mathbb{Z}', 0],
        ZnZ: ['\\mathbb{Z}/n\\mathbb{Z}', 0],
        Sm: ['{\\text{Sm}_k}', 0],
        GG: ['{\\mathbb{G}}', 0],
        bung: ['\\text{Bun}_G', 0],
        Aut: ['{\\text{Aut}}', 0],
        del: ['{\\partial}', 0],
        im: ['{\\text{im}~}', 0],
        homotopic: ['\\simeq', 0],
        into: ['\\to', 0],
        cross: ['\\times', 0],
        definedas: ['\\mathrel{\\vcenter{:}}=', 0],
        surjects: ['\\twoheadrightarrow', 0],
        onto: ['\\twoheadrightarrow', 0],
        injects: ['\\hookrightarrow', 0],
        id: ['\\text{id}', 0],
        inv: ['^{-1}', 0],
        normal: ['{~\\trianglelefteq~}', 0],
        units: ['^{\\times}', 0],
        arcsec: ['\\mathrm{arcsec}', 0],
        multinomial: ['\\left(\\!\\!{#1}\\!\\!\\right)', 1],
        stirlingfirst: ['\\genfrac{[}{]}{0pt}{}{#1}{#2}', 2],
        floor: ['{\\left\\lfloor #1 \\right\\rfloor}', 1],
        ad: ['\\mathrm{ad}', 0],
        ch: ['\\mathrm{char}~', 0],
        // Conflicts
        abs: ['{\\left\\lvert #2 \\right\\rvert_{\\text{#1}}}', 2, ''],
        vector: ['{\\mathbf{ {#1} }}', 1],
        hom: ['\\text{Hom}', 0],
        char: ['\\text{char}', 0]
    },
    extensions: [
        "noUndefined.js", "autoload-all.js",
        "AMSmath.js", "AMSsymbols.js", "color.js"
    ],

},
CommonHTML: { linebreaks: { automatic: true } },
"HTML-CSS": { linebreaks: { automatic: true } },
SVG:        { linebreaks: { automatic: true } },
tex2jax: {
    inlineMath: [ ['$','$'], ['\\(','\\)'] ],
    displayMath: [ ['$$','$$'], ['\\[','\\]'] ],
    processEscapes:true
},
CommonHTML: {
    scale: (!!navigator.userAgent.match(/(mac)|(mobile)/i) ? 150 : 100)
}
});
MathJax.Hub.Configured();
</script>
<script type="text/javascript">
    (function () {
        if (typeof MathJax === "undefined") {
            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML';
            document.body.appendChild(script);
        }
    })();
</script>
""")

CONFIG = {
    'pkg_arg': 'AnkdownPkg.apkg',
    'recur_dir': '.',
    'dollar': False,
    'highlight': False,
    'card_model_name': 'Custom Ankdown Model',
    'card_model_css': """
        .card {
            font-family: 'Crimson Pro', 'Crimson Text', 'Cardo', 'Times', 'serif';
            text-align: left;
            color: black;
            background-color: white;
            font-size: 18pt;
        }
        """,
    'card_model_fields': [
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Tags"},
    ],
    'card_model_templates': [
        {
            "name": "Ankdown Card",
            "qfmt": "{{{{Question}}}}\n{0}".format(CARD_MATHJAX_CONTENT),
            "afmt": "{{{{Question}}}}<hr id='answer'>{{{{Answer}}}}\n{0}".format(CARD_MATHJAX_CONTENT),
        }
    ]
}


def simple_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    h = hashlib.md5()
    h.update(text.encode("utf-8"))
    return int(h.hexdigest(), 16) % (1 << 63)


class Card(object):
    """A single anki card."""

    def __init__(self, filename, file_index):
        self.fields = []
        self.filename = filename
        self.file_index = file_index
        self.model = genanki.Model(
            simple_hash(CONFIG['card_model_name']),
            CONFIG['card_model_name'],
            fields=CONFIG['card_model_fields'],
            templates=CONFIG['card_model_templates'],
            css=CONFIG['card_model_css']
        )

    def deckdir(self):
        return os.path.dirname(self.filename)

    def deckname(self):
        return os.path.basename(self.deckdir())

    def basename(self):
        return os.path.basename(self.filename)

    def card_id(self):
        return "{}/{}{}".format(self.deckname(), self.basename(), self.file_index)

    def add_field(self, field):
        self.fields.append(field)

    def has_data(self):
        return len(self.fields) > 0 and any([s.strip() for s in self.fields])

    def has_front_and_back(self):
        return len(self.fields) >= 2

    def finalize(self):
        """Ensure proper shape, for extraction into result formats."""
        if len(self.fields) > 3:
            self.fields = self.fields[:3]
        else:
            while len(self.fields) < 3:
                self.fields.append('')

    def guid(self):
        return simple_hash(self.card_id())

    def to_genanki_note(self):
        """Produce a genanki.Note with the specified guid."""
        return genanki.Note(model=self.model, fields=self.fields, guid=self.guid())

    def make_ref_pair(self, filename):
        """Take a filename relative to the card, and make it absolute."""
        newname = '%'.join(filename.split(os.sep))

        if os.path.isabs(filename):
            abspath = filename
        else:
            abspath = os.path.normpath(os.path.join(self.deckdir(), filename))
        return (abspath, newname)

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.fields):
            current_stage = field
            for regex in [r'src="([^"]*?)"']: # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m):
                    initial_contents = m.group(1)
                    abspath, newpath = self.make_ref_pair(initial_contents)
                    results.append((abspath, newpath))
                    return r'src="' + newpath + '"'

                current_stage = re.sub(regex, process_match, current_stage)

                for r in results:
                    yield r

            # Anki seems to hate alt tags :(
            self.fields[i] = re.sub(r'alt="[^"]*?"', '', current_stage)


class DeckCollection(dict):
    """Defaultdict for decks, but with stored name."""
    def __getitem__(self, deckname):
        if deckname not in self:
            deck_id = simple_hash(deckname)
            self[deckname] = genanki.Deck(deck_id, deckname)
        return super(DeckCollection, self).__getitem__(deckname)


def field_to_html(field):
    """Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets."""
    if CONFIG['dollar']:
        for (sep, (op, cl)) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
            escaped_sep = sep.replace(r"$", r"\$")
            # ignore escaped dollar signs when splitting the field
            field = re.split(r"(?<!\\){}".format(escaped_sep), field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
        for bracket in ["(", ")", "[", "]"]:
            field = field.replace(r"\{}".format(bracket), r"\\{}".format(bracket))
            # backslashes, man.

    if CONFIG['highlight']:
        return highlight_markdown(field)


    return misaka.html(field, extensions=("fenced-code", "math"))


def compile_field(field_lines, is_markdown):
    """Turn field lines into an HTML field suitable for Anki."""
    fieldtext = ''.join(field_lines)
    if is_markdown:
        return field_to_html(fieldtext)
    else:
        return fieldtext


def produce_cards(filename):
    """Given the markdown in infile, produce the intended result cards."""
    with open(filename, "r") as f:
        current_field_lines = []
        i = 0
        current_card = Card(filename, file_index=i)
        for line in f:
            stripped = line.strip()
            if stripped in {"---", "%"}:
                is_markdown = not current_card.has_front_and_back()
                field = compile_field(current_field_lines, is_markdown=is_markdown)
                current_card.add_field(field)
                current_field_lines = []
                if stripped == "---":
                    yield current_card
                    i += 1
                    current_card = Card(filename, file_index=i)
            else:
                current_field_lines.append(line)

        if current_field_lines:
            is_markdown = not current_card.has_front_and_back()
            field = compile_field(current_field_lines, is_markdown=is_markdown)
            current_card.add_field(field)
        if current_card.has_data():
            yield current_card


def cards_from_dir(dirname):
    """Walk a directory and produce the cards found there, one by one."""
    for parent_dir, _, files in os.walk(dirname):
        for fn in files:
            if fn.endswith(".md") or fn.endswith(".markdown"):
                for card in produce_cards(os.path.join(parent_dir, fn)):
                    yield card


def cards_to_apkg(cards, output_name):
    """Take an iterable of the cards, and put a .apkg in a file called output_name.

    NOTE: We _must_ be in a temp directory.
    """
    decks = DeckCollection()

    media = set()
    for card in cards:
        card.finalize()
        # for abspath, newpath in card.determine_media_references():
            # copyfile(abspath, newpath) # This is inefficient but definitely works on all platforms.
            # media.add(newpath)
        decks[card.deckname()].add_note(card.to_genanki_note())

    package = genanki.Package(deck_or_decks=decks.values(), media_files=list(media))
    package.write_to_file(output_name)


def apply_arguments(arguments):
    global CONFIG
    if arguments.get('--configFile') is not None:
        config_file_path = os.path.abspath(os.path.expanduser(arguments.get('--configFile')))
        with open(config_file_path, 'r') as config_file:
            CONFIG.update(yaml.load(config_file))
    if arguments.get('--config') is not None:
        CONFIG.update(yaml.load(arguments.get('--config')))
    if arguments.get('-p') is not None:
        CONFIG['pkg_arg'] = arguments.get('-p')
    if arguments.get('-r') is not None:
        CONFIG['recur_dir'] = arguments.get('-r')
    if arguments.get('--highlight'):
        CONFIG['highlight'] = True
        css_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'highlight.css')
        with open(css_file_path) as css_file:
            CONFIG['card_model_css'] += css_file.read().replace('\n', '')



def main():
    """Run the thing."""
    apply_arguments(docopt(__doc__, version=VERSION))
    # print(yaml.dump(CONFIG))
    initial_dir = os.getcwd()
    recur_dir = os.path.abspath(os.path.expanduser(CONFIG['recur_dir']))
    pkg_arg = os.path.abspath(os.path.expanduser(CONFIG['pkg_arg']))

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname) # genanki is very opinionated about where we are.

        card_iterator = cards_from_dir(recur_dir)
        cards_to_apkg(card_iterator, pkg_arg)

        os.chdir(initial_dir)

    os.system('notify-send "Ankdown" "New cards generated." --urgency=critical --expire-time=5000')


if __name__ == "__main__":
    exit(main())
