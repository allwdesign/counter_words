"""Module display the total number of words in files using
command-line interface.

Display the number of words in files with the specified file extension.
Arbitrary nesting structure of directories.

Using arguments which are passed through command-line interface.
"""
import cliinterface
from basefilestools import BaseTools


def main():
    # Path that specified by user in the cli
    path = cliinterface.args.path

    # Extension for files that you want to count the total number of words
    # specified by user in the cli.
    extension = cliinterface.args.file_extension

    try:
        # Create base tool for work with files
        tools_for_files = BaseTools(path, extension)

        # Display message with total number of words in files specified by
        # extension. And a list of all files with this extension.
        tools_for_files.display_total_words()

    except FileNotFoundError as err:
        print(err)

if __name__ == "__main__":
    main()
