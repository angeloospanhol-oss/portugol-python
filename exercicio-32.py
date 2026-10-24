# Exercício 32 — Login com usuário e senha
# Nome: Angelo Otavio Spanhol
# Objetivo: Confirmar login do usuario

# Pedindo para o usuario digitar o usuario e senha
usuario = input("Digite o usuario: ")
senha = int(input("Digite a senha: "))

# Analizando se usuario e senha estão corretos
# Se o usuario e senha forem digitados corretamente login realizado com sucesso!
if usuario == "aluno" and senha == 1234:
    print("Login realizado com sucesso!")
# Se a senha for incorreta senha incorreta
elif usuario == "aluno" and senha != 1234:
    print("Senha incorreta")
# Se o usuario for incorreto usuário não encontrado
elif usuario != "aluno" and senha == 1234:
    print("Usuário não encontrado")
# Se usuário e senha estiverem incorretos
else:
    print("Usuario e senha não encontrado")