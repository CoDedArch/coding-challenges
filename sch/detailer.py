
# Refactor the structured codes into class
class Detailer:
    def __init__(self, pathto:str='nums.txt') -> None:
        self.file_path = pathto
        self.dictOfNums = {}

    
    def __dictionizer(self, nums_in_line:list, line_no):
        for num in nums_in_line:
            num = num.rstrip('\n')
            if num not in self.dictOfNums.keys():
                self.dictOfNums[num] = {'count': 1, 'onLine': []}
                self.dictOfNums[num]['onLine'].append(line_no)
            else:
                self.dictOfNums[num]['count'] += 1
                self.dictOfNums[num]['onLine'].append(line_no)

    def __getNumsInLineOf(self, pathto:str) -> None:
        """ ln ----> line """
        
        with open(pathto, 'r') as numsFile:
            for ln_no, ln in enumerate(numsFile.readlines()):
                nums_in_line = ln.split(' ')
                self.__dictionizer(nums_in_line, ln_no+1)
    
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
        print("NUMBER---------------------COUNT--------------------LINES APPEARED IN", end='\n')
        for key, value in self.dictOfNums.items():
            print(f'{key} ------------------------- {value['count']}  ------------------------ {value['onLine']}')

    def getNumDetails(self, num):
        self.__do()
        try:
            print("NUMBER---------------------COUNT--------------------LINES APPEARED IN", end='\n')
            print(f'{num} ------------------------- {self.dictOfNums[num]['count']}  ------------------------ {self.dictOfNums[num]['onLine']}')
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