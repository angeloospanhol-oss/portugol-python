# Exercício 15 	Desconto na compra  
# Nome: Angelo Otavio Spanhol
# Objetivo: Calcular o valor total a pagar de uma compra, aplicando um desconto de 10% para compras acima de R$100,00.

# Pedindo o valor da compra ao usuário
valor = float(input("Digite o valor da compra: R$"))

# Verificando se o valor da compra é maior ou igual a R$100,00
# Aplicando desconto de 10% para compras acima de R$100,00
if valor >= 100:
    print("O valor com desconto é: R$", valor * 0.10)
    print("O valor total a pagar é: R$", valor - (valor * 0.10))
# Caso o valor da compra seja menor que R$100,00
else:
    print("O valor total a pagar é: R$", valor)