#!/usr/bin/env python3

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")   # keyword to raise an error is raise. 
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False 
    return True
