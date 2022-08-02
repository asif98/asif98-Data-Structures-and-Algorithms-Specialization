# Uses python3
def calc_fib(n):
    a = 1 ## fib(-1)
    b = 0  ## fib(0)
    for _ in range(n) :
        a, b = b, a+b

    return b

n = int(input())
print(calc_fib(n))
