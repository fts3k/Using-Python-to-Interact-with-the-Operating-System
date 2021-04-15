# We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?
import re

def split_word(text):
    result= re.split(r"a|the", text)
    return result

print(split_word("One sentence. Another one? And the last one!"))

