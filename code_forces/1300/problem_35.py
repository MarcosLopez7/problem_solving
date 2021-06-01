import math


def solve(areas):
    a = math.sqrt((areas[2] * areas[0]) / areas[1])
    b = areas[0] / a
    c = areas[2] / a

    result = a * 4 + b * 4 + c * 4
    return result


areas = [int(num) for num in input().split()]
result = solve(areas)
print(int(result))


