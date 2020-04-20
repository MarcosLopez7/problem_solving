import sys

t = int(input())

for test_case in range(t):
    line = input().split()
    a, b = int(line[0]), int(line[1])
    n = int(input()) - 1

    tries = 0
    guess = (a + b) // 2
    min_n = a
    max_n = b
    print(guess)

    while n > 0:
        s = input()

        if s == 'TOO_BIG':
            max_n = guess - 1
        elif s == 'TOO_SMALL':
            min_n = guess + 1
        elif s == 'WRONG_ANSWER':
            print("error", file=sys.stderr)
            exit(-1)
        elif s == 'CORRECT':
            break

        guess = (min_n + max_n) // 2
        if guess == 0:
            guess = 1
        print(guess)

        n = n - 1