banco_dados = [
    {
        "ra":"123",
        "nome": "Fernando Leonid",
        "notas": [5, 1, 7],
        "email": "fernandoleonid@gmail.com"
    },
    {
        "ra":"432",
        "nome": "Ana Maria",
        "notas": [10, 3, 8],
        "email": "anamaria@gmail.com"
    }
]

def mostrar_nome ():
    print (banco_dados[0]["nome"])

def mostrar_notas ():
    for nota in banco_dados[0]["notas"]:
        print (f"{nota:.1f}")

def mostrar_situacao():
    soma = 0
    for nota in banco_dados[0]["notas"]:
        soma += nota
    media = soma / 3
    if (media >= 5):
        print (f"A média do Aluno é {media:.1f} e está Aprovado!")
    else:
        print (f"A média do Aluno é {media:.1f} e está Reprovado!")
