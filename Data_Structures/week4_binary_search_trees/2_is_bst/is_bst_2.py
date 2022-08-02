#!/usr/bin/python3

import sys, threading
from collections import deque+
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if not tree:
        return True
    queue = list()
    mn, mx = float("-inf"), float("inf")
    node_key, left_index, right_index = tree[0]
    queue.append([node_key, left_index, right_index, mn, mx])
    while queue:
        node_key, left_index, right_index, mn, mx = queue.pop(0)
        if mn <= node_key <= mx:
            if 0 <= left_index < len(tree):
                key, l, r = tree[left_index]
                queue.append([key, l, r, mn, node_key])
            if 0 <= right_index < len(tree):
                key, l, r = tree[right_index]
                queue.append([key, l, r, node_key, mx])
        else:
            return False
    return True


def main():

    nodes = int(sys.stdin.readline().strip())
    tree = []

    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
