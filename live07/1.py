# Estruturas de dados
# Listas
# -> Ordenadas
# -> Mutáveis
# -> Heterogênias
# -> Tamanho flexivel
# -> Indexadas

clientes = ["Ana", "Hugo", "Maria", "Felipe","Pedro"]
idades = [12, 43, 32, 45, 90, 2]

# contador = 0
# limite = len(clientes)
# while contador < limite:    
#     print (f"O nome do cliente é: {clientes[contador]}")
#     contador += 1

clientes[1] = "Fernando Leonid"

for cliente in clientes:
    print (f"O nome do cliente é: {cliente}")