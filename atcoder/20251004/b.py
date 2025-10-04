def b():
    S = input()
    dict = {}
    for s in S:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    for key, value in dict.items():
        if value == 1:
            print(key)
            return

if __name__ == "__main__":
    b()