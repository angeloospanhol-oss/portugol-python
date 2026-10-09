# Exercício 10 — Aprovado ou reprovado   
# Nome: Angelo Otavio Spanhol
# Objetivo: Calcular a média de três notas fornecidas pelo usuário e verificar se o aluno foi aprovado ou reprovado.

# Pedindo as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Calculando a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibindo a média das notas
print("A média das notas é:", media)

# Verificando se o aluno foi aprovado ou reprovado
# Aprovado: média maior ou igual a 7
if media >= 7:
    print("Aprovado!")
# Reprovado: média menor que 7
else:
    print("Reprovado!")