from collections import defaultdict, deque

def airport():
    n, m = map(int, input().split())

    checkpoint_capacity = list(map(int, input().split()))
    
    graph = defaultdict(lambda: defaultdict(int))
    
    for i in range(n):
        if checkpoint_capacity[i] == -1:
            graph[2*i+1][2*i+2] = float('inf')
        else:
            graph[2*i+1][2*i+2] = checkpoint_capacity[i]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[2*a][2*b-1] = float('inf')
    
    # BFS to find augmenting path
    def bfs(source, sink, parent):
        visited = set([source])
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    
                    if v == sink:
                        return True
        return False
    
    max_flow = 0
    source = 1
    sink = 2*n

    while True:
        parent = {}
        if not bfs(source, sink, parent):
            break        
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    
    print(max_flow)  
    

    

if __name__ == "__main__":
    airport()