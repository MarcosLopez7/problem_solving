test_cases = int(input())

for t in range(test_cases):
    m = int(input())

    deck = []

    for _ in range(m):
        line = input().split(" ")

        for _ in range(int(line[1])):
            deck.append(int(line[0]))

    print(deck)        
