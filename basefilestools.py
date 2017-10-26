# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


class BaseTools(object):
    """BaseTools class that contains tools for work with files"""
    def __init__(self, path=None, ext=''):
        self.path = BaseTools.check_path(path)
        self.extension = ext

    @staticmethod
    def check_path(path):
        """Check directory or file path"""
        if os.path.isdir(path):
            return path
        else:
            raise FileNotFoundError('Directory does not exist!')

    def change_dir(self):
        """Change current directory according to path"""
        os.chdir(self.path)

    def get_tree_el(self):
        """Traverses a directory tree

        Return: a tuple with lists files, full_paths.
        """
        dirs = []
        files = []
        full_paths = []

        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if filename.endswith(self.extension):
                    files.append(filename)
                    full_paths.append(os.path.join(dirpath, filename))

        return files, full_paths

    def count_files_by_ext(self):
        """Counts the files with the specified file extension.

        Return: a tuple with lists number of files specified by extension,
        and the list of paths to that files.
        """
        files, paths = self.get_tree_el()
        number_of_files = len(files)

        return number_of_files, paths, files

    @staticmethod
    def count_words_in_file(paths):
        """Counts the number of words in files with the specified
        file extension.

        Return: a total number of words in all files with the specified
        file extension by user in the cli.
        """
        total = 0
        words = []

        for path in paths:
            with open(path, 'r') as file:
                for line in file:
                    line = line.strip()
                    # A list of words in the string if the string is not empty.
                    words = [word for word in line.split(' ') if word]
                    total += len(words)
        return total

    def display_total_words(self):
        """Display a total number of words for user.

        Display message with total number of words in files and
        a list of all files with this extension.
        """
        number_of_files, paths, files = self.count_files_by_ext()

        # Total number of words in all files specified by extension
        total = BaseTools.count_words_in_file(paths)

        print('We found these files:')

        # Display a list of all files with this extension.
        for file in files:
            print('-'*5, file)

        print('Total:')

        msg = 'In {0} {1} files are {2} words.\n'.format(number_of_files,
                                                         self.extension,
                                                         total)

        print(msg)
