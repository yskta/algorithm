def Illuminati():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))
    
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (graph[i][j] == 1 and 
                    graph[j][k] == 1 and 
                    graph[k][i] == 1):
                    count += 1
    
    print(count)

if __name__ == "__main__":
    Illuminati()