from collections import deque

def counter():
    x = int(input())
    if x == 0:
        print(0)
        return
    # BFS
    queue = deque([(0, 0)]) #(現在値, 移動回数)
    visited = {0}

    while queue:
        current, moves = queue.popleft()

        next_val = current + 11
        if next_val == x:
            print(moves + 1)
            return
        if next_val <= x and next_val not in visited:
            visited.add(next_val)
            queue.append((next_val, moves + 1))
        
        next_val = current - 2
        if next_val == x:
            print(moves + 1)
            return
        if next_val >= 0 and next_val not in visited:
            visited.add(next_val)
            queue.append((next_val, moves + 1))
    
    print(-1)

if __name__ == "__main__":
    counter()
