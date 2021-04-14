test_cases = int(input())

for t in range(test_cases):
    line = input().split(" ")

    x = int(line[0])
    y = int(line[1])
    s = list(line[2])

    r = 0

    if x >= 0 and y >= 0:
        i = 0

        while i < len(s):
            if s[i] == '?':
                if i != 0:
                    figure_to_change = s[i - 1]
                else:
                    while i < len(s) and s[i] ==  '?':
                        i = i + 1
                    if i == len(s):
                        i = 0
                        while i < len(s):
                            s[i] = 'J'
                            i = i + 1
                        break
                    else:
                        figure_to_change = s[i]
                        i = 0
                        
                while i < len(s) and s[i] ==  '?':
                    s[i] = figure_to_change
                    i = i + 1
            else:
                i = i + 1      

    for i in range(len(s) - 1):
        if s[i] == 'C' and s[i + 1] == 'J':
            r = r + x
        elif s[i] == 'J' and s[i + 1] == 'C':
            r = r + y

    print(f"Case #{t + 1}: {r}")