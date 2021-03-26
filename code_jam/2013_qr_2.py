test_case = int(input())

for t in range(test_case):
    line = input().split(" ")
    n = int(line[0])
    m = int(line[1])

    pattern = []
    lawn = []

    for _ in range(n):
        row_pattern = [int(n) for n in input().split(" ")]
        row_lawn = [100 for _ in range(m)]
        pattern.append(row_pattern)
        lawn.append(row_lawn)

    y = "YES"

    finished = False

    while not finished:
        cutted = False 
        ## CHECANDO FILA POR FILA
        for i in range(n):
            h = pattern[i][0]
            cuttable = True
            for j in range(m):
                if h < pattern[i][j]:
                    cuttable = False
                    break

            if cuttable:
                for j in range(m):
                    if h < lawn[i][j]:
                        lawn[i][j] = h
                        cutted = True

        ## CHECANDO COLUMNA POR COLUMNA
        for i in range(m):
            h = pattern[0][i]
            cuttable = True
            for j in range(n):
                if h < pattern[j][i]:
                    cuttable = False
                    break

            if cuttable:
                for j in range(n):
                    if h < lawn[j][i]:
                        lawn[j][i] = h
                        cutted = True

        different = False

        for i in range(n):
            has_different = False
            for j in range(m):        
                if lawn[i][j] != pattern[i][j]:
                    different = True
                    has_different = True
                    break
            if has_different:
                break

        if not different:
            y = "YES"
            finished = True

        if not cutted:
            y = "N0"
            finished = True

    print(f"Case #{t + 1}: {y}")