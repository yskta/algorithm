def Find_Permutation():
    n = int(input())
    A_list = list(map(int, input().split()))
    P_list = [0] * n
    used = set()
    rest = list(range(1, n + 1))

    for i in range(n):
        if A_list[i] != -1 and A_list[i] not in used:
            used.add(A_list[i])
            P_list[i] = A_list[i]
            rest.remove(A_list[i])
        elif A_list[i] == -1:
            continue
        else:
            print("No")
            return
    
    for i in range(n):
        if P_list[i] == 0:
            P_list[i] = rest[0]
            rest.remove(P_list[i])

    print("Yes")
    print(" ".join(str(P_list[i]) for i in range(n))) 

if __name__ == "__main__":
    Find_Permutation()
