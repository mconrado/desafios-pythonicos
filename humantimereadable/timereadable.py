"""
Dado um número em segundos converta o mesmo no formato
de leitura humana sobre horas.

Exemplo:

funcao(1) retorna 00:00:01
funcao(5) retorna 00:00:05
funcao(86400) retorna 24:00:00
"""


def make_readable(seconds):
    hours = seconds // 60 // 60
    rest_seconds = seconds - (hours * 60 * 60)

    minutes = rest_seconds // 60
    rest_seconds = rest_seconds - (minutes * 60)

    seconds = rest_seconds

    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


assert make_readable(1) == "00:00:01"
assert make_readable(5) == "00:00:05"
assert make_readable(60) == "00:01:00"
assert make_readable(86399) == "23:59:59"
assert make_readable(359999) == "99:59:59"
