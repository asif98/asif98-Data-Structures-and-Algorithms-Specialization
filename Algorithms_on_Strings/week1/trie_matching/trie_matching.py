# python3
import sys

# NA = -1
#
# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4

class TrieNode :
	def __init__(self) :
		self.children = {}
		self.is_word = False

	# def print_node(self) :
	#     for char in self.children :
	#         next_node = self.children[char]
	#         print("{}->{}:{}".format(self.idx, next_node.idx, char))
	#         next_node.print_node()

class Trie :
	def __init__(self) :
		self.head = TrieNode()
		#self.count = 1
	def insert(self, word) :
		node = self.head
		for char in word :
			if char not in node.children :
				node.children[char] = TrieNode()
			node = node.children[char]
		node.is_word = True

def solve (text, n, patterns):
	trie = Trie()
	result = []
	for word in patterns :
		trie.insert(word)
	for i in range(len(text)) :
		node = trie.head
		for j in range(i, len(text)) :
			char = text[j]
			if char in node.children :
				node = node.children[char]
			else :
				break
			if node.is_word :
				result.append(i)
				break
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
