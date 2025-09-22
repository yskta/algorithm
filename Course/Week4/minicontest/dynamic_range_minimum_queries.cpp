#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class SegmentTree {
private:
    int n;
    vector<long long> tree;
    
    void build(vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }
    
    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) {
                update(2 * node + 1, start, mid, idx, val);
            } else {
                update(2 * node + 2, mid + 1, end, idx, val);
            }
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }
    
    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return LLONG_MAX;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        long long p1 = query(2 * node + 1, start, mid, l, r);
        long long p2 = query(2 * node + 2, mid + 1, end, l, r);
        return min(p1, p2);
    }

public:
    SegmentTree(vector<long long>& arr) {
        n = arr.size();
        tree.assign(4 * n, LLONG_MAX);
        build(arr, 0, 0, n - 1);
    }
    
    void update(int idx, long long val) {
        update(0, 0, n - 1, idx, val);
    }
    
    long long query(int l, int r) {
        return query(0, 0, n - 1, l, r);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    cin >> n >> q;
    
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    SegmentTree seg_tree(arr);
    
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int k;
            long long u;
            cin >> k >> u;
            seg_tree.update(k - 1, u);
        } else {
            int a, b;
            cin >> a >> b;
            cout << seg_tree.query(a - 1, b - 1) << "\n";
        }
    }
    
    return 0;
}