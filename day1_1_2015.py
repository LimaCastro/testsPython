'''
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

https://youtu.be/I1iY-gsyg20
'''
def showResult(andarAtual):
    print(f"O papai Noel se encontra no andar {andarAtual}")

#Função que localiza onde o conjunto de instruções levou o papai Noel, tendo 
#em vista que "(" significa subir um andar e ")" significa descer um andar,
#se somamos tudo as instruções de subida e tirar o número de instruções de 
#descida, temos o andar atual.
def floorIndicator(conteudo):
    instrucoesPositivas = conteudo.count('(')
    instrucoesNegativas = conteudo.count(')')

    andarAtual = instrucoesPositivas - instrucoesNegativas
    
    showResult(andarAtual)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#e passar essa variável para a função que irá determinar o andar em que o
#papai Noel se encontra 
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    floorIndicator(conteudo)

readFile()

