# Exercício de PLL Questão 3
# Programa que ler valores da largura e altura de um retângulo e retor a área, perímetro e diagonal

def menu3():
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



