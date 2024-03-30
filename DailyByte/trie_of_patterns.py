import unittest

patterns = []
class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

    def dfs(self, node, prefix):
        if node.children:
            for char, child in node.children.items():
                self.dfs(child, prefix + char)
        else:
            print(prefix)

    def display(self):
        self.dfs(self.root, "")


def set_patterns(n):
    i = 1
    while i <= n:
        is_a_valid_pattern = False
        while not is_a_valid_pattern:
            pattern = input('enter the genome pattern; allowable characters are: (A,C,G,T): ')    
            is_a_valid_pattern = confirm_valid_pattern(pattern)
        patterns.append(pattern)
        if n-i > 0:
            print(f'Genome valid and accepted-------> remaining {n-i} genome patterns')
        i += 1
    return

def confirm_valid_pattern(pattern:str):
    is_prefix = False
    for pi in patterns:
        is_prefix = pattern.startswith(pi)
        if is_prefix:
            break
    return set(pattern) <= {'A', 'C', 'G', 'T'} and not is_prefix


is_in_range = True
while(is_in_range):
    n = int(input('enter the length of your parttens: '))
    if n > 0 and n <= 100:
        is_in_range = False

set_patterns(n=n)

trie = Trie()
for pattern in patterns:
    trie.insert(pattern)
trie.display()


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("ACGT")
        self.assertEqual(self.trie.root.children["A"].char, "A")
        self.assertEqual(self.trie.root.children["A"].children["C"].char, "C")

    def test_insert_multiple(self):
        self.trie.insert("ACGT")
        self.trie.insert("ACGA")
        self.assertEqual(self.trie.root.children["A"].children["C"].children["G"].children["T"].char, "T")
        self.assertEqual(self.trie.root.children["A"].children["C"].children["G"].children["A"].char, "A")

if __name__ == "__main__":
    unittest.main()