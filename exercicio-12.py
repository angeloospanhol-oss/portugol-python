# Exercício 12 — Divisão segura   
# Nome: Angelo Otavio Spanhol
# Objetivo: Realizar uma divisão segura entre dois números fornecidos pelo usuário.

# Pedindo o divisor ao usuário
divisor = int(input("Digite o divisor: "))
# Pedindo o dividendo ao usuário
dividendo = int(input("Digite o dividendo: "))

# Verificando se o divisor é zero
if divisor == 0:
    print("Erro: não existe divisão por zero ")
# Se o divisor não for zero, realiza a divisão
else:
    print("O resultado da divisão é:", dividendo / divisor)