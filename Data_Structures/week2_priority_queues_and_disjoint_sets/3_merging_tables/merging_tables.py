# python3

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        #self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            # print(src_parent, dst_parent)
            # print(self.max_row_count)
            # print(self.row_counts)
            # print(self.parents)

            return False

        self.row_counts[dst_parent] += self.row_counts[src_parent]
        self.row_counts[src_parent] = 0
        self.parents[src_parent] = dst_parent
        self.max_row_count = max( self.max_row_count, self.row_counts[dst_parent])

        return True

    def get_parent(self, table):
        if self.parents[table] == table :
            return table
        else :
            return self.get_parent(self.parents[table])

# row_counts = [1,1,1,1,1]
# db = Database(row_counts)
# db.merge(2,4)
# db.merge(1,3)
# db.merge(0,3)
# db.merge(4,3)
# db.merge(4,2)

# row_counts = [10, 0, 5, 0, 3, 3]
# db = Database(row_counts)
# db.merge(5,5)
# db.merge(5,4)
# db.merge(4,3)
# db.merge(3,2)
# db.merge(4,2)

def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
