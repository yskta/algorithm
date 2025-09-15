def astralis_session():
    n = int(input())
    
    # nが奇数なら不可能
    if n % 2 == 1:
        print("No")
        return
    
    # グラフの構築
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    edges = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges.append((a, b))
    
    # 各エッジを削除したときの成分のサイズを調べる
    for u, v in edges:
        # エッジ(u, v)を一時的に削除
        graph[u].remove(v)
        graph[v].remove(u)
        
        # uから到達可能なノード数を数える（DFS）
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(u)
        count = len(visited)
        
        # エッジを戻す
        graph[u].append(v)
        graph[v].append(u)
        
        # 片方の成分がn/2なら、もう片方もn/2
        if count == n // 2:
            # 解を構築
            result = [''] * (n + 1)
            
            # エッジを削除して色付け
            graph[u].remove(v)
            graph[v].remove(u)
            
            # uから到達可能なノードを'U'に
            visited = set()
            def color_dfs(node, color):
                visited.add(node)
                result[node] = color
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        color_dfs(neighbor, color)
            
            color_dfs(u, 'U')
            color_dfs(v, 'M')
            
            print("Yes")
            print(''.join(result[1:]))
            return
    
    # 分割不可能（実際にはn偶数の木では必ず可能）
    print("No")


if __name__ == "__main__":
    astralis_session()
