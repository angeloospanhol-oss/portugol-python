# Exercício 34 — Aprovação com frequência
# Nome: Angelo Otavio Spanhol
# Objetivo: Verificar se o aluno passou de acorco com as notas e faltas

# Pedindo para o usuário digitar as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculo da média
media = (nota1 + nota2 + nota3) / 3

# Pedindo para o usuário digitar a frequência de aulas
frequencia = int(input("Digite a frequência de aulas frequentadas: "))

# Identificando se o aluno foi aprovado ou não
# Se o aluno foi aprovado frequência e notas boas
if media >= 7 and frequencia >= 75:
    print("Aprovado")
# Se o aluno reprovou por faltas
elif media >= 7 and frequencia < 75:
    print("Reprovado por falta")
# Se o aluno reprovou por notas
elif media < 7 and frequencia >= 75:
    print("Reprovado por nota")
# Se reprovou por notas e frequência
else:
    print("Reprovado por nota e frequência")