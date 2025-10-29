from math import gcd

def judge(segments, initial_speed):
    speed_num = initial_speed
    speed_den = 1
    happy_count = 0
    for p, r, a, f in segments:
        if speed_num < r * speed_den:
            return False, 0
        if speed_num >= p * speed_den:
            happy_count += 1
        speed_num = speed_num * (100 - f) - a * speed_den * 100
        speed_den = speed_den * 100
        
        g = gcd(abs(speed_num), speed_den)
        speed_num //= g
        speed_den //= g


    return True, happy_count

def Roller_coaster():
    n = int(input())
    segments = []
    for _ in range(n):
        p, r, a, f = map(int, input().split())
        segments.append((p, r, a, f))
    left, right = 0, 10**26
    while left < right:
        mid = (left + right) // 2
        can_complete, happy_count = judge(segments, mid)

        if can_complete and happy_count >= (n + 1) // 2:
            right = mid
        else:
            left = mid + 1
    print(left)

if __name__ == "__main__":
    Roller_coaster()