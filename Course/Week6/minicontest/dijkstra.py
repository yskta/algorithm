import heapq

def dijkstra():
    n, m = map(int, input().split())
    
    # グラフを隣接リストで表現
    graph = [[] for _ in range(n + 1)]
    
    # 辺の入力
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    # 距離配列（初期値は無限大）
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0  # 始点（Syrjälä）の距離は0
    
    # 優先度付きキュー（距離, 頂点番号）
    pq = [(0, 1)]
    
    # ダイクストラ法
    while pq:
        d, u = heapq.heappop(pq)
        
        # すでに最短距離が確定している場合はスキップ
        if d > dist[u]:
            continue
        
        # 隣接頂点を探索
        for v, cost in graph[u]:
            # より短い経路が見つかった場合
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))
    
    # 結果出力
    print(' '.join(map(str, dist[1:n+1])))

if __name__ == "__main__":
    dijkstra()