# Uses python3
import sys
import collections

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    dict = collections.defaultdict(lambda : [0, 0]) ## point -> [[start, end],[pos in points] ]

    for st in starts :
        dict[st][0] += 1
    for end in ends :
        dict[end][1] += 1
    for idx, pt in enumerate(points) :
        dict[pt].append(idx)

    all_points = sorted(dict.keys())

    cur_no_segments = 0
    for pt in all_points :
        #print([pt] + dict[pt])
        cur_no_segments += dict[pt][0]
        for idx in dict[pt][2:] :
            cnt[idx] = cur_no_segments
        cur_no_segments -= dict[pt][1]

    return cnt

# starts, ends, points = [[0,7],[5,10],[1,6,11]]
# print(fast_count_segments(starts, ends, points))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
