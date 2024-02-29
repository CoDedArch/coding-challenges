class Bisection(object):
    """Bisection method is going to accept a function and the interval for the function"""
    def __init__(self, prob_func:str, interval:str):
        self.prob_func = prob_func
        self.interval = interval.split(',')
        self._limit1_eval = None
        self._limit2_eval = None
        self.middle_limit = None
        self.iteration = 0
    
    def findIndependentVar(self):
        return [self.prob_func[i+1] for i in range(len(self.prob_func)) if self.prob_func[i] == '('][0]
    def satisfyAssumptions(self, interval):
        """
        for a problem to be solved using bisection method
        the function must be continous
        the product of the evaluation of the limits must be less than zero
        difference between xi and xu is a very small value
        """
        infinity = float('inf')
        self._limit1_eval = self.evaluate(interval[0])
        self._limit2_eval = self.evaluate(interval[1])
        print('limit 1: ',self._limit1_eval, 'limit 2: ',self._limit2_eval, 'product=', self._limit1_eval * self._limit2_eval)

        return all([self._limit1_eval != infinity, self._limit2_eval != infinity, self._limit1_eval * self._limit2_eval < 0])
    
    
    def evaluate(self,interval_elment:str):
       return eval(self.prob_func.replace(self.findIndependentVar(), interval_elment).split('=')[1])

    def bisect(self):
        self.iteration += 1
        if self.iteration == 10:
            print('iter @ 10:---------------------------------------- ', self.middle_limit)
        self.middle_limit = (float(self.interval[0]) + float(self.interval[1]))/ 2
        print(self.middle_limit)
        if self.evaluate(str(self.middle_limit)) == 0:
            """return the root"""
            return print('the correct estimated root is: ', self.middle_limit,
                         'at the end of iteration: ', self.iteration)
        else: 
            if self.satisfyAssumptions([self.interval[0]] + [str(self.middle_limit)]):
                print('entered first interval')
                self.interval = [self.interval[0]] + [str(self.middle_limit)]
                self.bisect()
            elif self.satisfyAssumptions([self.interval[1]] + [str(self.middle_limit)]):
                print('entered second interval')
                self.interval = [self.interval[1]] + [str(self.middle_limit)]
                self.bisect()
            else:
                return "given function doesn’t follow one of assumptions."


first = Bisection('f(x) = x**3 - 0.165*x**2 + 3.993 * 10**-4', '0,0.11')
first.bisect()

