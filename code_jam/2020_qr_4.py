def add(string):
    result = ""

    for i in range(len(string)):
        if string[i] == "0":
            result += "1"
        else:
            result += "0"

    return result


def resolve_for_10():
    result = ""
    for i in range(1, 11):
        print(i)
        result += input()

    return result


def resolve_for_20():
    part_1 = ""
    part_2 = ""
    for i in range(1, 6):
        print(i)
        part_1 += input()
        print(15 + i)
        part_2 += input()

    if part_1 != part_2[::-1] and part_1 != add(part_2[::-1]):
        muestreo = ""
        for i in range(1, 6):
            print(i)
            muestreo += input()

        if muestreo == add(part_1):
            part_1 = add(part_1)
            part_2 = add(part_2)
        elif muestreo == part_2[::-1]:
            part_1, part_2 = part_2[::-1], part_1[::-1]
        elif muestreo == add(part_2[::-1]):
            part_1, part_2 = add(part_2[::-1]), add(part_1[::-1])
        elif muestreo == part_1:
            pass

        for i in range(6, 11):
            print(i)
            part_1 += input()

        muestreo = ""
        for i in range(1, 6):
            print(i)
            muestreo += input()

        swapped = False
        if muestreo == add(part_1[:5]):
            part_1 = add(part_1)
            part_2 = add(part_2)
        elif muestreo == part_2[::-1]:
            part_1, part_2 = part_2[::-1], part_1[::-1]
            swapped = True
        elif muestreo == add(part_2[::-1]):
            part_1, part_2 = add(part_2[::-1]), add(part_1[::-1])
            swapped = True
        elif muestreo == part_1:
            pass

        if swapped:
            rango = range(6, 11)
        else:
            rango = reversed(range(11, 16))

        for i in rango:
            print(i)
            if swapped:
                part_1 += input()
            else:
                part_2 = input() + part_2

        return part_1 + part_2
    else:
        print(1)
        muestra = input()

        if muestra == add(part_1[0]):
            part_1 = add(part_1)
            part_2 = add(part_2)

        for i in range(6, 10):
            print(i)
            part_1 += input()

        print(10)
        input()

        for i in reversed(range(12, 16)):
            print(i)
            part_2 = input() + part_2

        if part_1[5:9] == part_2[12:16][::-1]:
            print(6)
            muestra = input()

            if muestra == add(part_1[5]):
                part_1 = add(part_1)
                part_2 = add(part_2)

            print(10)
            part_1 += input()
            print(11)
            part_2 = input() + part_2

            return part_1 + part_2
        elif part_1[5:9] == add(part_2[12:16][::-1]):
            print(5)
            muestra = input()
            print(6)
            muestra += input()

            if muestra == add(part_1[4:6]):
                part_1 = add(part_1)
                part_2 = add(part_2)
            elif muestra == part_2[14:16][::-1]:
                part_1, part_2 = part_2, part_1
            elif muestra == add(part_2[14:16][::-1]):
                part_1, part_2 = add(part_2), add(part_1)
            elif muestra == part_1[4:6]:
                pass

            print(10)
            part_1 += input()
            print(11)
            part_2 = input() + part_2

            return part_1 + part_2
        else:
            muestra = ""
            for i in range(6, 10):
                print(i)
                muestra += input()

            if muestra == add(part_1[5:9]):
                part_1 = add(part_1)
                part_2 = add(part_2)
            elif muestra == part_2[11:15][::-1]:
                part_1, part_2 = part_2, part_1
            elif muestra == add(part_2[11:15][::-1]):
                part_1, part_2 = add(part_2), add(part_1)
            elif muestra == part_1[5:9]:
                pass

            print(10)
            part_1 += input()
            print(11)
            part_2 = input() + part_2

            return part_1 + part_2


line = input().split()

t = int(line[0])
b = int(line[1])

for test_case in range(t):
    
    if b == 10:
        result = resolve_for_10()
    elif b == 20:
        result = resolve_for_20()
    elif b == 100:
        lel = ["1" for _ in range(100)]
        result = ''.join(lel)

    print(result)

    response = input()

    if response == 'N':
        exit(-1)