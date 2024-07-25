'''
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

https://youtu.be/D60K8BU6lsY
'''
from hashlib import md5

def showResult(resposta):
    print(f"O menor número acompanhado com a chave secreta que gera um hash que se inicia em \"00000\" é {resposta}")

#função que calcula o md5 da chaveSecreta
def calculate_md5(chaveSecreta):
    return md5(chaveSecreta.encode()).hexdigest()

#Função para checar o menor número que gera o prefixo 00000 junto com a chave
#secreta, foi realizado um strip() no conteudo porque ele estava com uma 
#quebra de linha e estava gerando uma chaveSecreta diferente da esperada.
def prefixChecker(conteudo):
    menorNumGerarPrefixo = 0
    prefixoEncontrado = False
    prefixoDesejado = "00000"
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

