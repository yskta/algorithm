def connect_cities():
    n, m = map(int, input().split())

    graph = {}
    for i in range (1, n + 1):
        graph[i] = []

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
   
    visited = set()
    connected_cities_groups = []

    for city in range(1, n + 1):
        if city not in visited:
            connected_cities_group = []
            stack = [city]
            while stack:
                current_city = stack.pop()
                if current_city not in visited:
                    visited.add(current_city)
                    connected_cities_group.append(current_city)
                    for neighbor_city in graph.get(current_city, []):
                        if neighbor_city not in visited:
                            stack.append(neighbor_city)

            connected_cities_groups.append(connected_cities_group)
    
    k = len(connected_cities_groups) - 1
    print(k)

    for i in range(1, len(connected_cities_groups)):
        city1 = connected_cities_groups[i - 1][0]
        city2 = connected_cities_groups[i][0]
        print(city1, city2)


if __name__ == "__main__":
    connect_cities()
