def create_parenthesis(string, n):
    if n >= 10:
        return string
    
    result = ""
    i = 0
    parentheses = False

    while i < len(string):
        if int(string[i]) < n:
            result += string[i]
        else:
            result += "("
            parentheses = True
            sub_str = string[i]
            i = i + 1
            while i < len(string) and int(string[i]) >= n:
                sub_str += string[i]
                i = i + 1
            result += create_parenthesis(sub_str, n + 1) + ")"
            i = i - 1

        i = i + 1

    return result


t = int(input())

for test_case in range(t):
    s = input()

    result = create_parenthesis(s, 1)

    print("Case #{}: {}".format(test_case + 1, result))