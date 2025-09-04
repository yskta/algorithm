# 競技プログラミング サンプルコード集

# ========== 1. A+B問題 (基本の入出力) ==========
def a_plus_b():
    """
    入力: A B (スペース区切り)
    出力: A+Bの値
    """
    A, B = map(int, input().split())
    print(A + B)

# ========== 2. 配列の最大値を求める ==========
def find_max():
    """
    入力: 
    N (配列の要素数)
    A1 A2 ... AN (配列の要素)
    出力: 配列の最大値
    """
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A))

# ========== 3. 文字列の回文判定 ==========
def is_palindrome():
    """
    入力: 文字列S
    出力: 回文ならYes、そうでなければNo
    """
    S = input().strip()
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")

# ========== 4. FizzBuzz ==========
def fizzbuzz():
    """
    入力: N
    出力: 1からNまでFizzBuzz
    """
    N = int(input())
    for i in range(1, N + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# ========== 5. 素数判定 ==========
def is_prime():
    """
    入力: N
    出力: 素数ならYes、そうでなければNo
    """
    N = int(input())
    
    if N < 2:
        print("No")
        return
    
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print("No")
            return
    
    print("Yes")

# ========== 6. 組み合わせ (nCr) ==========
def combination():
    """
    入力: n r
    出力: nCr の値
    """
    import math
    n, r = map(int, input().split())
    
    if r > n or r < 0:
        print(0)
    else:
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        print(result)

# ========== 7. 最大公約数 (GCD) ==========
def gcd_sample():
    """
    入力: A B
    出力: AとBの最大公約数
    """
    import math
    A, B = map(int, input().split())
    print(math.gcd(A, B))

# ========== 8. 二分探索 ==========
def binary_search():
    """
    入力:
    N (配列の要素数)
    A1 A2 ... AN (ソート済み配列)
    X (探す値)
    出力: Xが配列にあればYes、なければNo
    """
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    
    left, right = 0, N - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == X:
            found = True
            break
        elif A[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    
    print("Yes" if found else "No")

# ========== 9. DFS (深さ優先探索) - グラフ探索 ==========
def dfs_sample():
    """
    入力:
    N M (頂点数、辺数)
    以下M行: u v (辺の情報)
    出力: 頂点1から到達可能な頂点数
    """
    def dfs(v, visited, graph):
        visited[v] = True
        count = 1
        for next_v in graph[v]:
            if not visited[next_v]:
                count += dfs(next_v, visited, graph)
        return count
    
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (N + 1)
    result = dfs(1, visited, graph)
    print(result)

# ========== 10. 動的計画法 (DP) - ナップサック問題 ==========
def knapsack():
    """
    入力:
    N W (アイテム数、ナップサックの容量)
    以下N行: w v (重さ、価値)
    出力: 最大価値
    """
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        w, v = map(int, input().split())
        items.append((w, v))
    
    # dp[i][w] = i番目までのアイテムで重さwの時の最大価値
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        w, v = items[i - 1]
        for j in range(W + 1):
            # アイテムiを取らない場合
            dp[i][j] = dp[i - 1][j]
            # アイテムiを取る場合
            if j >= w:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
    
    print(dp[N][W])

# ========== クラス定義 ==========

class UnionFind:
    """Union-Find (素集合) データ構造"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # ランクによる結合
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.rank[root_x] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        return self.size[self.find(x)]


class SegmentTree:
    """セグメント木 (Range Minimum Query)"""
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (2 * self.n)
        
        # 葉ノードを初期化
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        
        # 内部ノードを構築
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, pos, value):
        """位置posの値をvalueに更新"""
        pos += self.n
        self.tree[pos] = value
        
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])
    
    def query(self, left, right):
        """区間[left, right)の最小値を取得"""
        left += self.n
        right += self.n
        result = float('inf')
        
        while left < right:
            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                result = min(result, self.tree[right])
            left //= 2
            right //= 2
        
        return result


class BIT:
    """Binary Indexed Tree (Fenwick Tree)"""
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        """位置iにdeltaを加算"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        """位置1からiまでの累積和を取得"""
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result
    
    def range_query(self, left, right):
        """区間[left, right]の和を取得"""
        return self.query(right) - self.query(left - 1)


class Point:
    """2D座標点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        """他の点との距離を計算"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y


class Graph:
    """グラフクラス (隣接リスト表現)"""
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, weight=1):
        """辺を追加"""
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))
    
    def dfs(self, start, visited=None):
        """深さ優先探索"""
        if visited is None:
            visited = [False] * self.n
        
        visited[start] = True
        result = [start]
        
        for neighbor, _ in self.adj[start]:
            if not visited[neighbor]:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def bfs(self, start):
        """幅優先探索"""
        from collections import deque
        
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dijkstra(self, start):
        """ダイクストラ法で最短距離を計算"""
        import heapq
        
        dist = [float('inf')] * self.n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > dist[u]:
                continue
            
            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist


class ModInt:
    """モジュラ演算クラス"""
    MOD = 1000000007
    
    def __init__(self, value):
        self.value = value % self.MOD
    
    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value + other.value)
        return ModInt(self.value + other)
    
    def __sub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value - other.value)
        return ModInt(self.value - other)
    
    def __mul__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value * other.value)
        return ModInt(self.value * other)
    
    def __pow__(self, exp):
        return ModInt(pow(self.value, exp, self.MOD))
    
    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value


# ========== クラスを使った問題例 ==========

def union_find_example():
    """Union-Findを使った連結成分の問題"""
    N, M = map(int, input().split())
    uf = UnionFind(N)
    
    for _ in range(M):
        u, v = map(int, input().split())
        uf.union(u - 1, v - 1)  # 0-indexedに変換
    
    # 連結成分の数を数える
    components = set()
    for i in range(N):
        components.add(uf.find(i))
    
    print(len(components))


def segment_tree_example():
    """セグメント木を使ったRange Minimum Query"""
    N = int(input())
    A = list(map(int, input().split()))
    
    seg_tree = SegmentTree(A)
    
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:  # 更新
            i, x = query[1] - 1, query[2]  # 0-indexedに変換
            seg_tree.update(i, x)
        else:  # 範囲最小値クエリ
            l, r = query[1] - 1, query[2]  # 0-indexedに変換
            print(seg_tree.query(l, r))


def dijkstra_example():
    """ダイクストラ法を使った最短経路問題"""
    N, M = map(int, input().split())
    graph = Graph(N, directed=True)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph.add_edge(u - 1, v - 1, w)  # 0-indexedに変換
    
    distances = graph.dijkstra(0)  # 頂点0から各頂点への最短距離
    
    for i in range(N):
        if distances[i] == float('inf'):
            print("INF")
        else:
            print(distances[i])


def modint_example():
    """ModIntを使った組み合わせ計算"""
    n, k = map(int, input().split())
    
    # nCk を計算
    numerator = ModInt(1)
    denominator = ModInt(1)
    
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    
    # フェルマーの小定理を使った逆元計算
    result = numerator * (denominator ** (ModInt.MOD - 2))
    print(result)


# ========== メイン実行部分 ==========
if __name__ == "__main__":
    # 実行したい問題の関数を呼び出してください
    # 例: a_plus_b()
    
    print("競プロサンプルコード集 (関数 + クラス)")
    print("実行したい関数のコメントアウトを外してください")
    
    # 基本問題
    # a_plus_b()
    # find_max()
    # is_palindrome()
    # fizzbuzz()
    # is_prime()
    # combination()
    # gcd_sample()
    # binary_search()
    # dfs_sample()
    # knapsack()
    
    # クラスを使った問題
    # union_find_example()
    # segment_tree_example()
    # dijkstra_example()
    # modint_example()