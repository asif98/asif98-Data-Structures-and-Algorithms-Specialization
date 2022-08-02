# python3
import sys


def compute_min_refills(distance, tank, stops):

    refill = -1
    remaining = 0
    stops = [0] + stops + [distance]

    for i in range(len(stops)-1) :
        if stops[i+1] - stops[i] > tank :
            return -1
        elif stops[i+1] - stops[i] <= remaining :
            remaining -= stops[i+1] - stops[i]
        else :
            refill += 1
            remaining = tank - stops[i+1] + stops[i]

    return refill
# print(compute_min_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_refills(10, 3, [1,2,5,9]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
