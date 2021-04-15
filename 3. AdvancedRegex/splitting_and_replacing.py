# split and replace functions.

import re

result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)

# To include elements we're using to split the values - use capturing parenthesis

result2 = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result2)


# sub - used to create new strings by subsituting all or part of them for different string.

# Anonymize email address.

redacted = re.sub(r"[\w.%+-]+@[\w.-]+", "REDACTED", "Received an email for go_nuts95@gmail.com")
print(redacted)

# Regex for replacing.

replace = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(replace)
