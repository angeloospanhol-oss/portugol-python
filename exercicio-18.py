# Exercício 18 — Maior ou iguais  
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o primeiro número é maior, menor ou igual ao segundo número.

# Pedindo os números ao usuário
# Numero 1:
n1 = float(input("Digite o primeiro número: "))
# Numero 2:
n2 = float(input("Digite o segundo número: "))

# Verificando qual é o maior número
# Se o primeiro número for maior que o segundo:
if n1 > n2:
    print("O maior é:", n1)
# Se o segundo número for maior que o primeiro:
elif n2 > n1:
    print("O maior é:", n2)
# Se os números forem iguais:
else:
    print("Os números são iguais.")