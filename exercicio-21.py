# Exercício 21 — Faixa etária  
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar se a idade digitada é criança, adolecente, adulto ou idoso.

# Pedindo para o usuario digitar a idade
idade = int(input("Digite uma idade: "))

# Identificando se o usuario é criança, adolecente, adulto ou idoso
# Se a idade for menor que 0
if idade <= 0:
    print("Idade invalida!")
# Se ele for criança
elif idade <= 12:
    print("Criança") 
# Se ele for adolecente
elif idade <= 17:
    print("Adolcente")
# Se ele for adulto
elif idade <= 59:
    print("Adulto")
# Se ele for idoso
else:
    print("Idoso")