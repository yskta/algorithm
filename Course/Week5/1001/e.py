def train_schedule():
    n = int(input())
    train_schedule_list = list(map(int, input().split()))
    output = [0] * n

    for i in range(n):
        j = i
        res = (n - 1 - i) // train_schedule_list[i]
        k = i + train_schedule_list[i] * res
        while j < k:
            output[j] += 1
            output[k] += 1
            j += train_schedule_list[i]
            k -= train_schedule_list[i]
            if j == k:
              output[j] -= 1
    print(" ".join(str(output[i]) for i in range(n))) 


if __name__ == "__main__":
    train_schedule()