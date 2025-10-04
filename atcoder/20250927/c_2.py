def Rotate_and_Sum_Query():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    
    double_a_list = a_list + a_list
    prefix_sum = [0] * (2 * n + 1)
    for i in range(2 * n):
        prefix_sum[i + 1] = prefix_sum[i] + double_a_list[i]

    rotation = 0
    
    for _ in range(q):
        query = list(map(int, input().split()))    
        if query[0] == 1:
            c = query[1]
            rotation = (rotation + c) % n
        else:
            l, r = query[1] - 1, query[2] - 1
            start = rotation + l
            end = rotation + r
            result = prefix_sum[end + 1] - prefix_sum[start]
            print(result)

if __name__ == "__main__":
    Rotate_and_Sum_Query()
