# What if we wanted a pattern that repeats specific number of times.
# Occurs if processing a line we know has some specific data in a column
# Or a string of a specific length.
# numeric repetition qualifiers.

# Match string of exactly 5 letters.
import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost")) # We only get the first one
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # matches 5 characters from appeared

# to match all the words that are exactly 5 letters long.

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

# Can have 2 numbers in a range.
# To match a range of 5 to 10 letters.

print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really strawberries"))





