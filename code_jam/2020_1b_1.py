def jump(vx, vy, x, y, m):
    if x == vx and y == vy:
        return ""
    else:
        m = m * 2
        if x + m < vx:
            pass


def solve(x, y):

    if y % 2 == x % 2:
        return "IMPOSSIBLE"


t = int(input())

for test_case in range(t):
    line = input().split()
    x = int(line[0])
    y = int(line[0])

    result = solve(x, y)

    print("Case #{}: {}".format(test_case + 1, result))
