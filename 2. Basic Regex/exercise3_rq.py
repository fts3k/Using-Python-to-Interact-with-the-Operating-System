import re

def repeating_letter_a(text):
    result = re.search(r"[Aa].*[Aa]", text)
    return result != None

print(repeating_letter_a("banana"))
print(repeating_letter_a("pineapple"))
print(repeating_letter_a("Animal kingdom"))
print(repeating_letter_a("A is for apple"))

