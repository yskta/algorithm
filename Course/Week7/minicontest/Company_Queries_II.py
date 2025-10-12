import sys
from math import log2, ceil

def Company_Queries():
    input = sys.stdin.buffer.readline
    n, q = map(int, input().split())
    boss_list = list(map(int, input().split()))

    parent = [0] * (n + 1)
    parent[1] = 1
    for i in range(2, n + 1):
        parent[i] = boss_list[i - 2]

    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        depth[i] = depth[parent[i]] + 1

    MAX_DEPTH = ceil(log2(n)) + 1
    up = [[0] * (n + 1) for _ in range(MAX_DEPTH)]
    for v in range(1, n + 1):
        up[0][v] = parent[v]
    for k in range(1, MAX_DEPTH):
        prev = up[k - 1]
        curr = up[k]
        for v in range(1, n + 1):
            curr[v] = prev[prev[v]]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]
        k = 0
        while diff:
            if diff & 1:
                a = up[k][a]
            diff >>= 1
            k += 1

        if a == b:
            return a

        for k in range(MAX_DEPTH - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]

        return up[0][a]

    out = []
    for _ in range(q):
        a, b = map(int, input().split())
        out.append(str(lca(a, b)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    Company_Queries()