# Capturing Groups - Portions of the pattern that are encolsed in parenthesis.

import re

result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada" )
print(result)
print(result.groups())
print(result[1])
print(result[2])

"{} {}".format(result[2], result[1])





