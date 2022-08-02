# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
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
        self.root = self.nodes[0]


    def inOrder(self):

        self.result = []
        def in_order_recur(node) :
            if node :
                in_order_recur(node.left)
                self.result.append(node.key)
                in_order_recur(node.right)
        in_order_recur(self.root)
        return self.result

    def preOrder(self):
        self.result = []
        def pre_order_recur(node) :
            if node :
                self.result.append(node.key)
                pre_order_recur(node.left)
                pre_order_recur(node.right)
        pre_order_recur(self.root)
        return self.result

    def postOrder(self):
        self.result = []
        def post_order_recur(node) :
            if node :
                post_order_recur(node.left)
                post_order_recur(node.right)
                self.result.append(node.key)
        post_order_recur(self.root)
        return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
