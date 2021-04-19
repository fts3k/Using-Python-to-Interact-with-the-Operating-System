# Sometimes checking for all the errors becomes a challenge
import os

#def read_file(filename):
#    if not os.path.exists(filename):
#        return ""
#   if not os.path.isfile(filename):
#        return ""
#   if not os.access(filename, os.R_OK):
#        return ""
#   if is_locked(filename):
#       return ""
#    if is_not_accessible(filename):
#        return ""



   # We could check for all these conditions but what if there's another thing to cause the open function to raise an error???

   # Solution is to use try except construct   