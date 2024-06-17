'''
Trabalho 3 - Análise de Algoritmos

Alunos:
    Guilherme Ponce - 2011179
    João Victor Godinho - 2011401
'''

print("Hello world!")


def i_bplate(which):
    i1 = [(10, 269),(55, 95),(10, 4),(47, 60),(5, 32),(4, 23),(50, 72),(8, 80),(61, 62),(85, 65),(87, 46)]
    i2 = [(20, 878), (44, 92), (46, 4), (90, 43), (72, 83), (91, 84), (40, 68), (75, 92), (35, 82), (8, 6), (54, 44), (78, 32), (40, 18), (77, 56), (15, 83), (61, 25), (17, 96), (75, 70), (29, 48), (75, 14), (63, 58)]
    i3 = [(4, 20), (9, 6), (11, 5), (13, 9), (15, 7)]
    i4 = [(4, 11), (6, 2), (10, 4), (12, 6), (13, 7)]
    i5 = [(10, 60), (20, 30), (18, 25), (17, 20), (15, 18), (15, 17), (10, 11), (5, 5), (3, 2), (1, 1), (1, 1)]
    i6 = [(7, 50), (70, 31), (20, 10), (39, 20), (37, 19), (7, 4), (5, 3), (10, 6)]
    i7 = [(5, 80), (33, 15), (24, 20), (36, 17), (37, 8), (12, 31)]
    match which:
        case 1:
            return i1
        case 2:
            return i2
        case 3:
            return i3
        case 4:
            return i4
        case 5:
            return i5
        case 6:
            return i6
        case 7:
            return i7
    return -1


def knapsackSolver(B: int, peso:list, valor:list):
    '''
    1) criar lista com W+1 e N+1 de tamanho
        talvez iniciar todo mundo com zero? nao tenho certeza

    2) for nos itens:
        for nos pesos:
            caso nao caiba na mochila, pega o anterior
            caso caiba:
                verificar max entre ter ele na mochila, e nao ter ele na mochila
    '''   
    QTD_MAX = 10 #quantidade maxima de vezes que posso pegar daquele item

    tam = len(valor) #quantidade de itens que eu tenho. Poderia ter pego o peso tambem para representar

    opt = [[0] * (B + 1) for i in range(tam + 1)]

    for i in range(1, tam + 1): #pula o primeiro elemento pois, sem nenhum item na mochila, o valor sempre será zero
        for j in range(B + 1):
            if(peso[i-1] > j): #nao cabe na mochila
                opt[i][j] = opt[i-1][j] #pega o valor anterior para o mesmo peso de mochila
            else:
                for n in range(1,QTD_MAX + 1):
                    if n * peso[i-1] <= j:
                        opt[i][j] = max(opt[i-1][j], (valor[i-1] * n) + opt[i-1][j- (n * peso[i-1])])

    return opt[-1][-1]

instancia = i_bplate(1)

W = instancia[0][1]

values = []
weights = []

for i in range(1,len(instancia)):
    values.append(instancia[i][0])
    weights.append(instancia[i][1]) 

# values = [60, 100, 120]
# weights = [10, 20, 30]
# W = 50
#   RESULTADO ESPERADO: 300


print(knapsackSolver(W,weights,values))
