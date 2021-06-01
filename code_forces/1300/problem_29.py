def solve(statements):
    x = 0

    for statement in statements:
        if '+' in statement:
            x = x + 1
        else:
            x = x - 1

    return x


n = int(input())
statements = [input() for _ in range(n)]

result = solve(statements)
print(result)



