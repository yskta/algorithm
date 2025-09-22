import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [float('inf')] * (2 * self.size)
        
        # Build tree
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, pos, val):
        pos += self.size
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])
    
    def query(self, l, r):
        l += self.size
        r += self.size
        res = float('inf')
        while l <= r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

def dynamic_range_minimum_queries():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    seg_tree = SegmentTree(arr)

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            k, u = query[1] - 1, query[2]
            seg_tree.update(k, u)
        else:
            a, b = query[1] - 1, query[2] - 1
            print(seg_tree.query(a, b))

if __name__ == "__main__":
    dynamic_range_minimum_queries()