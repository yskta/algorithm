from collections import deque

def topological_sort():
    n, m = map(int, input().split())
    
    # グラフと入次数を管理
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    # 辺の入力
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    # Kahn's algorithm
    # 入次数が0の頂点をキューに追加
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # トポロジカル順序を格納
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # uから出る辺を削除
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    # 全ての頂点を処理できたか確認
    if len(result) == n:
        print(' '.join(map(str, result)))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    topological_sort()