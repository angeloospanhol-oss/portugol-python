# Exercício 29 — O maior de trê
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar qual número é o maior

# Pedindo para o usuário digitar os tres numeros
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Verificando qual é o maior número
# Se o primeiro número for maior: 
if n1 > n2 and n1 > n3:
    print(n1, "é o maior número")
# Se o segundo número for maior:
elif n2 > n1 and n2 > n3:
    print(n2, "é o maior número")
# Se o terceiro número for maior:
else:
    print(n3, "é o maior número")