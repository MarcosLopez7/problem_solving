t = int(input())

for test_case in range(t):
    line = input().split()
    p, q = int(line[0]), int(line[1])

    persons_location = []
    for _ in range(p):
        persons_location.append(input().split())
