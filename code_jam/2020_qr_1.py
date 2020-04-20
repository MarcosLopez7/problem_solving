def diagon_sum(matrix):
    result = 0

    for i in range(len(matrix)):
        result += matrix[i][i]

    return result

def r_coincidence(matrix):
    result = 0

    for i in range(len(matrix)):
        set_list = list(set(matrix[i]))
        if len(set_list) != len(matrix):
            result = result + 1

    return result

def c_coincidence(matrix):
    result = 0
    n = len(matrix)

    for i in range(n):
        column = []
        for j in range(n):
            if matrix[j][i] in column:
                result = result + 1
                break

            column.append(matrix[j][i])

    return result


t = int(input())

for test_case in range(t):
    n = int(input())

    matrix = []

    for row in range(n):
        matrix.append([i for i in list(map(int, input().split()))])

    k = diagon_sum(matrix)
    r = r_coincidence(matrix)
    c = c_coincidence(matrix)

    print("Case #{}: {} {} {}".format(test_case + 1, k, r, c))



