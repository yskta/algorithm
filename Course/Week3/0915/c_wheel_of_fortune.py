def solve():
    n = int(input())
    values = list(map(int, input().split()))
    
    if n == 3:
        # Special case: n=3, we must use all three colors
        # Try all 6 permutations and pick the best
        best = float('-inf')
        colors = [0, 1, 2]  # 0=black(+), 1=red(-), 2=green(0)
        
        # Check all valid colorings for n=3
        for c0 in range(3):
            for c1 in range(3):
                for c2 in range(3):
                    if c0 != c1 and c1 != c2 and c2 != c0:
                        score = 0
                        if c0 == 0:
                            score += values[0]
                        elif c0 == 1:
                            score -= values[0]
                        if c1 == 0:
                            score += values[1]
                        elif c1 == 1:
                            score -= values[1]
                        if c2 == 0:
                            score += values[2]
                        elif c2 == 1:
                            score -= values[2]
                        best = max(best, score)
        print(best)
    else:
        # For n >= 4, we can use just 2 colors optimally
        # Use dynamic programming with states (position, last_color)
        # dp[i][c] = max money from positions 0 to i-1 with position i-1 having color c
        
        INF = float('-inf')
        dp = [[INF] * 3 for _ in range(n + 1)]
        
        # Try all starting colors
        for start_color in range(3):
            # Reset dp for this starting color
            for i in range(n + 1):
                for j in range(3):
                    dp[i][j] = INF
            
            # Base case
            if start_color == 0:
                dp[1][0] = values[0]
            elif start_color == 1:
                dp[1][1] = -values[0]
            else:
                dp[1][2] = 0
            
            # Fill dp table
            for i in range(1, n):
                for prev_color in range(3):
                    if dp[i][prev_color] == INF:
                        continue
                    
                    for curr_color in range(3):
                        if curr_color != prev_color:
                            gain = 0
                            if curr_color == 0:
                                gain = values[i]
                            elif curr_color == 1:
                                gain = -values[i]
                            
                            dp[i + 1][curr_color] = max(dp[i + 1][curr_color], 
                                                       dp[i][prev_color] + gain)
        
        # Find the best answer considering the circular constraint
        best = INF
        for last_color in range(3):
            for first_color in range(3):
                if last_color != first_color and dp[n][last_color] != INF:
                    # Check if we started with first_color
                    test_val = 0
                    if first_color == 0:
                        test_val = values[0]
                    elif first_color == 1:
                        test_val = -values[0]
                    
                    # Only consider valid paths that started with first_color
                    if dp[1][first_color] == test_val:
                        best = max(best, dp[n][last_color])
        
        print(best)

if __name__ == "__main__":
    solve()