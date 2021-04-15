#The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

import re

def long_words(text):
    result = re.findall(r"[\w*]{7,}", text)
    return result

print(long_words("I like to drink coffee in the morning"))
print(long_words("That sounds like a wonderful plan"))

