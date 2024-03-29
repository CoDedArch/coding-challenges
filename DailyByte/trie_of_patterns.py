class TriePatterns:
    def __init__(self,n:int, patterns:list) -> None:
            self.patterns = patterns
            self.n = n

    def set_patterns(self):
        i = 1
        self.patterns = []
        while i <= self.n:
            is_a_valid_pattern = False
            while not is_a_valid_pattern:
                pattern = input('enter the genome pattern; allowable characters are: (A,C,G,T): ')    
                is_a_valid_pattern = self.confirm_valid_pattern(pattern)
            self.patterns.append(pattern)
            if self.n-i > 0:
                print(f'Genome valid and accepted-------> remaining {self.n-i} genome patterns')
            i += 1
        return

    def confirm_valid_pattern(self, pattern:str):
        is_prefix = False
        for pi in self.patterns:
            is_prefix = pattern.startswith(pi)
            if is_prefix:
                break
        return set(pattern) <= {'A', 'C', 'G', 'T'} and not is_prefix



is_in_range = True
while(is_in_range):
    n = int(input('enter the length of your parttens: '))
    if n > 0 and n <= 100:
        is_in_range = False


test_pattern = TriePatterns(n=n, patterns=[])
test_pattern.set_patterns()
