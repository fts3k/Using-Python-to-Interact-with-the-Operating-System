# It's a good idea to have a count of how many times each username appears in our log.
# Use a dictionary

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) +1
print(usernames)


