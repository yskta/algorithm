class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return min(p1, p2)

def dynamic_range_minimum_queries():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    seg_tree = SegmentTree(arr)

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            k, u = query[1] - 1, query[2]
            seg_tree.update(0, 0, n - 1, k, u)
        else:
            a, b = query[1] - 1, query[2] - 1
            print(seg_tree.query(0, 0, n - 1, a, b))

if __name__ == "__main__":
    dynamic_range_minimum_queries()