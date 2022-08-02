# Uses python3
import sys
import itertools

def partition3(A):
    s = sum(A)
    if s%3 != 0 :
        return 0
    else :
        share = s//3

    A.sort()
    dp_dict = {}

    def dp(idx, target1, target2, target3) :

        if idx == len(A) :
            return target1 == target2 == target3 == 0

        if (idx, target1, target2, target3) in dp_dict :
            return dp_dict[(idx, target1, target2, target3)]

        if A[idx] <= target1 and dp(idx+1, target1-A[idx], target2, target3) :
            dp_dict[(idx, target1, target2, target3)] = True
            return True
        if A[idx] <= target2 and dp(idx+1, target1, target2-A[idx], target3) :
            dp_dict[(idx, target1, target2, target3)] = True
            return True
        if A[idx] <= target3 and dp(idx+1, target1, target2, target3-A[idx]) :
            dp_dict[(idx, target1, target2, target3)] = True
            return True

        dp_dict[(idx, target1, target2, target3)] = False
        return False

    return dp(0, share, share, share)

# A = [3, 3, 3, 3]
# A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
# print(partition3(A))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A)*1)
