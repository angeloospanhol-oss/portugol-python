# Exercício 23 — Cardápio da cantina   
# Nome: Angelo Otavio Spanhol
# Objetivo: Apresentar os produtos ao usuario pedir a quantidade e informar o preço

# Calendario dos produtos
print("===============Calendario===============")
print("Código 	   Produto        	Preço (R$)")
print("  1     Pão de queijo              4,50")
print("  2        Coxinha                 6,00")
print("  3        Pastel                  7,00")
print("  4         Suco                   5,00")
print("  5         Café                   3,00")

# Pedindo ao cliente o código do produto
codigo = int(input("Digite o código do produto: "))

# Informando o que cada código do produto esta relacionado
# Se código for 1 produto pão de queijo e preço 4,50
if codigo == 1:
    preco = float(4.50)
    print("\nProduto escolhido foi o pão de queijo")
    print("R$4,50")
# Se código for 2 produto coxinha e preço 6,00
elif codigo == 2:
    preco = float(6.00)
    print("\nProduto escolhido foi a coxinha")
    print("R$6,00")
# Se código for 3 produto pastel e preço 7,00
elif codigo == 3:
    preco = float(7.00)
    print("\nProduto escolhido foi o pastel")
    print("R$7,00")
# Se código for 4 produto suco e preço 5,00
elif codigo == 4:
    preco = float(5.00)
    print("\nProduto escolhido foi o suco")
    print("R$5,00")
# Se código for 5 produto café e preço 3,00
elif codigo == 5:
    preco = float(3.00)
    print("\nProduto escolhido foi o café")
    print("R$3,00")
# Se código não existir aparece código não encontrado
else:
    print("\nCódigo não encontrado")

# pedindo para o usuario digitar a quantidade
quantidade = int(input("\nDigite a quantidade desejada: "))

# Apresentando o total a pagar
print("Total a pagar foi de R$", preco * quantidade)