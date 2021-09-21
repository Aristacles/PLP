from time import sleep
from exercicio.lib.interface import *
while True:
    resposta = menu(['Questão 1','Questão 2','Questão 3','Questão 4','Questão 5','Sair do Programa'])
    if resposta == 1:
        cabeçalho("Abrindo exercício 1")
        menu1()
    elif resposta == 2:
        cabeçalho("Abrindo exercício 2")
        menu2()
    elif resposta == 3:
        cabeçalho("Abrindo exercício 3")
        menu3()
    elif resposta == 4:
        cabeçalho("Abrindo exercício 4")
        menu4()
    elif resposta == 5:
        cabeçalho("Abrindo exercício 5")
        menu5()
    elif resposta == 6:
        cabeçalho("Saindo do Programa")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida! \033[m")
    sleep(2)


