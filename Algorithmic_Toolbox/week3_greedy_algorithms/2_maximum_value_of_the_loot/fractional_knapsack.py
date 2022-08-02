# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    most_precious = sorted(list(zip(weights, values)), key = lambda lst: -lst[1]/lst[0])
    #print(most_precious)
    for w, v in most_precious :
        if capacity >= w :
            capacity -= w
            value += v
        else :
            value += capacity*v/w
            return value
    return value

# capacity = 10
# weights = [30]
# values = [500]
# #print(get_optimal_value(capacity, weights, values))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
