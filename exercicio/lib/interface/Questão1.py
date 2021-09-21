# Exercício de PLL Questão 1
# Programa que lê dados de 2 pessoas e mostra o nome da pessoa mais velha

def menu1():
    nome1 = input("Digite o nome da primeira pessoa ")
    idade1 = input("Digite a idade da primeira pessoa ")
    nome2 = input("Digite o nome da segunda pessoa ")
    idade2 = input("Digite idade da segunda pessoa ")
    print("Dados da primeira pessoa: \n")
    print("Nome: ", nome1)
    print("Idade: ", idade1)
    print("Dados da segunda pessoa: \n")
    print("Nome: ", nome2)
    print("Idade: ", idade2)

# Condicional para definir pessoa mais velha
    if idade1 > idade2:
        print("Pessoa mais velha: ", nome1)
    else:
        print("Pessoa mais velha: ", nome2)
    return 0
menu1()