# Exercício 28 — Vogal ou consoante
# Nome: Angelo Otavio Spanhol
# Objetivo: Identificar se a letra é vogal ou consoante

# Pedindo para o usuário digitar a letra
letra = input("Digite uma letra minúscula: ")

# Analizando se a letra é vogal ou consoante
# Se a letra for "a" "e" "i" "o" "u" é vogal
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Letra", letra, "é uma vogal")
# Se não for uma vogal letra é consoante
else:
    print("Letra", letra, "é uma consoante")