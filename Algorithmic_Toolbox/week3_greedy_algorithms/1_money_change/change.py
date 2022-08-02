# Uses python3
import sys

def get_change(m):
    #write your code here
    if m < 5 :
        return m
    elif m < 10 :
        return 1 + m - 5
    else :
        return m//10 + get_change(m%10)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
