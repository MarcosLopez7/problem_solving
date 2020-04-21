def solve(queue, t):
    i = len(queue) - 1
    result = [l for l in queue]

    # while 0 < i:
    #     if queue[i] == 'G':
    #         result[i] = 'G'
    #         j = i - 1
    #         while j >= i - t and queue[j] != 'G':
    #             result[j], result[j + 1] = result[j + 1], result[j]
    #             j = j - 1
    #
    #    else:
    #         pass


line = input().split()

n, t = int(line[0]), int(line[1])

sequence = input()

