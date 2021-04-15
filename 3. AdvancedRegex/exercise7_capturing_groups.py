import re

def rearrange_names(names):
    result = re.search(r"^(\w*), (\w*(\s\w*\.)?)$", names)
    if result is None:
        return names
    return "{} {}".format(result[2], result[1])

names = rearrange_names("Kevin, Ojijo K.")
print(names) 


# Another solution

def reverse_names(contacts):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", contacts)
    if result is None:
        return contacts
    return "{} {}".format(result[2], result[1])

contacts = reverse_names("John, Kennedy J")
print(contacts) 
