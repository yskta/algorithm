def building_teams():
    n, m = map(int, input().split())

    graph = {}
    for i in range (1, n + 1):
        graph[i] = []

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    teams = [0] * (n + 1)
    possible = True
    
    for start_pupil in range(1, n + 1):
        if teams[start_pupil] == 0:
            stack = [(start_pupil, 1)]
            
            while stack and possible:
                pupil, team = stack.pop()

                if teams[pupil] != 0:
                    if teams[pupil] != team:
                        possible = False
                        break
                    continue

                teams[pupil] = team
                if team == 1:
                    next_team = 2
                else:
                    next_team = 1

                for friend in graph[pupil]:
                    if teams[friend] == 0:
                        stack.append((friend, next_team))
                    elif teams[friend] == team:
                        possible = False
                        break

            if not possible:
                break
    
    if possible:
        print(" ".join(str(teams[i]) for i in range(1, n + 1)))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    building_teams()
