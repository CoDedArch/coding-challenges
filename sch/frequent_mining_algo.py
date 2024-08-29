
# Refactor the structured codes into class
class FIMAlgorithm:
    """
        This is my Implementation of the Frequent Itemset Mining Algorithm

        There is a flaw in my Implementation, I don't know when to stop recursing

        so i have a stopping_criterion set to 5 iterations, this isn't Ideal.
    """
    # initialize FIMALOG
    def __init__(self, pathto:str='nums.txt') -> None:
        self.file_path = pathto
        self.dictOfNums = {}
        self.transactions = {}
        self.mini_support = 2
        self.current_iteration_of_Frequent_itemset = 1
        self.stopping_criterion = True
        self.frequentItemset = []
        self.kindOfDetails = ''

    def __findSupportCount(self, nums_in_line:list, line_no):
        """
            create a dictionary from the data into dictOfNums 
            DictionaryOfNumbers is the initial step to get the sup and occurance of a number       
        """
        items_appearing = []
        for num in nums_in_line:
            if num.rstrip('\n'):
                num = int(num.rstrip('\n'))
            else:
                num = int(num)
            items_appearing.append(num)
            if not num == 0:
                self.dictOfNums.setdefault(num,{'count': 0, 'onLine': []})
                self.dictOfNums[num]['count'] += 1
                self.dictOfNums[num]['onLine'].append(line_no)
        
        # form a transaction with items appearing in the transaction
        self.transactions[line_no] = set(items_appearing)


    def __getNumsInLineOf(self, pathto:str) -> None:
        
        """ 
        for a line in the data, get the numbers in the line
        and call the findsupportcount to organize numbers into a dictionary
        ln ----> line 
        """
        with open(pathto, 'r') as numsFile:
            for ln_no, ln in enumerate(numsFile.readlines()):
                nums_in_line = ln.split(' ')
                self.__findSupportCount(nums_in_line, ln_no+1)

        print("transactions")
        print(self.transactions)

    def countMinSup(self, combined_Set:set) -> bool:
        """
        CountMinSup takes a combined set argument and 
        runs through the transaction values to check the sup of the arg

        it returns a true if the arg sup  is >= minsup else false

        """
        print("combined set is")
        print(combined_Set)
        count = 0
        for value in self.transactions.values():
            if combined_Set.issubset(value):
                count+=1

        return True if count >= self.mini_support  else False

    def formItemsetOfSizeN(self):
        """
        this function will create a workingset from the frequentItemset 
        based on the current iteration of the frequent itemset

        It Calls the CountMinSup and passes the new itemset to it, to check the sup of the item set

        if the sup of the itemset is >= the minsup, the itemset is added to the frequent itemset
        """
        workingset = [item for item in self.frequentItemset if len(item) == self.current_iteration_of_Frequent_itemset-1]
        for i in range(0,len(workingset)):
            for j in range( i+1, len(workingset)):
                conbined_items = workingset[i].union(workingset[j])
                self.frequentItemset.append(conbined_items) if self.countMinSup(combined_Set=conbined_items) and conbined_items not in self.frequentItemset else print("not added")

# organize numbers which are greater than or equal to the minimum support
    def frequentItemsetMining(self):
        """
        This is a recursive Function which finds the frequent Item set
        """

        print("Forming our Frequent Item Set ...")

        # this block of codes will run only when the frequent itemset is empty
        if not self.frequentItemset:
            print(f"Frequent ItemSet is Been populated by item set of size {self.current_iteration_of_Frequent_itemset}")
            for num in self.dictOfNums.copy():
                if self.dictOfNums[num]['count'] >= self.mini_support:
                    self.frequentItemset.append({num})
                else:
                    del self.dictOfNums[num]

            self.frequentItemset = sorted(self.frequentItemset)
            print("frequent item set:", end='\t')
            print(self.frequentItemset)
            self.current_iteration_of_Frequent_itemset += 1
            
        else:
            print(f"form an itemset with size {self.current_iteration_of_Frequent_itemset}")

            # this function forms an items set of size N base on the current iteration of the frequent itemset
            self.formItemsetOfSizeN()

            # increament the current iteration of frequent Itemset
            self.current_iteration_of_Frequent_itemset += 1
            
            print("frequent Itemset is ....")
            
            print(self.frequentItemset)
            
            # this isn't a valid stopping criterion; it won't work for all test cases
            if self.current_iteration_of_Frequent_itemset > 5:
                self.stopping_criterion = False

        # recursively call the frequentItemsetMining function
        self.frequentItemsetMining() if self.stopping_criterion else print("done")


# This is runs the main logic of the FIMAlgorithm class
    def __do(self):
        """This Function is an Add on to the main logic of FIMAlgorithm"""

        hasOwnFile = input("Do You have your own file? (y/n): ")
        file_exist = True

# check if the file exist or not and repeatedly ask for the correct file if it doesn't exist
        while(file_exist):
            if hasOwnFile == 'y':
                self.file_path = input("Enter path to file {Exclude .txt}: ") + ".txt"

            try:
                self.__getNumsInLineOf(self.file_path)
                file_exist = False
            except FileNotFoundError:
                print("File Doesn't Exist")

        self.kindOfDetails = input('Do you want details of a specific number?(y/n): ')
        

# presents the details in a tabular form
#showing working calls the do function and presents the data in an organized fashion
    def showWorking(self):
        """The Main Excution point"""
        
        self.__do()
        print("NUMBER--------------------- Support Count --------------------LINES APPEARED IN", end='\n')
        for key, value in self.dictOfNums.items():
            print(f'{key} -------------------------   {value['count']}           ------------------------ {value['onLine']}')

        # Organize the items which are greater than or equal to the minimum support
        self.frequentItemsetMining()

# returns the details of a specific number in the data
    def getNumDetails(self, num):
        self.__do()
        try:
            print("NUMBER--------------------- NO_OCCURANCE --------------------LINES APPEARED IN", end='\n')
            print(f'{num} -------------------------   {self.dictOfNums[num]['count']}               ------------------------ {self.dictOfNums[num]['onLine']}')
        except KeyError:
            print("Number doesn't Exist in file")
            return
        
        

dr = FIMAlgorithm()

if dr.kindOfDetails != 'y':
    dr.showWorking()
else:
    num = input('Enter the Number: ')
    dr.getNumDetails(num)
