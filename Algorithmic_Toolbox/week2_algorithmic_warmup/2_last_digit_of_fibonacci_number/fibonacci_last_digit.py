# Uses python3
import sys

def get_fibonacci_last_digit(n):
    a = 1 ## fib(-1)
    b = 0  ## fib(0)
    for _ in range(n) :
        a, b = b%10, (a+b)%10

    return b

# print(get_fibonacci_last_digit(331))
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
