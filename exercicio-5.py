# Exercício 5 — Minutos em horas   
# Nome: Angelo Otavio Spanhol
# Objetivo: Converter minutos em horas.

# Pedindo o número de minutos ao usuário
minutos = int(input("Digite o número de minutos: "))
# Convertendo minutos em horas
horas = minutos // 60
# Calculando os minutos restantes
minutos_restantes = minutos % 60

# Exibindo o resultado da conversão
print( horas, " hora (s) e ", minutos_restantes, " minuto (s).")
