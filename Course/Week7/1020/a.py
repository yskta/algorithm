def Three_SUM():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    arr = [(a[i], i + 1) for i in range(n)]
    arr.sort()

    found = False
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i][0] + arr[left][0] + arr[right][0]

            if current_sum == x:
                positions = [arr[i][1], arr[left][1], arr[right][1]]
                print(*positions)
                found = True
                break
            elif current_sum < x:
                left += 1
            else:
                right -= 1
        if found:
            break
    if not found:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    Three_SUM()