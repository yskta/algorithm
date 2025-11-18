def Exponentiation():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(pow(a, b, 10**9 + 7))
        
if __name__ == "__main__":
    Exponentiation()
    