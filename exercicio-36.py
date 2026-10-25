# Exercício 36 — Pedra, papel e tesoura
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar um ganhdor no pedra, peapel e tesoura

# Pedindo para o usuário digitar as joagadas
j1 = input("Jogador um digite sua jogada: ")
j2 = input("Jogador dois digite sua jogada: ")

# Verificando com o comando "not in" se as jogadas são verdadeiras
if j1 not in ["pedra", "papel", "tesoura"] or j2 not in ["pedra", "papel", "tesoura"]:     # Se o j1 ou j2 não digitar pedra, papel ou tesoura da erro
    print("Jogada inválida")
# Se jogador 1 digitar pedra ele vence
elif j1 == "pedra" and j2 == "tesoura":
    print("Jogador 1 venceu!")
# Se jogador 1 digitar papel ele vence
elif j1 == "papel" and j2 == "pedra":
    print("Jogador 1 venceu!")
# Se jogador 1 digitar tesoura ele vence
elif j1 == "tesoura" and j2 == "papel":
    print("Jogador 1 venceu!")
# Se jogador 1 e jogador 2 digitarem a mesma jogada: empate
elif j1 == j2:
    print("Empate!")
# Senão jogador 2 vence
else:
    print("Jogador 2 venceu!")