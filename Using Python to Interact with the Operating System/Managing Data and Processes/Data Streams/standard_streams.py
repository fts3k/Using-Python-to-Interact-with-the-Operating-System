# I/O streams - the basic mechanism for perfoming input & output operations in your programs.

# STDNIN - pathway between the screen and the user
# STDOUT - pathway btn program & target output.
# STDERR - specifically as a channel to show error messages.


data = input("This will come from STDIN")
print("Now we write it too STDOUT: "+ data)
print("Now we generate an error to STDERR: "+ data + 1)

