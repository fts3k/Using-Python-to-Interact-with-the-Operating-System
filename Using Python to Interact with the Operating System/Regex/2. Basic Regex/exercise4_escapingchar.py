import re

def check_character_groups(text):
    result = re.search(r"\w+\s+\w", text)
    return result != None

print(check_character_groups("One"))
print(check_character_groups("123 Ready Set Go"))
print(check_character_groups("username user_01"))
print(check_character_groups("shopping_list: milk, bread, eggs"))

# www.regex101.com

