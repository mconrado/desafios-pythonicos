import pytest
from ver_regras import ver_regras 
from vizinhos import vizinhos

matrix0 = [[0, 0], [1, 1]]
matrix1 = [[0, 1], [0, 0], [1, 1]]
matrix2 = [[1, 1, 0], [1, 0, 1], [0, 1, 0]]

def test_ver_regras():  
  assert ver_regras(1, vizinhos(matrix0, 1, 1)) == 0
  assert ver_regras(1, vizinhos(matrix1, 2, 1)) == 0
  assert ver_regras(1, vizinhos(matrix2, 0, 0)) == 1

if __name__ == "__main__":
    pytest.main(['-svv', __file__])

