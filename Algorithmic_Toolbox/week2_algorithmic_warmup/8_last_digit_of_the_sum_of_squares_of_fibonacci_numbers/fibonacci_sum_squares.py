# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    if n<2 : return n
    fib = [0, 1]
    for i in range(n) :
        fib.append((fib[-1] + fib[-2])%10)
        if fib[-1] == 1 and fib[-2] == 0 :
            period = len(fib) - 2
            break
    else :
        return (fib[-1]*fib[-2])%10

    # print("period = ",period)
    # print(fib)
    return (fib[(n+1)%period]*fib[n%period])%10

#print(fibonacci_sum_squares(1))

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
