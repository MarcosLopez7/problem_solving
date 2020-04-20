import re

def set_1(P):
    i = 0

    while i < (len(P) - 1):
        if P[i]['p'][1:] in P[len(P) - 1]['p'][1:]:
            i = i + 1
        else:
            return "*"

    return P[len(P) - 1]['p'][1:]


def solve(P):
    patters = []
    for pattern in P:
        patters.append({'p': pattern, 'length': len(pattern)})
    patters = sorted(patters, key=lambda k: k['length'])
    return set_1(patters)


t = int(input())

for test_case in range(t):

    n = int(input())

    patterns = []
    for _ in range(n):
        patterns.append(input())

    result = solve(patterns)

    print("Case #{}: {}".format(test_case + 1, result))

