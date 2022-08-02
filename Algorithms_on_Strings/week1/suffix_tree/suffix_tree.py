# python3
import sys

import sys
class TrieNode :
    def __init__(self, start, end) :
        self.start = start
        self.end = end
        #self.char = char
        self.children = {}
        self.is_suffix = False
        #self.is_word = False

    def print_node(self) :
        for char in sorted(self.children.keys()) :
            node = self.children[char]
            print(text[node.start: node.end])
            #print("{}->{}:{}".format(node.start, node.end, text[node.start: node.end]))
            node.print_node()

class Suffix_Trie :
    def __init__(self, text) :
        self.head = TrieNode(0, 0)
        self.trie = self.make_trie()
        self.text = text

    def make_trie(self) :
        #text = self.text
        n = len(text)
        for idx in range(n-1,-1,-1) :
        #for idx in range(n) :
            node = self.head
            pos = idx
            while pos < n :
                char = text[pos]
                if text[pos] not in node.children : ########### if the suffix diverges from node
                    new_node = TrieNode(pos, n)
                    node.children[char] = new_node
                    new_node.is_suffix = idx
                else :
                    next_node = node.children[char]
                    start = next_node.start
                    end = next_node.end
                    l = 0
                    while l < end - start and text[start + l] == text[pos + l] :
                        l += 1
                    if l == end - start :  ############## if the suffix reaches the next_node
                        pos += l
                        node = next_node
                    else :                ################ if the suffix diverges from the edge [node, next_node]
                        mid_node = TrieNode(pos, pos+l)
                        node.children[char] = mid_node
                        next_node.start = start + l
                        mid_node.children[text[next_node.start]] = next_node
                        pos += l
                        node = mid_node

    def print_trie(self) :
        self.head.print_node()

text = "AAAAAAAABAAAAAAAA$"
suff = Suffix_Trie(text)
suff.print_trie()

# def build_suffix_tree(text):
#
#
#   result = []
#   # Implement this function yourself
#   return result
#
#
# if __name__ == '__main__':
#   text = sys.stdin.readline().strip()
#   suff = Suffix_Trie(text)
#   suff.print_trie()
