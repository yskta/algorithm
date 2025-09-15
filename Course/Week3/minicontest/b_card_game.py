def card_game():
    n = int(input())
    cards = list(map(int, input().split()))
    
    if n < 3:
        print(0)
        return
    
    dp = [0] * (n + 1)
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1]
        if i >= 3:
            dp[i] = max(dp[i], dp[i - 3] + cards[i - 2])
    
    print(dp[n])

if __name__ == "__main__":
    card_game()