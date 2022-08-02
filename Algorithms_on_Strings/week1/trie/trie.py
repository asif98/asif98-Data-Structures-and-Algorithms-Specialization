#Uses python3
import sys
class TrieNode :
    def __init__(self, idx) :
        self.idx = idx
        #self.char = char
        self.children = {}
        self.is_word = False

    def print_node(self) :
        for char in self.children :
            next_node = self.children[char]
            print("{}->{}:{}".format(self.idx, next_node.idx, char))
            next_node.print_node()

class Trie :
    def __init__(self) :
        self.head = TrieNode(0)
        self.count = 1
    def insert(self, word) :
        node = self.head
        for char in word :
            if char not in node.children :
                node.children[char] = TrieNode(self.count)
                self.count += 1
            node = node.children[char]
        node.is_word = True
    def print_trie(self) :
        self.head.print_node()

def build_trie(patterns):
    trie = Trie()
    for word in patterns :
        trie.insert(word)
    return trie
    
# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.



if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    trie = build_trie(patterns)
    trie.print_trie()
    # for node in tree:
    #     for c in tree[node]:
    #         print("{}->{}:{}".format(node, tree[node][c], c))
