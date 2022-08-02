# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort()
    #print(segments)
    while segments :
        new_point = segments.pop()[0]
        points.append(new_point)
        while segments and segments[-1][1] >=  new_point :
            segments.pop()
    return points[::-1]

# segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
# #segments = [[1, 3], [2, 5], [3, 6]]
# print(optimal_points(segments))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(zip(data[::2], data[1::2]))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
