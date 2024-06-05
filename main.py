'''
Trabalho 3 - Análise de Algoritmos

Alunos:
    Guilherme Ponce - 2011179
    João Victor Godinho - 2011401
'''

'''
Items do problema:
    Tamanho da mochila
    Item (valor,peso)

Metadados:
    Matriz com todos os OPTs ()

'''
#   (valor,peso)
possible_items = [
    (1,1),
    (6,2),
    (18,5),
    (22,6),
    (28,7)
]

knapsack_size = 10

def create_opts(items): #lista de tuplas (valor, peso)

    if(len(items) == 1):
        return 

    #calcula todas as combinações possíveis de items (novamente )

    return

def opt_knapsack(items,w): 

    '''
    Pega item a item da mochila
        Se o item cabe, verificar se a mochila com ele presente faz parte da solução ótima
        Se ele não cabe, próximo item

    Retorna solução ótima dado uma lista de items e tamanho da mochila
    '''

    return
