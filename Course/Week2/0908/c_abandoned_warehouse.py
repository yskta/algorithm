from collections import deque

def abandoned_warehouse():
    n, m = map(int, input().split())
    grid = []
    start = None
    end = None
    
    for i in range(n):
        row = input().strip()
        grid.append(row)
        for j in range(m):
            if row[j] == 'A':
                start = (j, i)
            elif row[j] == 'B':
                end = (j, i)

    directions = [(0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R')]
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            # Reconstruct path
            path = []
            curr = end
            while parent[curr] is not None:
                px, py = parent[curr]
                for dx, dy, direction in directions:
                    if px + dx == curr[0] and py + dy == curr[1]:
                        path.append(direction)
                        break
                curr = parent[curr]
            path.reverse()
            print(f"YES\n{len(path)}\n{''.join(path)}")
            return

        for dx, dy, direction in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in parent and grid[new_y][new_x] != '#':
                parent[(new_x, new_y)] = (x, y)
                queue.append((new_x, new_y))
    print("NO")
    return

if __name__ == "__main__":
    abandoned_warehouse()
