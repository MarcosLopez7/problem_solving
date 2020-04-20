def solve(n):
    add = 0
    result = []
    r = 1

    if n > 1001:
        triangle_now = [1, 2, 1]
        next_row = [1, 3, 3, 1]
        add = 4
        result.append((1, 1))
        result.append((2, 1))
        result.append((3, 2))
        r = 3
        k = 2
        while add + sum(next_row[:k-1]) < n:
            triangle_now = next_row
            next_row = []
            i = 0
            next_row.append(triangle_now[i])
            while i < len(triangle_now) - 1:
                next_row.append(triangle_now[i] + triangle_now[i + 1])
                i = i + 1
            next_row.append(1)
            r = r + 1
            k = r // 2
            if len(triangle_now) % 2 != 0:
                k = k + 1

            add = add + triangle_now[k - 1]
            result.append((r, k))

        k = k - 1
        while k > 0:
            add = add + triangle_now[k - 1]
            result.append((r, k))
            k = k - 1

        while add != n:
            r = r - 1
            add = add + 1
            result.append((r, 1))

        return result

    elif n > 501:
        add = 5
        result.append((1, 1))
        result.append((2, 1))
        result.append((2, 2))
        result.append((3, 2))
        r = 4

        while add != n and (add + r - 1) < n:
            add = add + r - 1
            result.append((r, 2))
            r = r + 1

        if add != n:
            add = add + 1
            result.append((r - 1, 1))

    elif n > 6:
        add = 6
        result.append((1, 1))
        result.append((2, 1))
        result.append((2, 2))
        result.append((3, 2))
        result.append((3, 1))
        r = 4

    while sum != n:
        add = add + 1
        result.append((r, 1))
        r = r + 1

    return result


t = int(input())

for test_case in range(t):
    n = int(input())

    res = solve(n)

    print("Case #{}:".format(test_case + 1))
    for r in res:
        print(str(r[0]) + " " + str(r[1]))
