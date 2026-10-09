# Exercício 11 — O maior de dois  
# Nome: Angelo Otavio Spanhol
# Objetivo: Encontrar o maior de dois números fornecidos pelo usuário.

# Pedindo os números ao usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Verificando qual é o maior número
if n1 > n2:
    print("O maior é:", n1)
else:
    print("O maior é:", n2)