def Sigma_Cubes():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            sum -= i ** 3
        else:
            sum += i ** 3
    print(sum)

if __name__ == "__main__":
    Sigma_Cubes()
