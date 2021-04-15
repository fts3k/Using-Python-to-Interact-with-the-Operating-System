import re

def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result != None

print(check_punctuation("This is a sentence."))
print(check_punctuation("This ends without a period"))
print(check_punctuation("Aren't regex awesome?"))
print(check_punctuation("End of the line!"))