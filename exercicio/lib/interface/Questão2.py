# Exercício de PLL Questão 2
# Programa que lê nome e salário de funcionários e faz a media do mesmo

def menu2():
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
