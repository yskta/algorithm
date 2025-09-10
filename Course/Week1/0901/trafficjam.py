def backpacking():
    n = int(input())
    list = []
    for i in range(n):
        A, B = input().split()
        A = int(A)
        B = int(B)
        list.append([A, B])
    print(list)
    list.sort()
    print(list)
    # 重なっている区間を抽出する
    dup_interval = []
    for i in range(n):
        if i == 0:
            continue
        start = list[i][0]
        end = list[i][1]
        for j in range(i):
            compare_start = list[j][0]
            compare_end = list[j][1]
            if compare_end >= end:
                dup_interval.append[start, end]

    # max_traffix = 0

    return n

if __name__ == "__main__":
    backpacking()