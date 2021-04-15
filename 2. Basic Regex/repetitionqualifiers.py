# Repetition Qualifiers - used to match characters more than once.
# Use cases:
# Find the longest word in a string.
# Find hostnames in a log file by checking a bunch of alphanumeric characters between brackets.

import re

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Pygmalion"))  # Python programming - matches as many characters as possible - greedy.

# Use character class if you want the pattern to match letters.

print(re.search(r"Py[a-z]*n", "Python programming"))
print(re.search(r"Py[a-z]*n", "Pyn")) # Zero times is also a possibility.


# Using egrep
# + matches one or more characters that come before them.
#  

print(re.search(r"o+l", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "oil"))

# ? means zero or one occurence of the character before it.

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each","I like the peaches"))



