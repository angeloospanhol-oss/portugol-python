# Exercício 40 — Bilheteria da Festa do Pinhão (desafio final)
# Nome: Angelo Otavio Spanhol
# Objetivo: Sistema de ingresso da festa do pinhão

# Pedindo para o usuário digitar a idade
idade = int(input("Digite sua idade: "))

# Identificando a idade do usuário e identificando tipo de ingresso
# Se a idade for menor que seis anos: Pagamento R$0
if idade <= 6:
    print("\nGratuito — R$ 0.0")
    entrada = 0
# Se a idade não for menor que seis:
else:
    # Se a idade estiver entre 7 e 17 ou maior que 60 anos: Meia entrada
    if idade <= 17 or idade >= 60:
        print("\nMeia-entrada (R$ 20.00)")
        ingresso = "meia-entrada"
        entrada = 20
    # Se a idade estiver entre 18 e 59 anos: Entrada inteira
    else:
        print("\nInteira (R$ 40.00)")
        ingresso = "entrada-inteira"
        entrada = 40

# Se a entra for diferente de R$0: Prossegue a transação
if entrada != 0:
    print("\n1 = PIX (5% de desconto)")
    print("2 = Débito (sem alteração)")
    print("3 = Crédito(5% de acréscimo)")
    # Pedindo a forma de pagamento para o usuário
    pagamento = int(input("Digite a forma de pagamento: "))

    # Se a forma de pagamento for PIX: Desconto de 5%
    if pagamento == 1:
        desconto = entrada * 0.05
        entrada = entrada - desconto
        formaPagamento = "PIX"
    # Se a forma de pagamento for débito: Sem desconto
    elif pagamento == 2:
        desconto = 0
        formaPagamento = "Débito"
    # Se a forma de pagamento for crédito: acréscimo de 5%
    elif pagamento == 3:
        acrescimo = entrada * 0.05
        entrada = entrada + acrescimo
        formaPagamento = "Crédito"
    # Senão: forma de pagamento invalida
    else:
        print("Forma de pagamento inválida")

    # Informações finais
    print("Tipo de ingresso:", ingresso)
    print("Forma de pagamento:", formaPagamento)
    print("Valor final da entrada: ", entrada)