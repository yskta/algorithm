def sum_of_ones():
    n = int(input())
    binary = bin(n)[2:] # nを二進数文字列に変換（'0b'プレフィックスを除去）
    length = len(binary)
    result = 0
    
    for i in range(length):
        if binary[i] == '1':
            remaining = length - i - 1
            if remaining > 0:
                result += remaining * (2 ** (remaining - 1))
            if remaining > 0:
                result += int(binary[i+1:], 2) + 1
            else:
                result += 1 
    print(result)

if __name__ == "__main__":
    sum_of_ones()