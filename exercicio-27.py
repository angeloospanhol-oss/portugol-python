# Exercício 27 — Número no intervalo
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se um numero está entre 1 e 100

# Pedindo para o usuario digitar um numero
numero = int(input("Digite um numero: "))

# Se o numero estiver entre 100 e 1 dentro do intervalo
if numero <= 100 and numero >= 1:
    print(numero, "dentro do intervalo")
# Se o numero não estiver entre 100 e 1 fora do intervalo 
else:
    print(numero, "fora do intervalo")