# python3
import sys

import sys
def order(char) :
    return "$ACGT".find(char)
class TrieNode :
    def __init__(self, start, end) :
        self.start = start
        self.end = end
        #self.char = char
        self.children = [None]*5
        self.is_suffix = -1
        #self.is_word = False

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
                if not node.children[order(char)] : ########### if the suffix diverges from node
                    new_node = TrieNode(pos, n)
                    node.children[order(char)] = new_node
                    new_node.is_suffix = idx
                else :
                    next_node = node.children[order(char)]
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
                        node.children[order(char)] = mid_node
                        next_node.start = start + l
                        mid_node.children[order(text[next_node.start])] = next_node
                        pos += l
                        node = mid_node

    def print_trie(self) :
        result = []
        def print_node(node) :
            if node :
                if  node.is_suffix >= 0 :
                    result.append(node.is_suffix)
                for next_node in node.children :
                    print_node(next_node)
            # for node in self.children :
            #     if node and node.is_suffix >= 0 :
            #         result.append(node.is_suffix)
            #     #print(text[node.start: node.end])
            #     #print("{}->{}:{}".format(node.start, node.end, text[node.start: node.end]))
            #     if node : node.print_node()
        print_node(self.head)
        return result

# text = "AACGATAGCGGTAGA$"
# suff = Suffix_Trie(text)
# print()

# def build_suffix_array(text):
#
#   result = []
#   # Implement this function yourself
#   return result
#
#
if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  suff = Suffix_Trie(text)
  print(" ".join(map(str, suff.print_trie())))
