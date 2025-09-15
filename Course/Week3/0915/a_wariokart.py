def wario_kart():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list_meter = set(i * 100 for i in a_list)
    circle = n * 100

    dp = [0] * (k + 1)    
    for second in range(1, k + 1):
        prev_pos = dp[second - 1] % circle
        if prev_pos in a_list_meter:
            dp[second] = dp[second - 1] + 200
        else:
            dp[second] = dp[second - 1] + 100  
    print(dp[k] % circle)

if __name__ == "__main__":
    wario_kart()