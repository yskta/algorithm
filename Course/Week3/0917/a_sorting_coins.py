def sorting_coins():
    n, m = map(int, input().split())
    coin_radius_list = list(map(int, input().split()))
    hole_radius_list = list(map(int, input().split()))
    max_hole_radius = max(hole_radius_list)
 
    answer = [0] * n
 
    for i in range (n):
        if coin_radius_list[i] > max_hole_radius:
            answer[i] = m + 1
        for j in range(m):
            if coin_radius_list[i] <= hole_radius_list[j]:
                answer[i] = j + 1
                break
 
    print(" ".join(str(answer[i]) for i in range(n)))
 
if __name__ == "__main__":
    sorting_coins()
