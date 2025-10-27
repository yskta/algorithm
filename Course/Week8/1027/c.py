def optimal_sort():
    n = int(input())
    a = map(int, input().split())


    sorted_with_index = sorted(enumerate(a), key=lambda x: x[1])
    pos = [0] * n
    for new_pos, (old_pos, _) in enumerate(sorted_with_index):
        pos[old_pos] = new_pos

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or pos[i] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = pos[j]
            cycle_size += 1

        swaps += cycle_size - 1

    print(swaps)

if __name__ == "__main__":
    optimal_sort()