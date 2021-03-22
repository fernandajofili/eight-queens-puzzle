#  criação tabuleiro
#  criar teste de ataques
#  criar algoritmo de distribuição aleatória
#    checar condição de parada

# Ao receber validated = 0, gravar o chessboard como está no momento.
#    Comparar com chessboards já gravados antes. Se estiver igual a um anterior, ignorar. Se for diferente, salvar nas configurações
#    inéditas do tabuleiro

from random import shuffle

def chessboard():
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
    only_one_queen = 0                              # 0: true, 1: false

    #  validação de 1 rainha por linha
    for line in range (0, n):         
        queens = sum_check(chessboard[line])        
        if queens == 1:
            print(f'Apenas uma rainha na linha {line+1}')
        else:
            if queens == 0:
                print (f'Nenhuma rainha na linha {line+1}')
            else:
                print (f'Mais de uma rainha na linha {line+1}')
                only_one_queen = 1
            
    # validação de 1 rainha por coluna
    for column in range (0, n):       
        column_list = []
        for line in range (0, n):
            column_list.insert(line, chessboard[line][column])
        
        queens = sum_check(column_list)
        if queens == 1:
             print(f'Apenas uma rainha na coluna {column+1}')
        else:
            if queens == 0:
                print (f'Nenhuma rainha na coluna {column+1}')
            else:
                print (f'Mais de uma rainha na coluna {column+1}')
                only_one_queen = 1
            
    
    diagonal_list = []
    last_line = 1               # inicialmente consideramos que não estamos na última linha do tabuleiro
    
    # validação de 1 rainha por diagonal secundária
    for d in range(0, n):       
        if d == 0:
            diagonal_list.append(chessboard[d][d])

            queens = diagonal_list[d]
            if queens == 1:
                print(f'Apenas uma rainha na diagonal {d+1}')
            else:
                if queens == 0:
                    print (f'Nenhuma rainha na diagonal {d+1}')
                else:
                    print (f'Mais de uma rainha na diagonal {d+1}')
                    only_one_queen = 1
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
                print(f'Apenas uma rainha na diagonal {d+1}')
            else:
                if queens == 0:
                    print (f'Nenhuma rainha na diagonal {d+1}')
                else:
                    print (f'Mais de uma rainha na diagonal {d+1}')
                    only_one_queen = 1

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
                print(f'Apenas uma rainha na diagonal secundária {column_j + line + 1}')
            else:
                if queens == 0:
                    print (f'Nenhuma rainha na diagonal secundária {column_j + line + 1}')
                else:
                    print (f'Mais de uma rainha na diagonal secundária {column_j + line + 1}')
                    only_one_queen = 1


    diagonal_list_main = []
    last_line = 1               # inicialmente consideramos que não estamos na última linha do tabuleiro
    times = 1

    # validação de 1 rainha por diagonal principal
    for d in range (n - 1, -1, -1):
        if d == 7:
            diagonal_list_main.append(chessboard[d][0])

            queens = diagonal_list_main[0]
        
            if queens == 1:
                print(f'Apenas uma rainha na diagonal principal 1')
            else:
                if queens == 0:
                    print (f'Nenhuma rainha na diagonal principal 1')
                else:
                    print (f'Mais de uma rainha na diagonal principal 1')
                    only_one_queen = 1

            times += 1
        else:
            diagonal = []
            i = d

            if d == 0:
                last_line = 0                       # Passa a identificar a primeira linha na primeira vez que passa

            for j in range (0, times):
                diagonal.append(chessboard[i][j])

                if i < n:
                    i += 1
            
            diagonal_list_main.append(diagonal)
            queens = sum_check(diagonal_list_main[times - 1])

            if queens == 1:
                print(f'Apenas uma rainha na diagonal principal {times}')
            else:
                if queens == 0:
                    print (f'Nenhuma uma rainha na diagonal principal {times}')
                else:
                    print (f'Mais de uma rainha na diagonal principal {times}')
                    only_one_queen = 1
            
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
                print(f'Apenas uma rainha na diagonal principal {column_j + 8}')
            else:
                if queens == 0:
                    print (f'Nenhuma  rainha na diagonal principal {column_j + 8}')
                else:
                    print (f'Mais de uma rainha na diagonal principal {column_j + 8}')
                    only_one_queen = 1

            times -= 1


    return only_one_queen 
        




def sum_check(line_column_diagonal):
    sum = 0

    for element in line_column_diagonal:
        sum += element
    
    return sum

# Apresentando chessboard
chessboard = chessboard()

# Imprimindo chessboard
print_chessboard(chessboard)

# Testes de validação
validated = checking_queen(chessboard)          # 0: true, 1: false

if validated == 0:
    print("Solução de configuração de tabuleiro para questão das 8 rainhas")
else:
    print("Não é uma solução de configuração de tabuleiro")
