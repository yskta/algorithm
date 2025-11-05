def compute_z_array():
    s = input().strip()
    n = len(s)
    z = [0] * n
    z[0] = n
    
    # l and r define the interval [l, r] which is the rightmost segment
    # that matches a prefix of s
    l, r = 0, 0
    
    for i in range(1, n):
        # Case 1: i > r, we compute z[i] from scratch
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # Case 2: i <= r, we can use previously computed values
            k = i - l
            
            # If z[k] is less than the remaining interval
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                # We need to check beyond r
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    print(' '.join(map(str, z)))    
    
if __name__ == "__main__":
    compute_z_array()