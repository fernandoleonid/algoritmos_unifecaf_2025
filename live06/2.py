resposta = input("Você deseja converter dólar para real? (s/n) ")
if resposta == 's':
    dolar = int(input("Digite o valor em dólar: "))
    cotacao = int(input("Digite a cotação do dólar: "))
    real = dolar * cotacao
    print (f"O valor em real é: {real}")
else:
    real = int(input("Digite o valor em real: "))
    cotacao = int(input("Digite a cotação do dólar: "))
    dolar = real / cotacao
    print (f"O valor em dólar é: {dolar}")