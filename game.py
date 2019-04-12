def cell_check(section):

    # contador de vizinhos
    neighbours = 0
    # referência para o centro do recorte
    center = section[1][1]

    # somando todos os elementos do grupo
    for row in section:
        for cell in row:
            neighbours += cell

    # removendo o valor da célula central para que sobre somente a soma dos vizinhos
    neighbours -= center

    #######################################
    if neighbours == 0 or neighbours == 1:
        center = 0
    if neighbours > 1:
        center = 1
    if neighbours > 4:
        center = 0
    ######################################
    return center

def limit(section):

    neighbours = 0
    center = section[1][1]

    for row in section:
        for cell in row:
            neighbours += cell

    neighbours -= center
    ######################################
    if neighbours >= 0:
        center = 0
    ######################################
    return center

def get_section(matrix, row, col):
    '''
    Extrai um recorte 3x3 em um plano tratando as extremidades do plano
    como células sempre mortas
    '''
    # monta um plano 3x3 somente com células mortas para fazer uma cópia
    # da área a ser analizada
    section = [[0 for _ in range(3)] for _ in range(3)]

    # percorre as redondezas da célula de posição row x col copiando seu
    # valor para section exceto quando ultrapassa a borda
    for sec_r, r in enumerate(range(row-1, row+2)):
        for sec_c, c in enumerate(range(col-1, col+2)):
            if r >= 0 and c >= 0 and r < 50 and c < 50:
                section[sec_r][sec_c] = matrix[r][c]

    # devolve o recorte 3x3 do plano
    return section


def game_of_life(seed):
    '''
    Recebe uma seed de um plano 50x50 executa o game of life e devolve
    a geração seguinte
    '''
    next_gen = [[0 for _ in range(50)] for _ in range(50)]

    for r, row in enumerate(seed):
        for c, col in enumerate(row):
            next_gen[r][c] = cell_check(get_section(seed, r, c))
            if r == 49 or c == 49 or r == 0 or c == 0:
                next_gen[r][c] = limit(get_section(seed, r, c))
        
    return next_gen
