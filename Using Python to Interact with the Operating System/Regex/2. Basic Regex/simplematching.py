import re

result = re.search(r"aza", "plaza") # r - raw strings.
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "jobs")
print(result)


print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","clapping"))



# Case insensitive match, pass re.IGNORECASE option

print(re.search(r"p.ng", "Penguin", re.IGNORECASE))

