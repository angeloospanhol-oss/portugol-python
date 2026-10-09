# Exercício 16 — Saque no caixa eletrônico   
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o usuário possui saldo suficiente para realizar um saque no caixa eletrônico.

# Pedindo o saldo ao usuário
saldo = float(input("Digite o saldo do banco: R$"))
# Pedindo o valor do saque ao usuário
saque = float(input("Digite o valor do saque: R$"))

# Verificando se o usuário possui saldo suficiente para realizar o saque
# Caso o valor do saque seja maior que o saldo, exibir mensagem de saldo insuficiente
if saque > saldo:
    print("Saldo insuficiente para realizar o saque.")
# Se valor do saque for menor que o valor do saldo, saque realizado com sucesso e exibir o novo saldo
else:
    print("Saque realizado com sucesso. Novo saldo: R$", saldo - saque)