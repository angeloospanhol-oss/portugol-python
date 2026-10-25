# Exercício 37 — Três números em ordem crescente
# Nome: Angelo Otavio Spanhol
# Objetivo: Organizar os números em ordem crescente

# Pedindo para o usuário digitar os números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Organizando a sequencia dos números
# Se n1 for maior que n2 e n2 for maior que n3:
if n1 > n2 and n2 > n3:
    print(n1, n2, n3)
# Se n1 for maior que n3 e n3 for maior que n2:
elif n1 > n3 and n3 > n2:
    print(n1, n3, n2)
# Se n2 for maior que n1 e n1 for maior que n3:
elif n2 > n1 and n1 > n3:
    print(n2, n1, n3)
# Se n2 for maior que n3 e n3 for maior que n1:
elif n2 > n3 and n3 > n1:
    print(n2, n3, n1)
# Se n3 for maior que n2 e n2 for maior que n1:
elif n3 > n2 and n2 > n1:
    print(n3, n2, n1)
# Se n3 for maior que n1 e n1 for maior que n2:
else:
    print(n3, n1, n2)