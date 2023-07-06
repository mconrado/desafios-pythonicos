def ver_regras(celula, vizinhos):
    qt_vizinhos_vivos = vizinhos.count(1)

    estado_celula = 0

    permanece_viva = celula == 1 and (qt_vizinhos_vivos in (2, 3))
    ressucita = celula == 0 and qt_vizinhos_vivos == 3

    if permanece_viva or ressucita:
        estado_celula = 1

    return estado_celula

