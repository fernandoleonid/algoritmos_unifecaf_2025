numero = int (input("Digite o número para fatorial: "))

contador = 1
fatorial = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1
print (f"O fatorial de {numero} é: {fatorial}")