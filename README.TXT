Module display the number of words in files with the specified file extension.
With arbitrary nesting structure of directories.
Using arguments which are passed through command-line interface.


counter_words module project: Python (os, argparse)
    • has a console interface (arguments - file extensions, file path).
    • count the number of words in the files with the specified extension
    • in any folder tree with unlimited nesting
    • In each folder may be nested folders and / or files with a different extension
    • display the result to the console in the form of a report (how many files with this extension,
    it was found listed files, the total number of words in these files).
    
    counter.py - the main module.
    basefiletools.py - BaseTools class that contains tools for work with files.
    cliinterface.py - a console interface.
