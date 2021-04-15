# What if you needed to run a system program from a python script.

# e.g send ICMP packets to a host to check if it's responding.

import subprocess

subprocess.run(["date"])

# Parent can't do anything until the child process finishes.

# After the child finishes running, it exits & the control returns to the parent.

subprocess.run(["sleep", "2"])  # waits for 2 secs # intepreter is blocked until after the 2 seconds.

# 

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)



