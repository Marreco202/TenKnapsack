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
    i8 = [(20, 879), (91, 84), (72, 83), (90, 43), (46, 4), (55, 44), (8, 6), (35, 82), (75, 92), (61, 25), (15, 83), (77, 56), (40, 18), (63, 58), (75, 14), (29, 48), (75, 70), (17, 96), (78, 32), (40, 68), (44, 92)]
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
        case 8:
            return i8
    return -1


def knapsackSolver(B: int, peso:list, valor:list):
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

    w = B
    items_count = [0] * tam


    #Quais itens foram incluídos
    for i in range(tam, 0, -1):
        for n in range(QTD_MAX, 0, -1):
            if n * peso[i-1] <= w and opt[i][w] == opt[i-1][w - n * peso[i-1]] + (n * valor[i-1]):
                items_count[i-1] += n
                w -= n * peso[i-1]
                break

    # print("Itens selecionados:", items_count)

    p_total = 0

    print("QTDx item (v,w)")
    for i in range(0,len(items_count)):
        if items_count[i] != 0:
            print("{}x item ({},{})".format(items_count[i],valor[i],peso[i])) #valor,peso
            p_total += (items_count[i] * peso[i])
 

    print("peso final: {}/{}".format(p_total,B))

    return opt[-1][-1]

# instancia = i_bplate(1)


values = []
weights = []

for j in range(1,9):

    instancia = i_bplate(j)
    W = instancia[0][1]
    
    print(" === INSTANCIA {} === ".format(j))

    for i in range(1,len(instancia)):
        values.append(instancia[i][0])
        weights.append(instancia[i][1]) 

    print("valor ótimo:",knapsackSolver(W,weights,values))
    # print("peso da mochila: ",instancia[0][1])
    values = []
    weights = []
    print(" === ======== == === ".format(j))



