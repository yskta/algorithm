def a():
    X, Y = map(str, input().split())
    dict = {"Ocelot": 0, "Serval": 1, "Lynx": 2}
    if dict[X] >= dict[Y]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    a()