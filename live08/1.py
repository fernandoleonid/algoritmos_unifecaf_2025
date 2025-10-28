banco_dados = [
    {
        "ra":"123",
        "nome": "Fernando Leonid",
        "notas": [5, 7, 9],
        "email": "fernandoleonid@gmail.com"
    }
]

def mostrar_menu():
    print ("#"*30)
    print ("1 - Mostrar nome Aluno")
    print ("2 - Mostrar a notas do Aluno")
    print ("3 - Mostrar situação do Aluno")
    print ("0 - Sair do Sistema")
    print ("#"*30)

def mostrar_nome ():
    print ("Aluno: Fernando Leonid")


resposta = ""
while resposta != 0:
    mostrar_menu()
    resposta = int(input("Digite uma opção: "))
    if ( resposta == 1):
        mostrar_nome()
    elif ( resposta == 2):
        print ("Mostrando as notas do Aluno...")
    elif ( resposta == 3):
        print ("Mostrando a situação do Aluno...")
    elif ( resposta == 0):
        print ("Saindo do Sistema...")
    else:
        print ("Opção errada, tente novamente!")