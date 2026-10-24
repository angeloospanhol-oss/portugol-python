# Exercício 24 — Calculadora de IMC   
# Nome: Angelo Otavio Spanhol
# Objetivo: Calcular o IMC do usuario com base no peso e altura

# Pedindo ao usuario o peso
peso = float(input("Digite o seu peso em kg: "))
# Pedindo ao usuario a altura
altura = float(input("Digite sua altura em metros: "))

# Calculo do IMC
imc = peso / (altura * altura)

# Analizando o IMC do usuario
# Se o IMC for menor que 18.5 abaixo do peso
if imc <= 18.5:
    print(f"Seu IMC foi de: {imc:.2f}")
    print("Abaixo do peso")
# Se o IMC estiver de 18.5 até menos de 25 peso normal
elif imc <= 25:
    print(f"Seu IMC foi de: {imc:.2f}")
    print("Peso normal")
# Se o IMC estiver de 25 até menos de 30 sobrepeso
elif imc <= 30:
    print(f"Seu IMC foi de: {imc:.2f}")
    print("Sobrepeso")
# Se o IMC for maior que 30 sobrepeso
else:
    print(f"Seu IMC foi de: {imc:.2f}")
    print("Obesidade")