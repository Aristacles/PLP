# Exercício de PLL Questão 5
# Programa para ler dados de aluno e dizer se ta aprovado ou reprovado

def menu5():
    nome = input("Digite nome do aluno ")
    print("Nome do Aluno: ", nome)
    print("Digite as três notas do aluno: ")
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    notafinal: float = nota1+nota2+nota3
    print("NOTA FINAL = ", notafinal)
    reprovado: float = - notafinal + 60
    repro= str(reprovado)

#Condicional para saber se foi aprovado. Nota min 60 pts
    if notafinal < 60:
        print("REPROVADO \n" "FALTARAM " +repro+" PONTOS")
    else:
        print("APROVADO")