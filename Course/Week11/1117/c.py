from math import gcd
from functools import reduce

def rook_can_capture():
    n, y = map(int, input().split())
    steps = list(map(int, input().split()))
    
    overall_gcd = reduce(gcd, steps)
    
    if y % overall_gcd == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    rook_can_capture()