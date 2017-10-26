import argparse

parser = argparse.ArgumentParser(description="Counts the number of words in "
                                 "files with the specified file extension. "
                                 "Arbitrary nesting structure of directories.")


parser.add_argument("path",
                    type=str,
                    help="The root directory path for search files. "
                         "Must be a string.")

parser.add_argument("file_extension",
                    type=str,
                    help="Extension for files that you want "
                         "to count the total number of words. "
                         "Must be a string.")
args = parser.parse_args()
