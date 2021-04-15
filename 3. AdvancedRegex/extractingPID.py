import re

log = "July 31 07 07:51:48 mycomputer bad_process[12345]: ERROR perfoming package upgrade"
regex = r"\[(\d+)\]"

result = re.search(regex, log)  # re.search - 
print(result)

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")  # Results in an error
print(result)  # problem solved in extract PID exercise 9



