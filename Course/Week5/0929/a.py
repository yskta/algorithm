def deeleting_digits():
    n = int(input())
    count = 0
    i = n
    while i != 0:
        max_num = 0
        num_str = str(i)
        for j in range(len(num_str)):
            cur = int(num_str[j])
            if cur > max_num:
                max_num = cur
        i -= max_num
        count += 1
    print(count)

if __name__ == "__main__":
    deeleting_digits()