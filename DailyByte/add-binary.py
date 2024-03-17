"""
    This Question is asked by apple.
    Given two binary strings(strings
    containing only 1s and 0s) return 
    their sum (also as a binary string)
    Note: neither binary string will contain
    leading 0s unless the string itself
"""
def check_chars_are_1_and_0(string_to_check:str):
    """Checks if string are only binary

    Args:
        string_to_check (str): 

    Returns:
        bool: True chars are bits else False
    """
    all_chars_binary = True
    for char in string_to_check:
        if not char in ('1', '0'):
            all_chars_binary = False
            break
    return all_chars_binary

def check_is_binary(string_to_check:str):
    """Accepts a string, run test conditions to see if it satisfies
    as a binary string

    Args:
        string_to_check (str): String to run test conditions against

    Returns:
        bool: True if all conditions are satisfied, else False any fails
    """
    test_conditions = [
        string_to_check.isnumeric(),
        check_chars_are_1_and_0(string_to_check)
    ]
    return all(test_conditions)

def rem_leading_zero(string_to_remove):
    """remove leading 0 unless string itself"""

    if len(string_to_remove) > 1:
        if string_to_remove[0] == '0':
            return string_to_remove[1:]

def add_binary(first_string_bin:str, second_string_bin:str):
    """Accepts to binary strings and returns their sum

    Args:
        first_string_bin (str): 
        second_string_bin (str):

    Returns:
        str: string of bits
    """
    first_string_bin = rem_leading_zero(first_string_bin)
    second_string_bin = rem_leading_zero(second_string_bin)

    if check_is_binary(first_string_bin) and check_chars_are_1_and_0(second_string_bin):
        solution = None
        new_added_string = ''
        count_ = 0
        for i in range(len(first_string_bin)):
            solution = int(first_string_bin[-i]) + int(second_string_bin)
            if solution in (0,1):
                if len(first_string_bin) > 1:
                    solution = first_string_bin[:-i] + str(solution)
                return str(solution)
            else:
                count_ +=1
                new_added_string += '0'
                if count_ == len(first_string_bin):
                    solution = '1' + new_added_string
                    return solution
        print(new_added_string)
    return 'string passed is not a valid binary string'

print(add_binary('1', '1'))