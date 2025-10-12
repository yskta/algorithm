from collections import defaultdict

def Download_Speed():
    n, m = map(int, input().split())

    graph = defaultdict(lambda: defaultdict(int))

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] += c

    def find_path(source, sink, visited, min_cap):
        if source == sink:
            return min_cap
        
        visited.add(source)
                
        for neighbor, capacity in list(graph[source].items()):
            if neighbor not in visited and capacity > 0:
                flow = find_path(neighbor, sink, visited, min(min_cap, capacity))
                
                if flow > 0:
                    graph[source][neighbor] -= flow
                    graph[neighbor][source] += flow
                    return flow
        
        return 0
    
    max_flow = 0
    while True:
        flow = find_path(1, n, set(), float('inf'))
        if flow == 0:
            break
        max_flow += flow
    
    print(max_flow)  
    

if __name__ == "__main__":
    Download_Speed()