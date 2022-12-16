"""
Print Errors

Dado um conjunto de string como parâmetro na função
encontre a quantidade de caracteres que sejam maior que 'm'
e retorne a quantidade deles barra total de caracteres enviados

exemplo:
'ajajsjdhhmyy' => '3/12'
"""

def printer_error(s):

    count_m = [1 for x in s if x > 'm']

    return str(sum(count_m)) + '/' + str(len(s))


assert printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") == "3/56"
assert printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") == "6/60"
assert printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu") == "11/65"
assert printer_error("ajajsjdhhmyy") == "3/12"
