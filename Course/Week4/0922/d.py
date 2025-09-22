def targeted_advertising():
    n, k, q = map(int, input().split())
    a_list = list(map(int, input().split()))

    intrested_sum = []
    # i: things_number
    # j: age_number
    for i in range(1, k + 1):
        intrested_sum.append([0] * n)
        for j in range(n):
            if j == 0: 
                if a_list[j] == i:
                    intrested_sum[i - 1][j] += 1
                else:
                    continue 
            elif a_list[j] == i:
                intrested_sum[i - 1][j] = 1 + intrested_sum[i - 1][j - 1]
            else:
                intrested_sum[i - 1][j] = intrested_sum[i - 1][j - 1]
    # print(intrested_sum)

    for _ in range(q):
        l, r, x = map(int, input().split())
        l -= 1
        r -= 1
        x -= 1
        if l == 0:
            print(intrested_sum[x][r])
        else:
            print(intrested_sum[x][r] - intrested_sum[x][l - 1])


if __name__ == "__main__":
    targeted_advertising()