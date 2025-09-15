def dice_combinations():
    n = int(input())
    m = 10 ** 9 + 7
    count = [0] * (n + 1)
    count[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if (i - j >= 0):
                count[i] += count[i - j]
                count[i] %= m

    print(count[n])

if __name__ == "__main__":
    dice_combinations()