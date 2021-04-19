# In some cases, we may want to raise an error ourselves.
# This usually happens when some of the conditions necessary for a function to do its job properly aren't met & returning None or some other base value isn't good enough.

# Let's say we have a function that verifies whether a chosen username is valid.
# One of the checks this function does is to verify that the provided name is atleast a certain amount of characters with the minimum value received by a parameter.

#def validate_user(username, minlen):
 #   if len(username) < minlen:
#        return False
 #   if not username.isalnum():
 #       return False 
  #  return True


# The above code works as long as the provided values are sensible.
#  What would happen if the minlen variable is zero or negative number? Our function will allow an empty username as valid.  Which doesn't make much sense.
# 
# To prevent this, we can add an extra check to our function to verify the received parameters are sane.
#            

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")   # keyword to raise an error is raise. 
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False 
    return True

 # What if instead of string, we supply a number? Our interpreter raises an error since we are passing an int that doesn't have a len function.
 #  Try passing a list;
 #  First, an empty list -    return false; 
 # List with 1 variable - AttributeError coz we are trying to use isalnum method which is not supported on lists.

 # In situations where we want to check that our code behaves the way it should, we use an alternative to the raise function  - particulary when we wanna avoid situations that should never happen. - assert

