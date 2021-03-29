from random import shuffle
from copy import deepcopy
import time

def create_chessboard():
    n = 8                                          # número de linhas e colunas do tabuleiro de xadrez.
    elements = [0, 0, 0, 0, 0, 0, 0, 1]            # elementos que compoem a linha de um tabuleiro. 0: vazio, 1: rainha. Dessa forma reduzimos as possibilidades para 8!
    chessboard = []                                # espaço do tabuleiro.

    for line in range(0, n):                       # construção do tabuleiro com elementos aleatoriamente posicionados
        shuffle(elements)                          # alternando ordem dos elementos a cada linha
        chessboard.append(elements.copy())         # adicionando linha que só contém 1 rainha ao tabuleiro. Fazendo cópia da lista para não pegar por referência.

    return chessboard

def print_chessboard(chessboard):
    for line in range(0, len(chessboard)):
        print(chessboard[line])

def checking_queen(chessboard):
    n = len(chessboard)
    conflicts = 0

    #  validação de 1 rainha por linha
    for line in range (0, n):         
        queens = sum_check(chessboard[line])        
        if queens == 1:
            continue
        else:
            if queens == 0:
                continue
            else:
                conflicts += queens
            
    # validação de 1 rainha por coluna
    for column in range (0, n):       
        column_list = []
        for line in range (0, n):
            column_list.insert(line, chessboard[line][column])
        
        queens = sum_check(column_list)
        if queens == 1:
            continue
        else:
            if queens == 0:
                continue
            else:
                conflicts += queens
            
    
    diagonal_list = []
    last_line = 1               # inicialmente consideramos que não estamos na última linha do tabuleiro
    
    # validação de 1 rainha por diagonal secundária
    for d in range(0, n):       
        if d == 0:
            diagonal_list.append(chessboard[d][d])

            queens = diagonal_list[d]
            if queens == 1:
                continue
            else:
                if queens == 0:
                    continue
                else:
                    conflicts += queens
        else:
            diagonal = []
            j = 0

            if d == 7:
                last_line = 0                       # Passa a identificar a última linha na primeira vez que passa

            for i in range (d, -1, -1):
                diagonal.append(chessboard[i][j])

                if j <= d:
                    j += 1
            
            diagonal_list.append(diagonal)

            queens = sum_check(diagonal_list[d])        
            if queens == 1:
                continue
            else:
                if queens == 0:
                    continue
                else:
                    conflicts += queens

    # continuação da validação de 1 rainha por diagonal secundária
    # segundo loop, apenas na última linha
    if last_line == 0:
        for column_j in range (1, n):               # começa da coluna 1 e vai até a 7
            j = column_j
            diagonal = []

            for line_i in range (n - 1, column_j - 1, -1):     # começa da linha 7 e vai até a 1
                diagonal.append(chessboard[line_i][j])

                j += 1
            diagonal_list.append(diagonal)
            queens = sum_check(diagonal_list[column_j + line])

            if queens == 1:
                continue
            else:
                if queens == 0:
                    continue
                else:
                    conflicts += queens


    diagonal_list_main = []
    last_line = 1               # inicialmente consideramos que não estamos na última linha do tabuleiro
    times = 1

    # validação de 1 rainha por diagonal principal
    for dp in range (n - 1, -1, -1):
        if dp == 7:
            diagonal_list_main.append(chessboard[dp][0])

            queens = diagonal_list_main[0]
        
            if queens == 1:
                times += 1
                continue
            else:
                if queens == 0:
                    times += 1
                    continue
                else:
                    conflicts += queens

            times += 1
        else:
            diagonal = []
            i = dp

            if dp == 0:
                last_line = 0                       # Passa a identificar a primeira linha na primeira vez que passa

            for j in range (0, times):
                diagonal.append(chessboard[i][j])

                if i < n:
                    i += 1
            
            diagonal_list_main.append(diagonal)
            queens = sum_check(diagonal_list_main[times - 1])

            if queens == 1:
                times += 1
                continue
            else:
                if queens == 0:
                    times += 1
                    continue
                else:
                    conflicts += queens
            
            times += 1

    # continuação da validação de 1 rainha por diagonal principal
    # segundo loop, apenas na primeira linha
    if last_line == 0:
        times = n - 1

        for column_j in range (1, n):
            j = column_j
            diagonal = []

            for i in range (0, times):
                diagonal.append(chessboard[i][j])

                if j < n:
                    j += 1
            
            diagonal_list_main.append(diagonal)
            queens = sum_check(diagonal_list_main[column_j + 7])

            if queens == 1:
                times -= 1
                continue
            else:
                if queens == 0:
                    times -= 1
                    continue
                else:
                    conflicts += queens

            times -= 1


    return conflicts
        
def sum_check(line_column_diagonal):
    sum = 0

    for element in line_column_diagonal:
        sum += element
    
    return sum

def shuffle_board(chessboard):
    for i in range (0, 8):
        shuffle(chessboard[i])

    return chessboard

def compare_boards(chessboards, chessboard):
    if not chessboards:
        chessboards.append(deepcopy(chessboard))
    else: 
        if chessboard not in chessboards:
            chessboards.append(deepcopy(chessboard))

    return len(chessboards)

def compare(chessboards, chessboard):
    if chessboard in chessboards:
        return True                 # configuração já está salva, passar pra próxima configuração
    else:
        return False                # configuração ainda não está na pasta, deve passar por verificações
                 
def create_boards():
    qty_solutions = 0
    n = 8

    chessboard = []
    chessboards = []                                  

    # Montando chessboard básico
    chessboard = create_chessboard()

    while (qty_solutions < 5):                                  # Trocar por 96, total de soluções
        chessboard = shuffle_board(chessboard)

        new_solution = compare(chessboards, chessboard)         # Se já for uma configuração salva, passa para a próxima configuração
        if not new_solution:

            # Número de conflitos
            conflicts = checking_queen(chessboard)       

            if conflicts == 0:
                qty_solutions = compare_boards(chessboards, chessboard)
                print(f'Solução {qty_solutions}:')
                print_chessboard(chessboards[qty_solutions - 1])
                print('\n')
    
    return chessboards


# Criação automática de novas configurações
ini = time.time()

chessboards = create_boards()
fim = time.time()

tempo = fim - ini

print(f'Tempo de execução: {tempo:,.2f}')
