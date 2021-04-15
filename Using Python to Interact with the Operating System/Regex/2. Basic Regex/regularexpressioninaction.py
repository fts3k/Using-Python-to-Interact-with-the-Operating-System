# Check if country name start and ends in A/a
import re

print(re.search(r"A.*a","Argentina" ))
print(re.search(r"A.*a","Azerbaijan" ))  # matches Azerbaija because we didn't specify we wanted our pattern to match the whole string.


# Need to make the patterns stricter by adding the beginning & end of a line.

print(re.search(r"A.*a$","Azerbaijan" )) 
print(re.search(r"A.*a$","Argentina" ))

# Regex that validates a string contains valid variable name.

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "this_is_a_valid_one"))
print(re.search(pattern, "this is not a valid one"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "9my_variable1"))



