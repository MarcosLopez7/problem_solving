import sys

t = int(input())

for test_case in range(t):
    a = int(input())

    print(f"{10} {10}")
    while True:
        line = input().split()
        x, y = int(line[0]), int(line[1])

        if x == 0:
            break
        if x == -1:
            print("Error", file=sys.stderr)
            exit(-1)

        print(f"{x} {y}")
