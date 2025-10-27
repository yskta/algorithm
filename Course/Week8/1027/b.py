def Piva_and_Glasses():
    input_str = input()
    len_str = len(input_str)

    dict = {}
    count = 1
    for i in range(len_str):
        count *= (i + 1)
        if input_str[i] not in dict:
            dict[input_str[i]] = 1
        else:
            dict[input_str[i]] += 1

    for _, value in dict.items():
        if value != 1:
            for i in range(1, value+1):
                count //= i
    print(int(count))

if __name__ == "__main__":
    Piva_and_Glasses()