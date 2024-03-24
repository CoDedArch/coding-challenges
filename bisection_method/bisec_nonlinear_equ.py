class Bisection(object):
    def __init__(self, prob_func:str, interval:str):
        self.prob_func = prob_func
        self.interval = interval.split(',')
        self.limit1 = None
        self.limit2 = None
        self.middle_limit = None
        self.iteration = 0
    
    def findIndependentVar(self):
        return [self.prob_func[i+1] for i in range(len(self.prob_func)) if self.prob_func[i] == '('][0]
    def check_assumptions(self, interval):
        infinity = float('inf')
        self.limit1 = self.evaluate(interval[0])
        self.limit2 = self.evaluate(interval[1])
        print('limit 1: ',self.limit1, 'limit 2: ',self.limit2, 'product=', self.limit1 * self.limit2)

        return all([self.limit1 != infinity, self.limit2 != infinity, self.limit1 * self.limit2 < 0])
    
    
    def evaluate(self,interval_elment:str):
       return eval(self.prob_func.replace(self.findIndependentVar(), interval_elment).split('=')[1])

    def bisect(self):
        self.iteration += 1
        if self.iteration == 10:
            print('iter @ 10:---------------------------------------- ', self.middle_limit)
        self.middle_limit = (float(self.interval[0]) + float(self.interval[1]))/ 2
        print(self.middle_limit)
        if self.evaluate(str(self.middle_limit)) == 0:
            return print('the correct estimated root is: ', self.middle_limit,
                         'at the end of iteration: ', self.iteration)
        else: 
            if self.check_assumptions([self.interval[0]] + [str(self.middle_limit)]):
                print('entered first interval')
                self.interval = [self.interval[0]] + [str(self.middle_limit)]
                self.bisect()
            elif self.check_assumptions([self.interval[1]] + [str(self.middle_limit)]):
                print('entered second interval')
                self.interval = [self.interval[1]] + [str(self.middle_limit)]
                self.bisect()
            else:
                return "given function doesn’t follow one of assumptions."



user_inpput = input("please enter your function here in the format the computer will understand: ")
interval = input("please enter the interval here: ")
first = Bisection(user_inpput,interval=interval)
first.bisect()