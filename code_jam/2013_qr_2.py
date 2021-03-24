test_case = int(input())

for t in range(test_case):
    line = input().split(" ")
    n = int(line[0])
    m = int(line[1])

    pattern = []
    lawn = []

    for _ in range(n):
        row_pattern = [int(n) for n in input().split(" ")]
        row_lawn = [100 for _ in range(m)]
        pattern.append(row_pattern)
        lawn.append(row_lawn)

    y = "YES"

    for i in range(n):
        for j in range(m):
            pass



    print(f"Case #{t + 1}: {y}")