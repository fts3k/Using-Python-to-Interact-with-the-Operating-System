
log = "July 31 07 07:51:48 mycomputer bad_process[12345]: ERROR perfoming package upgrade"
index = log.index("[")
print(log[index+1:index+6])

# Problems with using index.
# We don't know how long the ID string will be if it changes - this might break the code.
# Instead we can use Regex to extract in a more robust method.


