alunos = [
    {"nome": "Ana", "nota": 4},
    {"nome": "Maria", "nota": 10}, 
    {"nome": "Hugo", "nota": 0},
    {"nome": "Marcos", "nota": 5}
]

for aluno in alunos:
    if aluno["nota"] >= 5:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print (f"{aluno["nome"]} está {situacao}")