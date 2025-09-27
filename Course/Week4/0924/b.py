def find_circle(start, p_list, n):
    visited = set()
    current = start
    steps = 0
    
    path = []
    while current not in visited:
        visited.add(current)
        path.append(current)
        current = p_list[current]
        steps += 1
        if steps > n:
            return -1, -1

    cycle_start = current
    distance_to_cycle = path.index(cycle_start)
    
    circle_length = len(path) - distance_to_cycle
    
    return distance_to_cycle, circle_length, path

def bathhouse():
    n, q = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list.insert(0, 0)
    distance_to_cycle, circle_length, path = find_circle(1, p_list, n)

    circle_exist = False

    if distance_to_cycle != -1 and circle_length != -1:
        circle_exist = True

    second_list = list(map(int, input().split()))
    output = []
    for second in second_list:
        if circle_exist:
            if second == 0:
                output.append(1)
            else:
                result = (second - distance_to_cycle) % circle_length
                output.append(path[distance_to_cycle] + result)
        else:
            if second > len(path):
                output.append(path[-1])
            else:
                output.append(path[second])
    print(" ".join(str(x) for x in output))

if __name__ == '__main__':
    bathhouse()