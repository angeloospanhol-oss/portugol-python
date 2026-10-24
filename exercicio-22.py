# Exercício 22 	Termômetro da Serra   
# Nome: Angelo Otavio Spanhol
# Objetivo: Pedindo uma temperatura em °celsius e apresentando uma mensagem

# Pedindo a temperatura em Celsius ao usuário
temperatura = float(input("Digite a temperatura em Celsius: "))

# Verificando cada temperatura
# Se temperatura for menos que 0:
if temperatura <= 0:
    print("Abaixo de zero — risco de geada! ")
# Se temperatura for menor que 10:
elif temperatura <= 10:
    print("Muito frio — capriche no agasalho ")
# Se temperatura for menor que 18:
elif temperatura <= 18:
    print("Frio")
# Se temperatura for menor que 25:
elif temperatura <= 25:
    print("Agradável")
# Se temperatura for maior que 25:
else:
    print("Calor")



