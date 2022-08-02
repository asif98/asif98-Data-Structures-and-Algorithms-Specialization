# Uses python3
import sys
import math

def optimal_summands(n):
    k = (math.sqrt(8*n+1) - 1)//2
    k = int(k)
    summands = list(range(1, k)) + [n - k*(k-1)//2]

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
