def solve_array_discord():
    n = int(input())
    numbers = list(map(int, input().split()))
    
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    for i in range(n):
        original_num = numbers[i]
        num_str = str(original_num)
        for pos in range(len(num_str)):
            original_digit = num_str[pos]
            for new_digit in '0123456789':
                if new_digit == original_digit:
                    continue
                new_str = num_str[:pos] + new_digit + num_str[pos + 1:]
                if len(new_str) > 1 and new_str[0] == '0':
                    continue     
                new_num = int(new_str)
                test_array = numbers.copy()
                test_array[i] = new_num
                if not is_sorted(test_array):
                    print(*test_array)
                    return
    print("impossible")

if __name__ == "__main__":
    solve_array_discord()