def appartments():
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    result = 0
    idx = 0

    for desired_size in a:
        while idx < m:
            b_size = b[idx]
            if ((desired_size - k) <= b_size) and (b_size <= (desired_size + k)):
                result += 1
                idx += 1
                break
            elif b_size < (desired_size - k):
                idx += 1
            else:
                break

    print(result)

if __name__ == "__main__":
    appartments()
