def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    if (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
        min(p[1], r[1]) <= q[1] <= max(p[1], r[1])):
        return True
    return False

def is_on_boundary(point, polygon):
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]        
        if orientation(p1, point, p2) == 0:
            if on_segment(p1, point, p2):
                return True
    return False

def is_inside_polygon(point, polygon):
    n = len(polygon)
    x, y = point
    inside = False
    
    p1x, p1y = polygon[0]
    
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        
        p1x, p1y = p2x, p2y
    
    return inside

def main():
    n, m = map(int, input().split())    
    polygon = []
    for _ in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    for _ in range(m):
        x, y = map(int, input().split())
        point = (x, y)
        if is_on_boundary(point, polygon):
            print("BOUNDARY")
        elif is_inside_polygon(point, polygon):
            print("INSIDE")
        else:
            print("OUTSIDE")

if __name__ == "__main__":
    main()