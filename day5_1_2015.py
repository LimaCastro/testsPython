'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

https://youtu.be/3oeDh4wriW4
'''
def showResult(resposta):
    print(f"Temos {resposta} strings \"nice\"")

#Função para verificação se a string é válida.
def wordChecker(palavra):
    verificadorDeVogal = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
    verificadorDeSequenciaNaughty = palavra.count("ab") + palavra.count("cd") + palavra.count("pq") + palavra.count("xy")

    for i in range(len(palavra) - 1):
        if verificadorDeSequenciaNaughty > 0 or verificadorDeVogal < 3:
            return "naughty"

        elif palavra[i] == palavra[i + 1]:
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

