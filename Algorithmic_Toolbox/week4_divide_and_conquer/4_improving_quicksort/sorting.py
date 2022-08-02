# Uses python3
import sys
import random

def partition3(a):
    def helper(l, r) :
        if r > l :
            x = a[l]
            j = l
            k = l  ######### a[l:k] < x, a[k:j] == x, a[j:i] > x
            for i in range(l + 1, r + 1):
                if a[i] < x:
                    k += 1
                    j += 1
                    a[i], a[j], a[k] = a[j], a[k], a[i]
                elif a[i] == x :
                    j += 1
                    a[i], a[j] = a[j], a[i]
            a[l], a[k] = a[k], a[l]
            helper(l, k)
            helper(j+1, r)
    helper(0, len(a)-1)

# arr = [3, 3, 3, 3]
# print(partition3(arr))
#
# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    partition3(a)
    for x in a:
        print(x, end=' ')
