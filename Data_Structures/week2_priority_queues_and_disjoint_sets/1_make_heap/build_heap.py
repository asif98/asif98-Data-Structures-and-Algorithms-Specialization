# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    n = len(data)
    Swaps = []
    def swap(i, j) :
        Swaps.append((i, j))
        data[i], data[j] = data[j], data[i]


    def siftdown (i) :
        smallest = i
        if 2*i + 1 < n and data[2*i+1] < data[smallest] :
            smallest = 2*i + 1
        if 2*i + 2 < n and data[2*i+2] < data[smallest] :
            smallest = 2*i + 2
        if smallest != i :
            swap(i, smallest)
            siftdown(smallest)

    for i in range(n,-1,-1) :
        siftdown(i)

    #print(data)
    return Swaps

# data = [5, 4, 3, 2, 1]
# print(build_heap(data))

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    Swaps = build_heap(data)

    print(len(Swaps))
    for i, j in Swaps:
        print(i, j)


if __name__ == "__main__":
    main()
