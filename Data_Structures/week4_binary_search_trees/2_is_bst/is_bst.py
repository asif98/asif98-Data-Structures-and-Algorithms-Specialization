#!/usr/bin/python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeNode :
	def __init__(self, val) :

		self.key = val
		self.left = None
		self.right = None

class TreeOrders:

	def read(self):
		self.n = int(sys.stdin.readline())
		self.nodes = [None]*self.n
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
	  #self.nodes =

		for i in range(self.n) :
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.nodes[i] = TreeNode(a)
			self.left[i] = b
			self.right[i] = c
		for i in range(self.n) :
			if self.left[i] >= 0 : self.nodes[i].left = self.nodes[self.left[i]]
			if self.right[i] >= 0 : self.nodes[i].right = self.nodes[self.right[i]]

		if self.n > 0 :
			self.root = self.nodes[0]
		else :
			self.root = None


def IsBinarySearchTree(root):
	def helper(node, max, min ) :
		if not node :
			return True
		if node.key <= min or node.key >= max :
			return False
		if helper(node.left, node.key, min) and helper(node.right, max, node.key) :
			return True

	return helper(root, float("inf"), float("-inf"))

def main() :
	tree = TreeOrders()
	tree.read()
	if IsBinarySearchTree(tree.root) :
		print("CORRECT")
	else :
		print("INCORRECT")

threading.Thread(target=main).start()
