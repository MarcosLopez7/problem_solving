test_case = int(input())

for t in range(test_case):
    n = int(input())

    l = [int(e) for e in input().split(" ")]

    r = 0

    for i in range(len(l) - 1):
        min_num = min(l[i:len(l)])
        j = l.index(min_num)
        sub_l = l[i:j + 1]
        sub_l.reverse()
        l = l[0:i] + sub_l + l[j + 1:len(l)]
        r = r + j - i + 1

    print(f"Case #{t + 1}: {r}")