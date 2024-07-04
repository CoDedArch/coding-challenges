def dictionizer(nums_in_line:list, dict_of_nums:dict, line_no):
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
    for line_no, line in enumerate(numsFile.readlines()):
        nums_in_line = line.split(' ')
        dictionizer(nums_in_line, nums_dict, line_no+1)
       
    print(nums_dict)