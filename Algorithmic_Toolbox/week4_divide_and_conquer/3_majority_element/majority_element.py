# Uses python3
import sys

def get_majority_element(arr):

    def helper(l, r) :  ## returns [val, no_appearance] if no_appearance >= n/2, else [None, None]
        if l == r :
            return arr[l]
        else :
            mid = (l+r)//2
            num1 = helper(l, mid)
            num2 = helper(mid+1, r)

            if num1 == None and num2 == None :
                return None
            elif num1 == num2 :
                return num1
            else :
                 app1 = arr[l: r+1].count(num1)
                 if 2*app1 > r-l+1 : return num1

                 app2 = arr[l: r+1].count(num2)
                 if 2*app2 > r-l+1 : return num2

                 return None

    return helper(0, len(arr)-1)

#print(get_majority_element([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *arr = list(map(int, input.split()))
    if get_majority_element(arr) == None :
        print(0)
    else:
        print(1)
