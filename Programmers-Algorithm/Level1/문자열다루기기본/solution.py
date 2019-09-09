def alpha_string46(s):
    if s.isdigit() and len(s) == 4 or len(s) == 6:
        return True
    else:
        return False


print( alpha_string46("a234") )
print( alpha_string46("1234") )
