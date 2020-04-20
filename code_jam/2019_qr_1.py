t = int(input())

for test_case in range(t):
    n = input()
    a = ''
    b = ''

    for digit in n:
        if digit == '4':
            a += '3'
            b += '1'
        else:
            a += digit
            b += '0'

    print("Case #{}: {} {}".format(test_case + 1, int(a), int(b)))
