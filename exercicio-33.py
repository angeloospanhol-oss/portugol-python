# Exercício 33 — Voto obrigatório
# Nome: Angelo Otavio Spanhol
# Objetivo: Ler a idade do usuario e informar a situação de voto dele

# Pedindo para o usuario digitar a idade
idade = int(input("Digite sua idade: "))

# Analizando se o usuário pode votar
# Se o usuário for menor de idade não pode votar
if idade < 16:
    print("Não pode votar")
# Se o usuário ter entre 16, 17 ou for maior que 70 anos voto facultativo
elif idade <= 17 or idade > 70:
    print("Voto facultativo")
# Se o usuário for adulto voto obrigatório
else:
    print("Voto obrigatório")