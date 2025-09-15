def cow_heist():
    n = int(input())
    c_list = list(map(int, input().split()))

    max_number = max(c_list)

    beams = []
    for i in range(0, 30):
        append = 2 ** i
        if append <= max_number:
            beams.append(append)
        else:
            beams.append(0)
    print(' '.join(map(str, beams))) 

if __name__ == "__main__":
    cow_heist()
