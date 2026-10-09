# Exercício 13 — Senha de acesso   
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se a senha fornecida pelo usuário está correta.

# Pedindo a senha ao usuário
senha = input("Digite sua senha: ")

# Verificando se a senha está correta
# Senha correta: "senai2026"
if senha == "senai2026":
    print("Acesso liberado!")
# Senha incorreta:
else:
    print("Acesso negado!")