def pair_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    
    swaps = []
    
    for i in range(0, 2*n, 2):
        if arr[i] == arr[i+1]:
            continue
        
        for j in range(i+2, 2*n):
            if arr[j] == arr[i]:
                arr[i+1], arr[j] = arr[j], arr[i+1]
                swaps.append((i+2, j+1))
                break
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    pair_sort()