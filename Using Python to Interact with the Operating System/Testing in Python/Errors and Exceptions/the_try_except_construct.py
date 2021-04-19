

def character_frequency(filename):
    """ Counts the frequency of each character in the given file. """
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters


    # When writing try except block - The code in the except block is only executed if one of the instructions in the try block raises an error of the matching type.
    # To use try except block, we need to be aware of the errors that functions that we are calling might raise.
    # How to raise own errors? Check raising errors.py
    #                 