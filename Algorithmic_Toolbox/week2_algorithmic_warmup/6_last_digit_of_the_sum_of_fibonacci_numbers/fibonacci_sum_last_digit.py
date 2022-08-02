# Uses python3
import sys

def fibonacci_sum(n):
    if n < 2 : return n
    fib = [0, 1]
    for i in range(n+1) :
        fib.append((fib[-1] + fib[-2])%10)
        if fib[-1] == 1 and fib[-2] == 0 :
            period = len(fib) - 2
            break
    else :
        return (fib[-1]-1)%10

    # print("period = ",period)
    # print(fib)
    return (fib[(n+2)%period]-1)%10

#print(fibonacci_sum(3))
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
