def solve(word):
    lower_cases = 0
    upper_cases = 0

    for letter in word:
        if letter.lower() == letter:
            lower_cases = lower_cases + 1
        else:
            upper_cases = upper_cases + 1

    if lower_cases >= upper_cases:
        return word.lower()
    else:
        return word.upper()

word = input()
result = solve(word)
print(result)
