from collections import defaultdict

def count_subarrays_with_sum():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    prefix_sum = 0
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1

    for num in a:
        prefix_sum += num
        count += prefix_sum_count[prefix_sum - x]
        prefix_sum_count[prefix_sum] += 1

    print(count)

if __name__ == "__main__":
    count_subarrays_with_sum()