# Exercício 17 — Positivo, negativo ou zero   
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o número é positivo, negativo ou zero.

# Pedindo um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é positivo ou negativo
# Numero negativo:
if numero < 0:
    print("O número é negativo.")
# Numero positivo:
elif numero > 0:
    print("O número é positivo.")
# Numero zero:
else:
    print("O número é zero.")