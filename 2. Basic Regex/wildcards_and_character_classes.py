# . - wildcard; matches any character
# To restrict a range of wildcard, we use character classes [xxx]

import re

print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way","Highway"))

print(re.search(r"[a-z]way", "What a way to go")) # No match because string way is preceeded by space.

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Sometimes we may want to match characters that aren't in a group.

print(re.search(r"[^a-zA-Z]", "This is a sentence"))  # Matches any character that isn't a letter.
print(re.search(r"[^a-zA-Z ]", "This is a sentence."))

# To list alternative options that can get matches, use | symbol.

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats and dogs.")) # Have 2 possible matches but only gets the 1st one

# findall - used to get all possible matches.

print(re.findall(r"cat|dog", "I like cats and dogs"))