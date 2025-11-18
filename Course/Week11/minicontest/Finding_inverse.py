def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    a = a % m
    g, x, _ = gcd_extended(a, m)
    if g != 1:
        return -1
    else:
        return (x % m + m) % m

def finding_inverse():
    a, m = map(int, input().split())

    result = mod_inverse(a, m)
    print(result)

if __name__ == "__main__":
    finding_inverse()