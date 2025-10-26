from collections import defaultdict, deque

def Snakeless_path():
    n, m = map(int, input().split())

    forbidden = set()

    for _ in range(m):
        a, b = map(int, input().split())
        forbidden.add((a, b))

    graph = defaultdict(list)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            edge = (i, j)
            if edge not in forbidden:
                graph[i].append(j)
                graph[j].append(i)


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

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return None
    path = find_path(1, n)
    if path is None:
        print(0)
    else:
        print(len(path))
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    Snakeless_path()