# Exercício 35 — Calculadora
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar o resultado das operações

# Pedindo para o usuário informar os números e o operador
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ")

# Identificando o operador e efetuando a conta
# Se o operador for "+": número 1 + número 2 
if operador == "+":
    print("A soma dos números foi de:", n1 + n2)
# Se o operador for "-": número 1 - número 2
elif operador == "-":
    print("A subtração dos números foi de:", n1 - n2)
# Se o operador for "*": número 1 * número 2
elif operador == "*":
    print("A multiplicação dos números foi de:", n1 * n2)
# Se o operador for "/" e o segundo número for 0: Erro de divisão
elif operador == "/":
    n2 == 0
    print("Erro: divisão por zero") 
    if operador == "/":     # Se o operador for "/": número 1 / número 2
        print("A divisão dos números doi de:", n1 / n2)
# Se o operador não for identificado: Operador inválido
else:
    print("Operador inválido")