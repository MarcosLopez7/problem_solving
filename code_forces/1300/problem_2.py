def get_steps(x, y):
    return abs(x - 2) + abs(y - 2)


def solve(matrix):

    x = y = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                x = i
                y = j
                return get_steps(x, y)


matrix = []


for _ in range(5):
    matrix.append([number for number in list(map(int, input().split()))])

print(solve(matrix))
