# Exercício 6 — Compra na cantina 
# Nome: Angelo Otavio Spanhol
# Objetivo: Calcular o valor total de uma compra na cantina.

# Informando o valor do pastel
pastel = float(4.50)
# Exibindo o valor do pastel
print("O valor do pastel é: R$", pastel)

# Pedindo o valor em dinheiro que o usuário possui
dinheiro = float(input("Digite o valor em dinheiro que você possui: R$"))

# Pedindo a quantidade de pastéis ao usuário
quantidade = int(input("Digite a quantidade de pastéis que deseja comprar: "))

# Calculando o valor total da compra
total = pastel * quantidade
# Exibindo o valor total da compra
print("Total R$", total)

# Exibindo o troco do usuário
print("Troco: R$", dinheiro - total)