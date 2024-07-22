'''
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?

https://youtu.be/TovPse42g3M
'''
def showResult(resposta):
    print(f"Os elfos precisarão de {resposta} pés de fita")

#Função que retorna o menor perímetro considerando as faces do presente
def calculateSmallestPerimeterOfFaceOfRectangle(comprimento, largura, altura):
    menorValor = comprimento + largura

    if (menorValor <= comprimento + altura) and (menorValor <= largura + altura):
        return menorValor

    elif (comprimento + altura <= menorValor) and (comprimento + altura <= largura + altura):
        menorValor = comprimento + altura
        return menorValor

    else:
        menorValor = largura + altura
        return menorValor

#Função para calcular a quantidade de fita que os elfos necessitarão, a uma 
#chamada para função que calcula o menor perímetro considerando as faces do 
#presente, que é necessário para o cálculo.
def calculateRibbon(conteudo):
    totalDeFita = 0

    linhas = conteudo.splitlines()

    for linha in linhas:
        valores = linha.split()
        comprimento, largura, altura = map(int, valores)

        menorPerimetroDaFaceDoPresente = calculateSmallestPerimeterOfFaceOfRectangle(comprimento, largura, altura)

        totalDeFita += (comprimento * largura * altura) + (2 * menorPerimetroDaFaceDoPresente)

    showResult(totalDeFita)

#Função para formatar a string em uma que o caracter 'x' não apareça mais e o
#separador seja o espaço em branco
def formatTheInstructions(conteudo):
    removerCaracter = 'x'

    conteudo = conteudo.replace(removerCaracter, ' ')
    
    calculateRibbon(conteudo)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#que será usada para saber a quantidade de papel de embrulho necessária ao 
#Papai Noel. 
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    formatTheInstructions(conteudo)

readFile()
