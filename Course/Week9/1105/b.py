def Ctrl_F():
    line = input().strip()
    a, b = line.split()

    positions = []
    start = 0

    while True:
        pos = b.find(a, start)
        if pos == -1:
            break
        positions.append(pos + 1)
        start = pos + 1

    print(len(positions))
    if positions:
        print(' '.join(map(str, positions)))
    else:
        print()

if __name__ == "__main__":
    Ctrl_F()