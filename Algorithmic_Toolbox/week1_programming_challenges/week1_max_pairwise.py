import sys

data = sys.stdin.readlines()

#n = int(data[0])
arr = list(map(int, data[1].split()))

max1 = 0
max2 = 0

for num in arr :
    max1, max2 = sorted([max1, max2, num], reverse = True)[:2]

print(max1*max2)
