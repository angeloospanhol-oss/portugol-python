# Exercício 39 — Caixa eletrônico: contagem de notas
# Nome: Angelo Otavio Spanhol
# Objetivo: Calcular a menor quantidade de notas de um saque

# Pedindo para o usuário informar o valor do saque
saque = int(input("Digite a quantidade de saque: "))

# Verificando se o valor digitado corresponde as especificações
if saque %10 != 0 or saque <= 0:
    print("Valor inválido para saque")
else:
    # Se o saque for divisivel por 100 contabiliza a quantidade de notas de R$100
    if saque // 100:
        notas100 = saque // 100     # Conta quantas vezes foi dividido (Quantidade de notas) 
        saque = saque % 100     # Pega o resto da divisão (Valor do saque)
        print("Notas de R$100:", notas100)

    # Se o saque for divisivel por 50 contabiliza a quantidade de notas de R$50
    if saque // 50:
        notas50 = saque // 50     # Conta quantas vezes foi dividido (Quantidade de notas) 
        saque = saque % 50     # Pega o resto da divisão (Valor do saque)
        print("Notas de R$50:", notas50)

    # Se o saque for divisivel por 20 contabiliza a quantidade de notas de R$20
    if saque // 20:
        notas20 = saque // 20     # Conta quantas vezes foi dividido (Quantidade de notas) 
        saque = saque % 20     # Pega o resto da divisão (Valor do saque)
        print("Notas de R$20:", notas20)

    # Se o saque for divisivel por 10 contabiliza a quantidade de notas de R$10
    if saque // 10:
        notas10 = saque // 10     # Conta quantas vezes foi dividido (Quantidade de notas) 
        saque = saque % 10     # Pega o resto da divisão (Valor do saque)
        print("Notas de R$10:", notas10)
