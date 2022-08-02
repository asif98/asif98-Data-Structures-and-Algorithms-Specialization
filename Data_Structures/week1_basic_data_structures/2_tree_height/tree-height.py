# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def compute_height(n, parent) :

    Heights = [None]*n

    def height(vertex) :
        if Heights[vertex] != None :
            return Heights[vertex]
        elif parent[vertex] == -1 :
            Heights[vertex] = 1
            return 1
        else :
            Heights[vertex] = 1 + height(parent[vertex])
            return Heights[vertex]

    maxHeight = 0
    for vertex in range(n) :
        maxHeight = max(maxHeight, height(vertex))
    return maxHeight


# n = 5
# parent = [-1, 0, 4, 0, 3]
# print(compute_height(n, parent))

def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    # Printing answer, write your code here
    print(compute_height(n, parent))


if __name__ == "__main__":
    main()


# class TreeHeight:
#         def read(self):
#                 self.n = int(sys.stdin.readline())
#                 self.parent = list(map(int, sys.stdin.readline().split()))
#
#         def compute_height(self):
#                 # Replace this code with a faster implementation
#                 maxHeight = 0
#                 for vertex in range(self.n):
#                         height = 0
#                         i = vertex
#                         while i != -1:
#                                 height += 1
#                                 i = self.parent[i]
#                         maxHeight = max(maxHeight, height);
#                 return maxHeight;
#
# def main():
#   tree = TreeHeight()
#   tree.read()
#   print(tree.compute_height())
#
# threading.Thread(target=main).start()
