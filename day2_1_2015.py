'''
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

https://youtu.be/mvi5hD0gCDs
'''
def showResult(resposta):
    print(f"Os elfos precisarão de {resposta} pés quadrados de papel de embrulho")

#Função para calcular a menor área considerando as faces do presente.
def calculateSmallestAreaOfFaceOfRectangle(comprimento, largura, altura):
    menorValor = comprimento * largura

    if (menorValor <= comprimento * altura) and (menorValor <= largura * altura):
        return menorValor

    elif (comprimento * altura <= menorValor) and (comprimento * altura <= largura * altura):
            menorValor = comprimento * altura
            return menorValor

    else:
        menorValor = largura * altura
        return menorValor

#Função para calcular a quantidade de papel de embrulho necessária, como cada
#linha é um presente lemos linha a linha(presente a presente) a string e como
#os valores são strings realizamos uma conversão para int e chamamos a função
#para o cálculo da menor área considerando as faces do presente, que é
#necessário para o cálculo da área
def calculateWrappingPaper(conteudo):
    totalDePapelDeEmbrulho = 0

    linhas = conteudo.splitlines()
    
    for linha in linhas:
        valores = linha.split()
        comprimento, largura, altura = map(int, valores)

        menorAreaDaFaceDoPresente = calculateSmallestAreaOfFaceOfRectangle(comprimento, largura, altura)

        totalDePapelDeEmbrulho += ((2 * comprimento * largura) + (2 * comprimento * altura) + (2 * largura * altura) + menorAreaDaFaceDoPresente)

    showResult(totalDePapelDeEmbrulho)

#Função para formatar a string em uma que o caracter 'x' não apareça mais e o
#separador seja o espaço em branco
def formatTheInstructions(conteudo):
    removerCaracter = 'x'

    conteudo = conteudo.replace(removerCaracter, ' ')
    
    calculateWrappingPaper(conteudo)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#que será usada para saber a quantidade de papel de embrulho necessária ao 
#Papai Noel. 
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    formatTheInstructions(conteudo)

readFile()
