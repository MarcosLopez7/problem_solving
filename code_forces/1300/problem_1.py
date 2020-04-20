def solve(matrix):

    for i in range(3):
        total_column = 0
        for j in range(len(matrix)):
            total_column = total_column + matrix[j][i]
        if total_column != 0:
            return "NO"

    return "YES"


n = int(input())
matrix = []


for _ in range(n):
    matrix.append([number for number in list(map(int, input().split()))])

print(solve(matrix))
