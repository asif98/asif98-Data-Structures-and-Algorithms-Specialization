# python3
import sys
from collections import defaultdict


def build_suffix_array(s) :
    char_set = set(list(s))
    char_sorted = sorted(list(char_set))
    def char_order(char) :
        return char_sorted.index(char)

    count = [0]*len(char_sorted)
    for idx, char in enumerate(s) :
        count[char_order(char)] += 1
    for idx in range(1, len(count)) :
        count[idx] += count[idx-1]
    order = [None]*len(s)
    for idx in range(len(s)-1,-1,-1) :
        char = s[idx]
        count[char_order(char)] -= 1
        order[count[char_order(char)]] = idx
    print("order       = ", order)
    order_class = [None]*len(s)
    for idx in order :
        order_class[idx] =  char_order(s[idx])
    print("order_class = ", order_class)

    ####################################

    def sortDouble(s, L, order, order_class) :
        count = [0]*len(s)
        new_order = [None]*len(s)

        for cl in order_class :
            count[cl]  += 1
        for idx in range(1, len(count)) :
            count[idx] += count[idx-1]

        for idx in range(len(s)-1, -1, -1) :
            start = (order[idx] - L) %len(s)
            cl = order_class[start]
            count[cl] -= 1
            new_order[count[cl]] = start
        print("order       = ", new_order)
        return new_order

    def updateClass(s, L, new_order, order_class) :
        new_order_class = [None]*len(s)
        new_order_class[new_order[0]] = 0
        prev_class = 0

        start = order_class[new_order[0]]
        mid = order_class[(new_order[0] + L) %len(s)]

        # for idx in range(1, len(s)) :
        #     if order_class[new_order[idx]] == order_class[new_order[idx-1]] and order_class[new_order[idx]+L] == order_class[new_order[idx-1]+L] :

        for idx in new_order[1:] :
            if order_class[idx] == start and order_class[(idx + L) %len(s)] == mid :
                new_order_class[idx] = prev_class
            else :
                prev_class += 1
                new_order_class[idx] = prev_class
            start = order_class[idx]
            mid = order_class[(idx + L) %len(s)]

        print("order_class = ", new_order_class)
        return new_order_class

    L = 1
    while L < len(s) :
        order = sortDouble(s, L, order, order_class)
        order_class = updateClass(s, L, order, order_class)
        L = 2*L

    return order
    # result = []
    # # Implement this function yourself
    # return result
s = "AACGATAGCGGTAGA$"
build_suffix_array(s)

# if __name__ == '__main__':
#   s = sys.stdin.readline().strip()
#   print(" ".join(map(str, build_suffix_array(s) )))
