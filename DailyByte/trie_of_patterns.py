class TriePatterns:
    def __init__(self,patterns:list) -> None:
            self.patterns = patterns

    def set_patterns(self,length_of_patterns):
        i = 1
        self.patterns = []
        while i <= length_of_patterns:
            is_a_valid_pattern = False
            while not is_a_valid_pattern:
                pattern = input('enter the genome pattern allowable characters are: (A,C,G,T): ')    
                is_a_valid_pattern = self.confirm_valid_pattern(pattern)
            self.patterns.append(pattern)
        return

    @staticmethod
    def confirm_valid_pattern(pattern):
        return set(pattern) <= {'A', 'C', 'G', 'T'}







is_in_range = True
while(is_in_range):
    n = int(input('enter the length of your parttens: '))
    if n > 0 and n <= 100:
        is_in_range = False


