# Exercício 19 — Situação do aluno 
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o aluno está reprovado, aprovado ou me recuperação de acordo com a média

# Pedindo as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calculando a média das notas
media = (nota1 + nota2) / 2

# Exibindo a média das notas e a situação do aluno
# Se média for maior ou igual a 7, o aluno está aprovado
if media >= 7:
    print(media, "Aprovado")
# Se média for menor ou igual a 5, o aluno está reprovado
elif media <= 5:
    print(media, "Reprovado")
# Se média for maior que 5 e menor que 7, o aluno está em recuperação
else:
    print(media, "Recuperação")