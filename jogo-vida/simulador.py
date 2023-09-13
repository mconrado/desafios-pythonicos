from vizinhos import vizinhos
from ver_regras import ver_regras
from time import sleep
from os import system
from copy import deepcopy

#SIMULACÓES
matrix1 = [[0, 1], [0, 0], [1, 1]]
matrix1 = [[1, 1, 0], [1, 0, 1], [0, 1, 0]]
matrix1 = [[0, 0], [1, 1], [0, 0]]
matrix1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
matrix1 = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
matrix1 = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],[0, 0, 0, 0, 0]]


def printa_matriz(matriz, cls=False):
    if cls : system('clear')
    for linha in matriz:
        for item in linha:
            print(item, end=' ')
        print(end='\n')
    print(end='\n')


if __name__ == "__main__":
    system('clear')
    printa_matriz(matrix1)
    sleep(1)
    matrix_resultado = deepcopy(matrix1)
    matrix_anterior = []
    
    while True:

        for pos_grupo, grupo in enumerate(matrix1):
            for pos_cel, celula in enumerate(grupo):
                viz = vizinhos(matrix1, pos_grupo, pos_cel)
                matrix_resultado[pos_grupo][pos_cel] = ver_regras(celula, viz)

        printa_matriz(matrix_resultado, True)
        sleep(0.5)

        if matrix1 == matrix_resultado:
            break
        
        matrix1 = deepcopy(matrix_resultado)
    
