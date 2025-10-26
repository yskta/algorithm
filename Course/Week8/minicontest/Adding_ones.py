import sys

def Adding_ones():
    input = sys.stdin.readline
    n = int(input())

    result = []
    for _ in range(n):
        input_num = int(input())
        result.append(str(input_num + 1))
    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == "__main__":
    Adding_ones()