#Uses python3
import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    for pay, click in zip(a, b):
        res += pay*click
    return res

# print(max_dot_product([1, 3, -5], [-2, 4, 1]))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
