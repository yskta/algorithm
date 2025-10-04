def Sledding():
    n = int(input())
    heights = list(map(int, input().split()))

    max_diff = 0
    L, R = 1, 2
    
    start = 0
    is_increasing = None

    for i in range(1, n):
        if heights[i] > heights[i-1]:
            if is_increasing == False:
                start = i - 1
            is_increasing = True
            diff = heights[i] - heights[start]
            if diff > max_diff:
                max_diff = diff
                L, R = start + 1, i + 1

        else:
            if is_increasing == True:
                start = i - 1
            is_increasing = False
            diff = heights[start] - heights[i]
            if diff > max_diff:
                max_diff = diff
                L, R = start + 1, i + 1  

    print(L, R)

if __name__ == "__main__":
    Sledding()