opcao = ""

while opcao != 0:
    print ("Menu de opções:")
    print ("1 - Para Mostrar o nome da Faculdade")
    print ("2 - Para Mostrar o nome da Disciplina")
    print ("3 - Para Mostrar o nome do Aluno")
    print ("4 - Para Mostrar o situação do Aluno")
    print ("0 - Para sair do Sistema")

    opcao = input ("Digite a opção desejada: ")
    if opcao == "1":
        print ("-------------")
        print ("UniFECAF")
        print ("-------------")
    elif opcao == "2":
        print ("-------------")
        print ("Algoritmos")
        print ("-------------")
    elif opcao == "3":
        print ("-------------")
        print ("Leonid")
        print ("-------------")
    elif opcao == "4":
        print ("-------------")
        print ("Aprovado")
        print ("-------------")
    elif opcao == "0":
        print ("-------------")
        print ("Saindo do sistema X...")
        print ("-------------")
        exit()
    else:
        print ("-------------")
        print ("Opção inválida, tente novamente...")
        print ("-------------")