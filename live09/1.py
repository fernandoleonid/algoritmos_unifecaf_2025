import os
from colorama import init, Fore

lista_tarefas = [
    {
        "tarefa":"Estudar Python",
        "data":"31/10/2025"
    },
    {
        "data": "30/10/2025",
        "tarefa":"Correr"
    }
]

init(autoreset=True)

def limpar_tela():
    os.system("cls")

def pausar():
    input ("Aperte ENTER para continuar...")

def adicionar_tarefa():
    nova_tarefa = input ("Digite a sua nova tarefa: ")
    data_tarefa = input ("Digite a data para a Tarefa: ")

    tarefa = {
        "tarefa": nova_tarefa,
        "data": data_tarefa
    }
    lista_tarefas.append(tarefa)
    print (f"{Fore.MAGENTA}Tarefa adicionada com sucesso!!!")

def exibir_tarefas():
    for tarefa in lista_tarefas:
        print (f"{Fore.GREEN}--> {tarefa}")

def exibir_menu ():
    limpar_tela()
    print (f"{Fore.BLUE}####### MENU #######")
    print ("1 - Adicionar Tarefa")
    print ("2 - Exibir Tarefa")
    print ("3 - Remover Tarefa")
    print ("0 - Sair")
    print (f"{Fore.BLUE}#"*20)

resposta = ""
while resposta != "0":
    exibir_menu()
    resposta = input ("Escolha um opção: ")
    if ( resposta == "1"):
        limpar_tela()
        adicionar_tarefa()
        pausar()
    elif ( resposta == "2"):
        exibir_tarefas()
        pausar()
    elif ( resposta == "3"):
        exibir_tarefas()
        tarefa = input ("Digite a tarefa para excluir: ")
        lista_tarefas.remove(tarefa)
    elif ( resposta == "0"):
        print ("Saindo do sistema")
    else:
        print ("Opção invalida, tente novamente!")