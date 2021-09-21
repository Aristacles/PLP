def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def linha(tam=42):
    return'-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho("EXERCÍCIO DE PLP")
    print("Escolha qual programa quer acessar")
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

# Exercício de PLL Questão 1
# Programa que lê dados de 2 pessoas e mostra o nome da pessoa mais velha

def menu1():
    print("Programa que lê dados de 2 pessoas e mostra o nome da pessoa mais velha\n")
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

# Exercício de PLL Questão 2
# Programa que lê nome e salário de funcionários e faz a media do mesmo

def menu2():
    print("Programa que lê nome e salário de funcionários e faz a media do mesmo \n")
    func1 = input("Digite o nome do primeiro funcionário: ");
    sal1 = input("Informe o salário do funcionário inserido: ");
    func2 = input("Digite o nome do segundo funcionário: ");
    sal2 = input("Informe o salário do segundo funcionário: ");
    a_sal1 = float(sal1)
    a_sal2 = float(sal2)
    media = float(a_sal1 + a_sal2)/2
    print("Dados do primeiro funcionário: ");
    print("Nome: ", func1);
    print(" Salário: ", sal1);
    print(" Dados do segundo funcionário: ");
    print(" Nome: ", func2);
    print(" Salário: ", sal2);
    print("Salário médio = ", media);
    return 0

# Exercício de PLL Questão 3
# Programa que ler valores da largura e altura de um retângulo e retor a área, perímetro e diagonal
def menu3():
    print("Programa que ler valores da largura e altura de um retângulo e retorna a área, perímetro e diagonal \n")
    import math
    print("Digite a largura e altura do retângulo: ");
    largura = float(input());
    altura = float(input());

    #Calcula área
    area = largura * altura
    #Calcula perímetro
    perimetro = (largura*2)+(altura*2)
    #Calcula diagonal
    diagonal = math.sqrt(largura**2 + altura**2)
    #Saída dos valores
    print("AREA = ", area)
    print("PERÍMETRO = ", perimetro)
    print("DIAGONAL = ", diagonal)

# Exercício de PLL Questão 4
# Programa que ler dados de um funcionário e calcula porcentagens recebida
def menu4():
    print("Programa que ler dados de um funcionário e calcula porcentagens recebida \n")
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

# Exercício de PLL Questão 5
# Programa para ler dados de aluno e dizer se ta aprovado ou reprovado

def menu5():
    print("Programa para ler dados de aluno e dizer se ta aprovado ou reprovado \n")
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
