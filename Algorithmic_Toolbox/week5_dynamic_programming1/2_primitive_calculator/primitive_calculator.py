# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    dp_dict = {1:[1], 2:[1, 2], 3:[1, 3]}

    def dp(m) :

        if m in dp_dict : return dp_dict[m]

        q2, r2 = divmod(m, 2)
        q3, r3 = divmod(m, 3)
        cand1 = dp(m//2) + list(range(2*(m//2), m+1))
        cand2 = dp(m//3) + list(range(3*(m//3), m+1))

        if len(cand1) <= len(cand2) :
            ans = cand1
        else :
            ans = cand2

        dp_dict[m] = ans
        return ans

    return dp(n)
# print(optimal_sequence(996234))

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
