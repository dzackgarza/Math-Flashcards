# Instructions

- You'll need a working installation of [Python 3](https://realpython.com/installing-python/)
- (Optional) Install [ankdown](https://github.com/benwr/ankdown). If you have pip, you can just run something like `pip3 install --user ankdown`.
  - Alternative: I've included my own modified copy of `ankdown.py` that can just be run directly by either
    - Running `chmod +x ankdown.py` and subsequently `ankdown.py ...`
    - Running `python3 ./ankdown.py ...`
- As a test, you can try running  `ankdown ./ankdown.py -r ./Decks -p ./mathnotes.apkg`
  - The '-r' option points it at a directory, which is recursively searches for '.md' files to parse as cards
  - The '-p' option tells it to output a '.apkg' file, which can be imported to Anki
- This should generate 'mathnotes.apkg'

![](figures/image_2020-05-15-22-58-48.png)

![](figures/image_2020-05-15-22-59-55.png)

![](figures/image_2020-05-15-23-00-17.png)
