class Segment_Tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr[:]
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, l, r)
        right_sum = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum
    
    def range_sum(self, l, r):
        return self.query(1, 0, self.n - 1, l, r)


def Rotate_and_Sum_Query():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    seg_tree = Segment_Tree(a_list)
    rotation = 0
    
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            c = query[1]
            rotation = (rotation + c) % n            
        else:
            l, r = query[1] - 1, query[2] - 1    
            actual_l = (l + rotation) % n
            actual_r = (r + rotation) % n            
            if actual_l <= actual_r:
                result = seg_tree.range_sum(actual_l, actual_r)
            else:
                result = seg_tree.range_sum(actual_l, n - 1) + seg_tree.range_sum(0, actual_r)
            print(result)

if __name__ == "__main__":
    Rotate_and_Sum_Query()
