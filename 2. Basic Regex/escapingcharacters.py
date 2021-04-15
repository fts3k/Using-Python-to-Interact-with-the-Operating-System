# Escaping characters are used to match special characters.

import re

print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# Note \n is used to indicate a new line.
# \t does the same for tabs.
# \w matches any alphanumeric character including letters, numbers and underscores

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# \d for matching digits.
# \s for matching whitespace such as tabs and newline.
# \b for new boundary


