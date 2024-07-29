'''
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

https://youtu.be/75WJIcnWfXE
'''
def showResult(resposta):
    print(f"Temos {resposta} strings \"nice\"")

#Função para verificação se a string é válida. Ela se difere nas 
#regras que a parte 2 pede, checo primeiro se o caracter após o 
#adjacente é igual o caracter atual, passando por essa verificação,
#vejo se o caracter e o subjacente repetem mais de uma vez em 
#sequência sem overlap.
def wordChecker(palavra):
    firstChecker = 0
    secondChecker = 0

    for i in range(len(palavra) - 2):
        if palavra[i] == palavra[i + 2]:
            firstChecker = 1
            break

    for i in range(len(palavra) - 1):
        if firstChecker == 0:
            return "naughty"

        substring = palavra[i] + palavra[i + 1]
        secondChecker = palavra.count(substring)
        
        if secondChecker > 1:
            return "nice"

    return "naughty"            

#Função que conta as strings válidas.
def countWords(conteudo):
    totalDePalavrasLiberadas = 0

    linhas = conteudo.splitlines()

    for linha in linhas:
        palavra = linha

        verificadorDePalavra = wordChecker(palavra)

        if verificadorDePalavra == "nice":
            totalDePalavrasLiberadas += 1

    showResult(totalDePalavrasLiberadas)

#Função para leitura do arquivo que contém as strings para realizar a 
#avaliação. Essas strings são jogadas em uma variável que vai para a função
#que conta as strings aprovadas
def readFile():
    arquivo = open("inputInst.txt", "r")
    
    conteudo = arquivo.read()
    
    arquivo.close()

    countWords(conteudo)

readFile()
