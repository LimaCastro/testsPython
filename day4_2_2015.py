'''
--- Part Two ---
Now find one that starts with six zeroes.

https://youtu.be/47bJ1m4S28E
'''
from hashlib import md5

def showResult(resposta):
    print(f"O menor número acompanhado com a chave secreta que gera um hash que se inicia em \"000000\" é {resposta}")

#função que calcula o md5 da chaveSecreta
def calculate_md5(chaveSecreta):
    return md5(chaveSecreta.encode()).hexdigest()

#Função para checar o menor número que gera o prefixo 000000 junto com a
#chave secreta, foi realizado um strip() no conteudo porque ele estava com 
#uma quebra de linha e estava gerando uma chaveSecreta diferente da esperada.
def prefixChecker(conteudo):
    menorNumGerarPrefixo = 0
    prefixoEncontrado = False
    prefixoDesejado = "000000"
    contadorDeIteracoes = 0

    while not prefixoEncontrado:
        chaveSecreta = conteudo.strip() + str(contadorDeIteracoes)
        hashChaveSecreta = calculate_md5(chaveSecreta)

        if hashChaveSecreta.startswith(prefixoDesejado):
            menorNumGerarPrefixo = contadorDeIteracoes
            prefixoEncontrado = True

        contadorDeIteracoes += 1

    showResult(menorNumGerarPrefixo)    

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#que é a chave secreta que devemos calcular o md5
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    prefixChecker(conteudo)

readFile()

