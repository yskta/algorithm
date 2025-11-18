def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) - (B[1] - A[1]) * (C[0] - A[0])

def intersect(p1, p2, p3, p4):
    d1 = ccw(p3, p4, p1)
    d2 = ccw(p3, p4, p2)
    d3 = ccw(p1, p2, p3)
    d4 = ccw(p1, p2, p4)
    
    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    
    if d1 == 0 and on_segment(p3, p1, p4):
        return True
    if d2 == 0 and on_segment(p3, p2, p4):
        return True
    if d3 == 0 and on_segment(p1, p3, p2):
        return True
    if d4 == 0 and on_segment(p1, p4, p2):
        return True
    
    return False

def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def line_intersection():
    n = int(input())
    lines = []

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append(((x1, y1), (x2, y2)))

    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
                count += 1

    print(count)

if __name__ == "__main__":
    line_intersection()