# python3
import sys
from collections import defaultdict

def InverseBWT(bwt):
    n = len(bwt)
    count = defaultdict(int)
    char_order = []
    start = 0
    for i,char in enumerate(bwt) :
        char_order.append(count[char])
        count[char] += 1
        if char < bwt[start] :
            start = i

    count_list = sorted(list(count.items()))

    sum = 0
    cum_count = {}
    for key, val in count_list :
        cum_count[key] = sum
        sum += val
    perm = [ cum_count[char] + char_order[idx] for idx, char in enumerate(bwt) ]

    text = ""
    idx = start
    for _ in range(n) :
        text += bwt[idx]
        idx = perm[idx]

    return text[::-1]

# bwt = "ATG$CAAA"
# print(InverseBWT(bwt))

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
