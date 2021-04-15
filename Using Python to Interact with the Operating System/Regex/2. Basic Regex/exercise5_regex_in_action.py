import re
def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]*[\.\?!]$", text)
    return result != None

print(check_sentence("Is this a sentence?"))
print(check_sentence("is this a sentence?"))
print(check_sentence("Hello"))    