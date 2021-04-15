import re

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid("99 elephants in a [cage]"))
print(extract_pid("July 31 07 07:51:48 mycomputer bad_process[12345]: ERROR perfoming package upgrade"))



# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
