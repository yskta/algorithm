from collections import defaultdict, deque

def Distinct_Routes():
    n, m = map(int, input().split())

    graph = defaultdict(lambda: defaultdict(int))

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] += 1

    def find_path(source, sink):
        visited = {source}
        queue = deque([source])
        parent = {source: None}
        
        while queue:
            node = queue.popleft()
            if node == sink:
                path = []
                current = sink
                while parent[current] is not None:
                    path.append(current)
                    current = parent[current]
                path.append(source)
                path.reverse()
                return path
            for neighbor, capacity in graph[node].items():
                if neighbor not in visited and capacity > 0:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        return None
    
    paths = []
    while True:
        path = find_path(1, n)
        if path is None:
            break
        paths.append(path)
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= 1
            graph[v][u] += 1
    
    print(len(paths))
    for path in paths:
        print(len(path))
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    Distinct_Routes()