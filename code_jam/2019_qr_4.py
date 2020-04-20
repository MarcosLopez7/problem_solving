def bit_process(bits, response):

    return bits


t = int(input())

for test_case in range(t):
    line = input().split()
    n, b, f = int(line[0]), int(line[1]), int(line[2])

    bits = ["0" if i % 2 == 0 else "1" for i in range(n)]
    last_response = ""

    while True:
        print("".join(bits))
        response = input()

        if response == last_response:
            break
        elif response == "-1":
            exit(-1)
        else:
            last_response = response

        bits = bit_process(bits, response)