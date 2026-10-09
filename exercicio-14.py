# Exercício 14 — Radar de velocidade   
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o usuário está dentro do limite de velocidade.

# Pedindo a velocidade do carro ao usuário
velocidade = int(input("Digite a velocidade do carro (em km/h): "))

# Verificando se o usuário está dentro do limite de velocidade
# Limite de velocidade: 80 km/h
# Velocidade acima do limite:
if velocidade > 80:
    print("Multado! Você passou", velocidade - 80, "km/h acima do limite.")
# Velocidade dentro do limite:
else:
    print("Velocidade dentro do limite. Boa viagem! ")
