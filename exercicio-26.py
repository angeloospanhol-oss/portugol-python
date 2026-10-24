# Exercício 26 — Desconto progressivo
# Nome: Angelo Otavio Spanhol
# Objetivo: Informar a quantidade de desconto de um produto

# Pedindo para o usuario informar o valor da compra
valorCompra = float(input("Digite o valor da sua compra: "))

# Verificando se há desconto na compra
# Se o valor da compra for menor 50 sem desconto
if valorCompra <= 50:
    print("Sem desconto")
    print("Valor final: R$", valorCompra)
# Se o valor da compra estiver entre 100 e 50 desconto de 5%
elif valorCompra <= 100:
    desconto = valorCompra * 0.05   # Calculo do desconto de 5%
    print("Desconto de: R$", desconto)
    print("Valor final: R$", valorCompra - desconto)
# Se o valor da compra estiver entre 200 e 100 desconto de 10%
elif valorCompra <= 200:
    desconto = valorCompra * 0.10   # Calculo do desconto de 10%
    print("Desconto de: R$", desconto)
    print("Valor final: R$", valorCompra - desconto)
# Se o valor da compra for maior que 200 desconto de 15%
else:
    desconto = valorCompra * 0.15   # Calculo do desconto de 15%
    print("Desconto de: R$", desconto)
    print("Valor final: R$", valorCompra - desconto)