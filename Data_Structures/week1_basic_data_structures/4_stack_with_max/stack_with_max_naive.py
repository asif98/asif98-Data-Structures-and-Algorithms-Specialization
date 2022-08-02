#python3
import sys
import heapq

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.maxValues = []
        self.max = float("-inf")

    def Push(self, val) :
        #heapq.heappush(self.maxHeap, (-a, len(self.stack)))
        self.stack.append(val)
        if val >= self.max :
            self.maxValues.append(val)
            self.max = val

    def Pop(self):
        assert(len(self.stack))
        val = self.stack.pop()
        if val == self.max :
            self.maxValues.pop()
            if self.maxValues :
                self.max = self.maxValues[-1]
            else :
                self.max = float("-inf")

    # def Max(self):
    #     assert(len(self.stack))
    #     while self.maxHeap :
    #         -a, idx = self.maxHeap[0]
    #         if self.stack[idx] == a :
    #             return a
    #         else :
    #             heapq.heappop(self.maxHeap)



if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.max)
        else:
            assert(0)
