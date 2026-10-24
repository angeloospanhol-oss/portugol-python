# Exercício 25 — Radar com tipo de infração  
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o usuário está dentro do limite de velocidade e informar a porcentagem

# Pedindo o limite da via ao usuario
limite = int(input("Digite a velocidade maxima da via (em km/h): "))
# Pedindo a velocidade do carro ao usuario
velocidade = int(input("Digite a velocidade do carro (em km/h): "))

# calculo da porcentagem de velocidade acima do limite
percentualAcima = (velocidade - limite) / limite * 100

# Identificando qual tipo de infração
# Se percentual estiver acima de 50 infração gravissíma
if percentualAcima >= 50:
    print(f"{percentualAcima:.2f}% acima")
    print("Infração gravíssima")
# Se percentual estiver entre 20% e 50% infração grave   
elif percentualAcima > 20:
    print(f"{percentualAcima:.2f}% acima")
    print("Infração grave")
# Se percentual estiver entre 0% e 20% infração média
elif percentualAcima > 0:
    print(f"{percentualAcima:.2f}% acima")
    print("Infração média")
# Se a velociade estiver dentro do limite
else:
    print("Sem infração")

