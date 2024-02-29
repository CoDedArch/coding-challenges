class Bisection(object):
    """Bisection method is going to accept a function and the interval for the function"""
    def __init__(self, prob_func:str, interval:str):
        self.prob_func = prob_func
        self.interval = interval.split(',')
        self._limit1_eval = None
        self._limit2_eval = None
        self.middle_limit = None
        self.root = None
    
    def findIndependentVar(self):
        return [self.prob_func[i+1] for i in range(len(self.prob_func)) if self.prob_func[i] == '('][0]
    def satisfyAssumptions(self, interval):
        """
        for a problem to be solved using bisection method
        the function must be continous
        the product of the evaluation of the limits must be less than zero
        """
        infinity = float('inf')
        self._limit1_eval = self.evaluate(interval[0])
        self._limit2_eval = self.evaluate(interval[1])

        return all([self._limit1_eval != infinity, self._limit2_eval != infinity, self._limit1_eval * self._limit2_eval < 0])
    
    
    def evaluate(self,interval_elment:str):
       return eval(self.prob_func.replace(self.findIndependentVar(), interval_elment).split('=')[1])

    def bisect(self):
        self.middle_limit = (int(self.interval[0]) + int(self.interval[1]))/ 2
        if self.evaluate(self.middle_limit) == 0:
            self.root = self.middle_limit
            return self.root
        else: 
            if self.satisfyAssumptions(self.interval[0] + [str(self.middle_limit)]):
                self.interval = self.interval[0] + [str(self.middle_limit)]
                self.bisect()
            elif self.satisfyAssumptions(self.interval[1] + [str(self.middle_limit)]):
                self.interval = self.interval[1] + [str(self.middle_limit)]
                self.bisect()
            else:
                return "given function doesn’t follow one of assumptions."


first = Bisection('f(x) = 2*x + 3*x**2', '1,2')
print(first.bisect())
