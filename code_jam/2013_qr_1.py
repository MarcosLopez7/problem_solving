test_case = int(input())

def check(board):
    X = 0
    O = 0
    started_with = '.'
    dot = False

    #CHECANDO DIAGONAL SUPERIOR A INFERIOR
    for i in range(4):
        if board[i][i] == 'X':
            # if started_with == 'O':
            #     break
            X = X + 1
            started_with = 'X'
        elif board[i][i] == 'O':
            # if started_with == 'X':
            #     break
            O = O + 1
            started_with = 'O'
        elif board[i][i] == 'T':
            X = X + 1
            O = O + 1
        else:
            dot = True
            break

    if X == 4:
        return "X won"
    elif O == 4:
        return "O won"

    X = 0
    O = 0
    started_with = '.'

    #CHECANDO DIAGONAL INFERIOR A SUPERIOR
    for i in range(3, -1, -1):
        if board[i][3 - i] == 'X':
            # if started_with == 'O':
            #     break
            X = X + 1
            started_with = 'X'
        elif board[i][3 - i] == 'O':
            # if started_with == 'X':
            #     break
            O = O + 1
            started_with = 'O'
        elif board[i][3 - i] == 'T':
            X = X + 1
            O = O + 1
        else:
            dot = True
            break

    if X == 4:
        return "X won"
    elif O == 4:
        return "O won"

    #CHECANDO POR FILA
    for i in range(4):
        X = 0
        O = 0
        started_with = '.'

        for j in range(4):
            if board[i][j] == 'X':
                # if started_with == 'O':
                #     break
                X = X + 1
                started_with = 'X'
            elif board[i][j] == 'O':
                # if started_with == 'X':
                #     break
                O = O + 1
                started_with = 'O'
            elif board[i][j] == 'T':
                X = X + 1
                O = O + 1
            else:
                dot = True
                break
        if X == 4:
            return "X won"
        elif O == 4:
            return "O won"

    #CHECANDO POR COLUMNA
    for i in range(4):
        X = 0
        O = 0
        started_with = '.'

        for j in range(4):
            if board[j][i] == 'X':
                if started_with == 'O':
                    break
                X = X + 1
                started_with = 'X'
            elif board[j][i] == 'O':
                if started_with == 'X':
                    break
                O = O + 1
                started_with = 'O'
            elif board[j][i] == 'T':
                X = X + 1
                O = O + 1
            else:
                dot = True
                break
        if X == 4:
            return "X won"
        elif O == 4:
            return "O won"

    if dot:
        return "Game has not completed"
    else:
        return "Draw"


for t in range(test_case):

    board = []

    for _ in range(4):
        row = list(input())

        board.append(row)
    
    y = check(board)

    print(f"Case #{t + 1}: {y}")

    input()