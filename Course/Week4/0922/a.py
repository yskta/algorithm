def xor_sum():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
    
    for _ in range(q):
        a, b = map(int, input().split())
        result = prefix_xor[b] ^ prefix_xor[a - 1]
        print(result)

if __name__ == "__main__":
    xor_sum()