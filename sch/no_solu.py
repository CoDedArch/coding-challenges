def creating_dict(nums_in_line:list, dict_of_nums:dict, line_no):
    """This function will loop through the list and create a dictionary
        with key being the number and its value will be a new dict with 
        keys count and onLine

        the value for count is the number of appearance of a number

        the value for onLine is a list on of lines on which the number appeared on
    """
    for num in nums_in_line:
        num = num.rstrip('\n')
        if num not in dict_of_nums.keys():
            dict_of_nums[num] = {'count': 1, 'onLine': []}
            dict_of_nums[num]['onLine'].append(line_no)
        else:
            dict_of_nums[num]['count'] += 1
            dict_of_nums[num]['onLine'].append(line_no)

nums_dict = {}
with open('nums.txt', 'r') as numsFile:

    """with is a context manager, it will automatically close the file"""
    for line_no, line in enumerate(numsFile.readlines()):
        nums_in_line = line.split(' ')
        creating_dict(nums_in_line, nums_dict, line_no+1)
       
    print(nums_dict)