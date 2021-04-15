test_cases = int(input())

for t in range(test_cases):
    n = int(input())

    l = [int(x) for x in input().split(" ")]

    r = 0

    i = 1

    while i < n:
        if l[i] > l[i - 1]:
            i = i + 1
        else:
            digit_diff = len(str(l[i - 1])) - len(str(l[i]))
            nines = ''

            for _ in range(digit_diff):
                nines += '9'

            max_number = str(l[i]) + nines
            max_number = int(max_number)

            zeros = ''
            for _ in range(digit_diff):
                zeros += '0'
            min_number = str(l[i]) + zeros
            min_number = int(min_number)

            if max_number <= l[i - 1]:
                digit_diff = digit_diff + 1
                l[i] = str(min_number) + '0'
                l[i] = int(l[i])
            elif min_number > l[i - 1]:
                l[i] = min_number
            else:
                l[i] = l[i - 1] + 1

            r = r + digit_diff

            i = i + 1

    print(f"Case #{t + 1}: {r}")