def polygon_area():
    n = int(input())
    vertices = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    
    area_2x = 0
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area_2x += x1 * y2 - x2 * y1
    
    print(abs(area_2x))

if __name__ == "__main__":
    polygon_area()