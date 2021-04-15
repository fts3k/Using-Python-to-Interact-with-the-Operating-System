# If we want python to manipulate the output of system command, need to tell the run function to capture it.

# e.g stats on users logged into a server in a day. - use the "who" command.
import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

print(result.returncode)



