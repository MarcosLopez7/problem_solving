letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def max_factor(a, b, last_factor = 1):
    if a == b:
        return (a // last_factor)

    while b:
        mcd = b
        b = a % b
        a = mcd
    return mcd


def get_word(ciphertext, l):
    numbers = []

    index = 0

    for i in reversed(range(l - 1)):
        if ciphertext[i + 1] != ciphertext[i]:
            index = i
            break

    first_factor = max_factor(ciphertext[index + 1], ciphertext[index])
    factor = 1

    for i in reversed(range(index + 1)):
        factor = max_factor(ciphertext[i + 1], ciphertext[i], factor)
        if i == l - 2:
            numbers.append(ciphertext[i + 1] // factor)
        numbers.append(factor)
        last_number = ciphertext[i]
        last_letter_value = factor

    numbers.append(last_number // last_letter_value)

    other_part = []
    if index != l - 2:
        factor = first_factor
        for i in range(index + 1, l - 1):
            factor = max_factor(ciphertext[i + 1], ciphertext[i], factor)
            other_part.append(factor)
            last_number = ciphertext[i + 1]
            last_letter_value = factor
        other_part.append(last_number // last_letter_value)

    numbers = list(reversed(other_part)) + numbers

    ordered_numbers = sorted(list(set(numbers)))
    letter_values = {ordered_numbers[i]: letters[i] for i in range(len(letters))}
    result = ""
    for n in numbers:
        result += letter_values[n]

    return result[::-1]


t = int(input())

for test_case in range(t):
    line = input().split()
    n = int(line[0])
    l = int(line[1])

    ciphertext = list(map(int, input().split()))

    res = get_word(ciphertext, l)
    print("Case #{}: {}".format(test_case + 1, res))


def cipher_text(word, list_value):
    result = []

    for i in range(len(word) - 1):
        result.append(list_value[word[i]] * list_value[word[i + 1]])

    return " ".join(list(map(str, result)))
