import functools
print('11'.replace('1', '0'))

def convert_list_to_str(list_to_convert:str):
    new_str = ''
    for i in list_to_convert:
        new_str += i
    print(new_str)
    return new_str

def check_chars_are_1_and_0(string_to_check:str):
    all_chars_binary = True
    for char in string_to_check:
        if not char in ('1', '0'):
            all_chars_binary = False
            break
    return all_chars_binary

def check_is_binary(string_to_check:str):
    test_conditions = [
        string_to_check.isnumeric(),
        check_chars_are_1_and_0(string_to_check)
    ]
    return all(test_conditions)

def add_binary(first_string_bin:str, second_string_bin:str):
    """_summary_

    Args:
        first_string_bin (str): _description_
        second_string_bin (str): _description_

    Returns:
        _type_: _description_
    """
    if check_is_binary(first_string_bin) and check_chars_are_1_and_0(second_string_bin):
        
    return 'string passed is not a valid binary string'

print(add_binary('11', '1'))