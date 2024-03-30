class TriePatterns:
    def __init__(self,n:int, patterns:list) -> None:
            self.patterns = patterns
            self.n = n
            self.graph = {}
    def form_graph(self):
        # add root
        self.graph['0'] = set()
        for pi in self.patterns:
            self.graph['0'].add(pi[0])
            # for edges as we go
            self.graph[pi[0]] = set()
            self.add_edge(pi)
           
        print(self.graph)
    
    def add_edge(self, genome):
        
        if len(genome) < 2: 
            print(genome)
            return

        initial_prefix, next_char = genome[0], genome[1]
        if initial_prefix in self.graph:
            self.graph[initial_prefix].add(next_char)
        else:
            print('Key does not exist')
            self.graph[initial_prefix] = {next_char}
        
        if next_char not in self.graph:
            self.graph[next_char] = set()

        return self.add_edge(genome[1:])

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
test_pattern.form_graph()
