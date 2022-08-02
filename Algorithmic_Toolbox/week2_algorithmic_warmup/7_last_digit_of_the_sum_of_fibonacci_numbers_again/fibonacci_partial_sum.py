# Uses python3
import sys

def fibonacci_partial_sum(m, n):
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

    if m == 0 :
        return fibonacci_sum(n)%10
    else :
        return (fibonacci_sum(n) - fibonacci_sum(m-1))%10

#print(fibonacci_partial_sum(10, 200))

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
