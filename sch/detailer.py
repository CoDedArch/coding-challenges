
# Refactor the structured codes into class
class Detailer:
    def __init__(self, pathto:str='nums.txt') -> None:
        self.file_path = pathto
        self.dictOfNums = {}
        self.mini_support = 2
        self.greater_min_support = []

    
    def __dictionizer(self, nums_in_line:list, line_no):
        for num in nums_in_line:
            num = num.rstrip('\n')
            if not num == '0':
                self.dictOfNums.setdefault(num,{'count': 0, 'onLine': []})
                self.dictOfNums[num]['count'] += 1
                self.dictOfNums[num]['onLine'].append(line_no)

    def __getNumsInLineOf(self, pathto:str) -> None:
        """ ln ----> line """
        with open(pathto, 'r') as numsFile:
            for ln_no, ln in enumerate(numsFile.readlines()):
                nums_in_line = ln.split(' ')
                self.__dictionizer(nums_in_line, ln_no+1)

    def getGreaterThanMinSupport(self):
        for num in self.dictOfNums.copy():
            if self.dictOfNums[num]['count'] >= self.mini_support:
                self.greater_min_support.append(num)
            else:
                del self.dictOfNums[num]
        print(self.greater_min_support)

    def __do(self):
        hasOwnFile = input("Do You have your own file? (y/n): ")
        file_exist = True

        while(file_exist):
            if hasOwnFile == 'y':
                self.file_path = input("Enter path to file: ") + ".txt"

            try:
                self.__getNumsInLineOf(self.file_path)
                file_exist = False
            except FileNotFoundError:
                print("File Doesn't Exist")

    def showWorking(self):
        self.__do()
        print("NUMBER--------------------- NO_OCCURANCE --------------------LINES APPEARED IN", end='\n')
        for key, value in self.dictOfNums.items():
            print(f'{key} -------------------------   {value['count']}           ------------------------ {value['onLine']}')

        self.getGreaterThanMinSupport()

    def getNumDetails(self, num):
        self.__do()
        try:
            print("NUMBER--------------------- NO_OCCURANCE --------------------LINES APPEARED IN", end='\n')
            print(f'{num} -------------------------   {self.dictOfNums[num]['count']}               ------------------------ {self.dictOfNums[num]['onLine']}')
        except KeyError:
            print("Number doesn't Exist in file")
            return
        

dr = Detailer()

kindOfDetails = input('Do you want details of a specific number?(y/n): ')
if kindOfDetails != 'y':
    dr.showWorking()
else:
    num = input('Enter the Number: ')
    dr.getNumDetails(num)