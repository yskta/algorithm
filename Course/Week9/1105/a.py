def Broken_backspace():
    s = input().strip()
    t = input().strip()
    t_idx = 0
    
    for char in s:
        if t_idx < len(t) and char == t[t_idx]:
            t_idx += 1
    
    if t_idx == len(t):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    Broken_backspace()