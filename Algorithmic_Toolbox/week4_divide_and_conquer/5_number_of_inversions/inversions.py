import sys

def get_number_of_inversions(arr):
    def helper(left, right) :
        number_of_inversions = 0
        if right == left :
            return 0
        mid = (left + right) // 2
        number_of_inversions += helper(left, mid)
        number_of_inversions += helper(mid+1, right)
        i = left
        j = mid + 1
        new_list = []
        while i <= mid or j <= right :
            if i <= mid and (j>right or arr[i] <= arr[j]) :
                new_list.append(arr[i])
                i += 1
            else :
                new_list.append(arr[j])
                number_of_inversions += mid - i + 1
                j += 1
        arr[left:right+1] = new_list
        return number_of_inversions

    res = helper(0, len(arr)-1)
    #print(arr)
    return res

# arr = [1,6,5,6,6,2]
# print(get_number_of_inversions(arr))
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *arr = list(map(int, input.split()))
    print(get_number_of_inversions(arr))
