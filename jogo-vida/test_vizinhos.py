import pytest
from vizinhos import vizinhos, anterior, posterior, marca_elemento_alvo, envolvidos, matrix_envolvidos


matrix0 = [[0, 0], [1, 1]]
matrix1 = [[0, 1], [0, 0], [1, 1]]
matrix2 = [[1, 1, 0], [1, 0, 1], [0, 1, 0]]


def test_vizinhos():  
    assert vizinhos(matrix0, 0, 1) == [0, 1, 1]
    assert vizinhos(matrix0, 1, 1) == [0, 0, 1]
    assert vizinhos(matrix0, 0, 0) == [0, 1, 1]

    assert vizinhos(matrix1, 0, 1) == [0, 0, 0]
    assert vizinhos(matrix1, 1, 0) == [0, 1, 0, 1, 1]
    assert vizinhos(matrix1, 1, 1) == [0, 1, 0, 1, 1]
    assert vizinhos(matrix1, 2, 1) == [0, 0, 1]

    assert vizinhos(matrix2, 0, 0) == [1, 1, 0]
    assert vizinhos(matrix2, 0, 2) == [1, 0, 1]
    assert vizinhos(matrix2, 2, 1) == [1, 0, 1, 0, 0]
    assert vizinhos(matrix2, 1, 1) == [1, 1, 0, 1, 1, 0, 1, 0]


def test_posterior():
    assert posterior(0, 3) == 1
    assert posterior(1, 3) == 2
    assert posterior(1, 2) == 1
    assert posterior(2, 3) == 2


def test_anterior():
    assert anterior(0) == 0
    assert anterior(1) == 0
    assert anterior(2) == 1

def test_matrix_envolvidos():
    assert matrix_envolvidos(matrix1, {0, 1, 0}) == [[0, 1], [0, 0]]
    assert matrix_envolvidos(matrix1, {1, 0}) == [[0, 1], [0, 0]]
    assert matrix_envolvidos(matrix1, {1, 2, 0}) == [[0, 1],[0, 0], [1, 1]]

def test_envolvidos():
    assert envolvidos(matrix2, 0) == {0, 1}
    assert envolvidos(matrix2, 1) == {0, 1, 2}
    assert envolvidos(matrix2[0], 1) == {0, 1, 2}

def test_marca_elemento_alvo():
    assert marca_elemento_alvo(matrix1, 0, 1) == [[0, -1],[0, 0],[1, 1]] 
    assert marca_elemento_alvo(matrix1, 0, 0) == [[-1, 1],[0, 0],[1, 1]] 
    assert marca_elemento_alvo(matrix1, 2, 1) == [[0, 1],[0, 0],[1, -1]] 

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
    
