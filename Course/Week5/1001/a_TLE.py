def Sledding():
    n = int(input())
    heights = list(map(int, input().split()))
 
    max_diff = 0
    L, R = 1, 2
    for i in range(n):
        j = i
        while j + 1 < n and heights[j] < heights[j+1]:
            j += 1
        if j > i:
            diff = heights[j] - heights[i]
            if diff > max_diff:
                max_diff = diff
                L, R = i + 1, j + 1
        j = i
        while j + 1 < n and heights[j] > heights[j+1]:
            j += 1
        if j > i:
            diff = heights[i] - heights[j]
            if diff > max_diff:
                max_diff = diff
                L, R = i + 1, j + 1
    print(L, R)
 
if __name__ == "__main__":
    Sledding()