def Dice_Summation():
    n = int(input())
    MOD = 10**9 + 7

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for dice in range(1, 7):
            if i - dice >= 0:
                dp[i] = (dp[i] + dp[i - dice]) % MOD
    print(dp[n])

if __name__ == "__main__":
    Dice_Summation()
