def binary_search(keys, query):
    # write your code here
    l = 0
    r = len(keys) - 1
    if query < keys[0] or query > keys[-1] : return -1

    while r > l :
        mid = (r+l)//2
        if query == keys[mid] :
            return mid
        elif query < keys[mid] :
            r = mid - 1
        else :
            l = mid + 1
    return l if keys[l] == query else -1

# keys = [1, 5, 8, 12, 13]
# query = -100
# print(binary_search(keys, query))

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
