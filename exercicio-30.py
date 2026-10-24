# Exercício 30 — Ano bissexto
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar se o ano é bissexto ou não

# Pedindo para o usuário digitar um número
ano = int(input("Digite um ano: "))

# Identificando se o ano é bissexto ou não
# Se o ano dividido por 4 tiver resto 0 e ano dividido por 100 tiver resto diferente ou igual a 0 é bissexto, ou se for dividido por 400 com resto 0. 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print(ano, "é bissexto")
# Quando não é
else:
    print(ano, "não é bissexto")