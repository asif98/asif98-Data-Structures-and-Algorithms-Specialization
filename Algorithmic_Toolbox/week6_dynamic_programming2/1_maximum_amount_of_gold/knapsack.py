# Uses python3
import sys

def optimal_weight(capacity, weights):
    # write your code here
    dp_dict = {}
    weights.sort()

    def dp(cap, idx) :
        if cap == 0 or idx >= len(weights) :
            return 0
        elif (cap, idx) in dp_dict :
            return dp_dict[(cap, idx)]
        elif cap < weights[idx] :
            return 0
        else :
            ans = max( weights[idx] + dp(cap-weights[idx], idx+1), dp(cap, idx+1) )
            dp_dict[(cap, idx)] = ans
            return ans
    return dp(capacity, 0)

# capacity = 10
# weights = [1, 2, 4, 8]
# print(optimal_weight(capacity, weights))

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
