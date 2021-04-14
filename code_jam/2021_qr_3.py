test_case = int(input())

for t in range(test_case):

    line = input().split(" ")

    n = int(line[0])
    c = int(line[1])

    min_cost = n - 1
    max_cost = sum(range(n + 1)) - 1

    if c < min_cost or c > max_cost:
        print(f"Case #{t + 1}: IMPOSSIBLE")
        continue

    result = [number + 1 for number in range(n)]
    remaining_cost = c - min_cost
    
    i = 0

    if remaining_cost >= n - 1:
        j = n - 1
    else:
        j = remaining_cost

    cont = 0

    while remaining_cost != 0:
        sub_result = result[i:j + 1]
        sub_result.reverse()
        result = result[0:i] + sub_result + result[j + 1:n]
        remaining_cost = remaining_cost - j + i


        if remaining_cost > n - 2 - cont:
            if cont % 2 == 0:
                j = j - 1
            else:
                i = i + 1
        else:
            if cont % 2 == 0:
                j = j - 1
                i = j - remaining_cost
            else:
                i = i + 1
                j = i + remaining_cost

        cont = cont + 1

    result = [str(num) for num in result]

    print(f"Case #{t + 1}: {' '.join(result)}")