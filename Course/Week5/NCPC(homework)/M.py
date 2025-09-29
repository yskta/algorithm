def add(x, y):
    if y == "0":
        return x
    elif y.startswith("S(") and y.endswith(")"):
        inner_y = y[2:-1]
        return "S(" + add(x, inner_y) + ")"

def multiply(x, y):
    if y == "0":
        return "0"
    elif y.startswith("S(") and y.endswith(")"):
        inner_y = y[2:-1]  # S(y) の y 部分
        return add(multiply(x, inner_y), x)

def methodic_multiplication():
    a = input()
    b = input()
    result = multiply(a, b)
    print(result)

if __name__ == "__main__":
    methodic_multiplication()