# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n < 2 : return n 
    fib = [0, 1]
    for i in range(n-1) :
        fib.append((fib[-1] + fib[-2])%m)
        if fib[-1] == 1 and fib[-2] == 0 :
            period = len(fib) - 2
            break
    else :
        return fib[-1]

    # print("period = ",period)
    # print(fib)
    return fib[n%period]

# print(get_fibonacci_huge_naive(12, 3))

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
