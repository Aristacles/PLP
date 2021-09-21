# Exercício de PLL Questão 4
#Programa que ler dados de um funcionário e calcula porcentagens recebida
def menu4():
    nome = input("Digite o nome do funcionário ")
    salario = float(input("Digite salário bruto "))
    imposto = float(input("Digite valor do imposto "))
    funcionario = salario - imposto
    print("Nome: ", nome)
    print("Salário bruto: ", salario)
    print("Imposto: ", imposto)
    print("Funcionário: ", nome + ", R$ ", funcionario)
    porcentagem = float(input("Digite a porcentagem para aumentar o salário: "))
    atual = funcionario + ((funcionario/100)*porcentagem)
    print("Dados atualizados: ", nome + ", R$ ", atual)
