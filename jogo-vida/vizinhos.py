#https://replit.com/@holland1antari/jogo-da-vida-dojo-da-galera#main.py
from copy import deepcopy

def vizinhos(matrix, grupo_alvo, pos_alvo):
    vizinhos = []
    matrix_alvos = marca_elemento_alvo(matrix, grupo_alvo, pos_alvo)
    matrix_alvos = matrix_envolvidos(matrix_alvos, envolvidos(matrix, grupo_alvo))
    
    pos_alvos = envolvidos(matrix[grupo_alvo], pos_alvo)


    for grupo in matrix_alvos:
        for k, celula in enumerate(grupo):
            if celula == -1:
                continue

            if k in pos_alvos:
                vizinhos.append(celula)
    
    return vizinhos

def anterior(alvo):
    return 0 if alvo == 0 else alvo - 1

def posterior(alvo, limite):
    return alvo if alvo == limite - 1 else alvo + 1

def matrix_envolvidos(matrix, grupos_envolvidos): 
    return [matrix[x] for x in grupos_envolvidos]

def envolvidos(grupo, alvo):
    alvo_anterior = anterior(alvo)
    alvo_posterior = posterior(alvo, len(grupo))

    return set([alvo, alvo_anterior, alvo_posterior])

def marca_elemento_alvo(matrix, grupo, alvo):
    matrix_com_elemento_alvo_marcado = deepcopy(matrix)
    matrix_com_elemento_alvo_marcado[grupo][alvo] = -1
    
    return matrix_com_elemento_alvo_marcado

