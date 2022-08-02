# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    res = []
    maximums = deque()
    for i in range(len(sequence)):

        if i >= m :
            prev = sequence[i-m]
            if prev == maximums[0] :
                maximums.popleft()

        nxt = sequence[i]
        while maximums and maximums[-1] < nxt :
            maximums.pop()
        maximums.append(nxt)
        #print(maximums)
        if i >= m-1 : res.append(maximums[0])

    return res

# sequence = [2, 7, 3, 1, 5, 2, 6, 2]
# m = 4
# print(max_sliding_window_naive(sequence, m))

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
