# Uses python3
import sys

def gcd(a, b):

    a, b = sorted([a, b])

    if a == 0 : return b

    q, r = divmod(b, a)

    return gcd(r, a)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
