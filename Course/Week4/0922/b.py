def forest_density():
    n, q = map(int, input().split())
    
    trees_sum = []

    for i in range(n):
        arr = list(input())
        trees_sum.append([0] * n)
        count = 0
        for j in range (n):
            if arr[j] == "*":
                count += 1
            if i == 0:
                trees_sum[i][j] = count
            else:
                trees_sum[i][j] = count + trees_sum[i - 1][j]
    # print(trees_sum)
    for _ in range(q):
        y1, x1, y2, x2 = map(int, input().split())
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        if y1 == 0 and x1 == 0:
            print(trees_sum[y2][x2])
        elif y1 == 0:
            print(trees_sum[y2][x2] - trees_sum[y2][x1 - 1])
        elif x1 == 0:
            print(trees_sum[y2][x2] - trees_sum[y1 - 1][x2])
        else:
            print(trees_sum[y2][x2] - trees_sum[y2][x1 - 1] - trees_sum[y1 - 1][x2] + trees_sum[y1 - 1][x1 - 1])

if __name__ == "__main__":
    forest_density()