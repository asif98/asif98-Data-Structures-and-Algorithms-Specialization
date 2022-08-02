#Uses python3
import sys
import math
import bisect

def minimum_distance(X, Y):
    #write your code here
    points = sorted(zip(X, Y))
    #print(points)

    def dist(i, j) :
        xi, yi = points[i]
        xj, yj = points[j]
        return math.sqrt((xi-xj)**2 + (yi-yj)**2)

    def helper(left, right) :
        #print(left, right, points[left], points[right])
        if right == left :
            return float("inf")
        elif right == left + 1 :
            return dist(left, right)
        else :
            mid = (left+right)//2
            x_mid = points[mid][0]
            #print(x_mid)

            d = min(helper(left, mid), helper(mid+1, right))

            idx_l = bisect.bisect_left(points, (x_mid - d, 0), left, right+1)
            idx_r = bisect.bisect_right(points, (x_mid + d, float("inf")), left, right+1)

            for idx in range(idx_l, idx_r - 1) :
                for j in range(idx+1, min(idx+7, idx_r)) :
                    d = min(d, dist(idx, j))
            return d
    return helper(0, len(points)-1)

# X = [0,3]
# Y = [0,4]
# print(minimum_distance(X,Y))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
