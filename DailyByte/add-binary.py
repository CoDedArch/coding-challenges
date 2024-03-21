"""
    This Question is asked by apple.
    Given two binary strings(strings
    containing only 1s and 0s) return 
    their sum (also as a binary string)
    Note: neither binary string will contain
    leading 0s unless the string itself
"""
def is_binary(s:str):
    """Check if a string is a binary string."""
    return s.isnumeric() and set(s) <= {'0', '1'}

def remove_zeros(s:str):
    """remove leading 0 unless string itself"""
    return s.lstrip('0') or '0'

def add_binary(str_a:str, str_b:str):
    """Add two binary strings and return the result as a binary string."""
    str_a = remove_zeros(str_a)
    str_b = remove_zeros(str_b)

    if is_binary(str_a) and is_binary(str_b):
        result = ''
        carry = 0
        for i in range(len(str_a)):
            sum = int(str_a[-i]) + int(str_b)
            if sum in (0,1):
                if len(str_a) > 1:
                    sum = str_a[:-i] + str(sum)
                return str(sum)
            else:
                carry +=1
                result += '0'
                if carry == len(str_a):
                    sum = '1' + result
                    return sum
        print(result)
    return 'string passed is not a valid binary string'

print(add_binary('111', '1'))