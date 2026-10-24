# Exercício 31 — Tipo de triângulo
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar o tipo de triângulo (equilátero, isóceles e escaleno)

# Pedindo ao usuário o valor dos lados
lado1 = float(input("Digite o primeiro número para o lado do triângulo: "))
lado2 = float(input("Digite segundo número para o lado do triângulo: "))
lado3 = float(input("Digite terceiro número para o lado do triângulo: "))

# Identificando o tipo de triângulo
# Quando o triângulo não fecha
if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
    print("Esses lados não formam um triângulo")
# Triãngulo equilátero todos os lados iguais
elif lado1 and lado2 == lado3:
    print("Triângulo equilátero")
# Triângulo isóceles dois lados iguais e um diferente
elif lado1 and lado2 != lado3 or lado1 and lado3 != lado2 or lado3 and lado2 != lado1:
    print("Triângulo isóceles")
# Triângulo escaleno todos os lados diferentes
else:
    print("Triãngulo escaleno")