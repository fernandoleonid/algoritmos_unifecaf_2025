senha_cadastrada = "123"

senha_digitada = input ("Digite sua senha: ")
quantidade_tentativas = 1

while senha_digitada != senha_cadastrada:
    senha_digitada = input ("Senha Incorreta, tente novamente: ")
    quantidade_tentativas += 1
    if quantidade_tentativas >= 3:
        print ("Usuário bloqueado por 5 minutos!")
        exit()

print ("Bem-vindo ao Sistema!!!")