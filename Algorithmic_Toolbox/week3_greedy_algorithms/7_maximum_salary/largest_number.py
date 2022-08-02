#Uses python3

import sys

def largest_number(A):
    #write your code here
        return "".join(list(map(str,sorted(A,key=lambda x:-x/(10**(len(str(x)))-1)))))
# A = [23, 39, 92]
# print(largest_number(A))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a = data[1:]
    print(largest_number(a))
