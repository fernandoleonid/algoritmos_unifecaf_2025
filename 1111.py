senha_cadastrada = "123"

senha_digitada = input("Digite sua senha: ") 
quantidade_tentativas = 1

while senha_digitada != senha_cadastrada:
    senha_digitada = input("Senha incorreta, tente novamente: ")
    quantidade_tentativas += 1
    if quantidade_tentativas >= 3:
        print("Número máximo de tentativas excedido. Acesso bloqueado.")
        break

print("Seja bem vindo a calculadora.")

opcao = ""
while opcao != 0:
    print ("Menu de Opções! digite a operação desejada:")
    print ("1 - Adição")
    print ("2 - Sobtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Sair do Programa")

    opcao = input ("Digite a opção desejada: ")
    if opcao == "1":
            print ("----------")
            print (int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))
            print ("----------")
    elif opcao == "2":
            print ("----------")
            print (int(input("Digite o primeiro número: ")) - int(input("Digite o segundo número: ")))
            print ("----------")
    elif opcao == "3":
            print ("----------")
            print (int(input("Digite o primeiro número: ")) * int(input("Digite o segundo número: ")))
            print ("----------")
    elif opcao == "4":
            print ("----------")
            print (int(input("Digite o primeiro número: ")) / int(input("Digite o segundo número: ")))
            print ("----------")
    elif opcao == "5":
            print("Saindo do programa...")
            exit() 