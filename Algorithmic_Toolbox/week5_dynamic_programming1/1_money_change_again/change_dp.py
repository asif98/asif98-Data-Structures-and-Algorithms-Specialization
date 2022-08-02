# Uses python3
import sys

def get_change(money):
    #write your code here
    dp_arr = [None]*(money+1)
    dp_arr[0] = 0

    def dp(m) :
        if m < 0 :
            return float("inf")
        elif dp_arr[m] != None :
            return dp_arr[m]
        else :
            res = 1 + min(dp(m-1), dp(m-3), dp(m-4))
            dp_arr[m] = res
            return res
    return dp(money)


if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
