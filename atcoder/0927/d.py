H, W = map(int, input().split())
S = [list(input()) for i in range(H)]


dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def in_grid(x, y):
    return 0 <= x < H and 0 <= y < W


def count(x, y):
    c = 0
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny) and S[nx][ny] == "#":
            c += 1
    return c


for i in range(H * W):
    # 初回は全マス操作
    if i == 0:
        T = []
        for x in range(H):
            for y in range(W):
                if S[x][y] == "." and count(x, y) == 1:
                    T.append((x, y))
    else:
        nT = []
        for x, y in T:
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny) and S[nx][ny] == "." and count(nx, ny) == 1:
                    nT.append((nx, ny))
        T = nT

    if len(T) == 0:
        break
    for x, y in T:
        S[x][y] = "#"


ans = 0
for x in range(H):
    for y in range(W):
        ans += int(S[x][y] == "#")

print(ans)