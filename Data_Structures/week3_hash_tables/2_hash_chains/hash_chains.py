# python3
class ListNode :
    def __init__(self, val = None) :
        self.val = val
        self.next = None

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [ListNode() for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            node = self.elems[query.ind].next
            chain = []
            while node :
                chain.append(node.val)
                node = node.next
            self.write_chain(chain)

            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
        else:

            ind = self._hash_func(query.s)
            root = self.elems[ind]
            prev = root
            node = root.next
            while node :
                if node.val == query.s :
                    break
                prev, node = node, node.next

            if query.type == 'find':
                if node :
                    self.write_search_result(True)
                else :
                    self.write_search_result(False)
            elif query.type == 'add':
                if not node :
                    temp = root.next
                    root.next = ListNode(query.s)
                    root.next.next = temp
            else:
                if node :
                    prev.next = node.next
                    del node

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

# qp = QueryProcessor(5)
# qp.process_query(Query(["add", "world"]))
# qp.process_query(Query(["add", "HellO"]))
# qp.process_query(Query(["check", 4]))
# qp.process_query(Query(["find", "world"]))
# qp.process_query(Query(["find", "World"]))
# qp.process_query(Query(["del", "world"]))
# qp.process_query(Query(["check", 4]))


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
