def LumberUolevi():
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        return
    elif n == k:
        trees = list(range(1, n + 1))
        print(*trees)
    else:       
        minimum_weight = k * (k + 1) // 2
        minimum_truck_needed = (minimum_weight + n - 1) // n
        total_weight_capacity = minimum_truck_needed * n
        trees = list(range(1, k + 1))
        current_total_weight = minimum_weight
        diff = total_weight_capacity - current_total_weight
        used = set(trees)
        i = k - 1
        while diff > 0 and i >= 0:
            for new_tree in range(min(n, trees[i] + diff), trees[i], -1):
                if (new_tree not in used) and (new_tree - trees[i] <= diff):
                        used.remove(trees[i])
                        used.add(new_tree)
                        diff -= (new_tree - trees[i])
                        trees[i] = new_tree
                        break
            i -= 1
        print(*sorted(trees))

if __name__ == "__main__":
    LumberUolevi()