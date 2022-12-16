"""
Dois corredores A e B correm a mesma velocidade só que em percursos e distâncias diferentes.
Partem do mesmo ponto de inicio.

Recebendo  dois números, ou seja, a distância de percurso de cada um, a função deve retornar
quantas voltas cada um deve dar para se encontrar denovo no ponto de partida
"""


def nbr_of_laps(x, y):
    calcx = []
    calcy = []

    calctotal = x if x > y else y

    div = lambda a, b: a / b

    for tab in range(1, calctotal + 1):
        calcx.append(x * tab)
        calcy.append(y * tab)

    lapx = [resultx for resultx in calcx if resultx % y == 0][0]
    lapy = [resulty for resulty in calcy if resulty % x == 0][0]

    return div(lapx, x), div(lapy, y)


assert nbr_of_laps(5, 3) == (3, 5)
assert nbr_of_laps(4, 6) == (3, 2)
assert nbr_of_laps(5, 5) == (1, 1)
assert nbr_of_laps(8, 4) == (1, 2)
assert nbr_of_laps(7, 14) == (2, 1)
