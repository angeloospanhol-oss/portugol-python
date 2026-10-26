# Exercício 38 — Equação do 2º grau
# Nome: Angelo Otavio Spanhol
# Objetivo: Resolver uma ecuação do 2° utilizando bhaskara

# Pedindo para o usuário digitar os números
a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

# Se "a" for 0: não é uma ecuação do 2° grau
if a == 0:
    print("Não é uma equação do 2º grau.")

# Declarando o delta
delta = (b * b - 4) * a * c

# Se delta for menor que 0: não existem raízes reais
if delta < 0:
    print("Não existem raízes reais.")
# Se delta igual a 0: existe apenas uma raíz
elif delta == 0:
    x = -b * (2 * a)
    print("existe uma raiz:", x)
# Se delta for maior que 0 formula normal
else:
    import math     # Importando o "math" para poder efetuar a raíz quadrada

    x1 = (-b + math.sqrt(delta)) / (2 * a)      # math.sqrt igual a raíz
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"x1 = {x1:.2f}... e x2 = {x2:.2f}...")