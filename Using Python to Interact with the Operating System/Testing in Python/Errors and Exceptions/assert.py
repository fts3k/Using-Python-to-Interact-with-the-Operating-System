# Assert Keyword - verifies that a conditional expression is true.
# If false - it raises an AssertionError


def validate_user(username, minlen):
    assert type(username) == str,"username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")   # keyword to raise an error is raise. 
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False 
    return True

    # Assertions will get removed from our code if we ask the interpreter to optimize it to run faster.
    # Hence we should use raise to check for exceptions that we except to run during normal running of the code.
    # 