import math

def bus_tours():
    n, q = map(int, input().split())

    for i in range(q):
        a, b = map(int, input().split())
        stops = n // math.gcd(n, a)
        print(stops)
    return 0

if __name__ == "__main__":
    bus_tours()