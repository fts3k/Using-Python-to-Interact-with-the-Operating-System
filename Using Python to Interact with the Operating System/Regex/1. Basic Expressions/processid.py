import re

log = "July 31 07 07:51:48 mycomputer bad_process[12345]: ERROR perfoming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)  # re.search - 
print(result)


