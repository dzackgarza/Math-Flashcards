import os

def extract_apkg_filenames():
    # Get the current working directory
    directory = os.getcwd()

    # Walk the directory and get a list of all files with the ".apkg" extension
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.apkg'):
                # Extract the base name of the file and print it
                base_name = os.path.splitext(file)[0]
                print(base_name)

# Extract the base names of all ".apkg" files in the current directory
extract_apkg_filenames()
