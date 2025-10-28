import os
from aluno import *

def limpar_tela():
    os.system('cls')

def pausar():
    input ("Digite ENTER para continuar...")

def mostrar_menu():
    print ("#"*30)
    print ("1 - Mostrar nome Aluno")
    print ("2 - Mostrar a notas do Aluno")
    print ("3 - Mostrar situação do Aluno")
    print ("0 - Sair do Sistema")
    print ("#"*30)


resposta = ""
while resposta != 0:
    mostrar_menu()
    resposta = int(input("Digite uma opção: "))
    if ( resposta == 1):
        limpar_tela()
        mostrar_nome()
        pausar()
    elif ( resposta == 2):
        limpar_tela()
        mostrar_notas()
        pausar()
    elif ( resposta == 3):
        limpar_tela()
        mostrar_situacao()
        pausar()
    elif ( resposta == 0):
        print ("Saindo do Sistema...")
    else:
        print ("Opção errada, tente novamente!")