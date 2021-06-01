def solve(stones):
    result = 0

    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            result = result + 1

    return result


n = int(input())
stones = input()
result = solve(stones)
print(result)
