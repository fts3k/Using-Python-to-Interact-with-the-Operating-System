import re
def extract_pid(log_line):
    x = re.search(r"\[(\d+)\]: ([A-Z]*)", log_line)
    if x is None:
        return None
    return "{} ({})".format(x[1], x[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)