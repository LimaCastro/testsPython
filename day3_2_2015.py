'''
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

https://youtu.be/yxzHzspf3RU
'''
from coordenadas import CasasVisitadas

def showResult(resposta):
    print(f"O Papai Noel visitou {resposta} casas")

#Função para separar a lista de casa em somente casa de posições distintas,
#para se saber a quantia de casas visitadas pelo Papai Noel.
def housesWithAtLeastOneGift(listaDeCasasVisitadas):
    listaDeCasasUnicas = set((c.x, c.y) for c in listaDeCasasVisitadas)

    quantidadeDeCasasVisitadas = len(listaDeCasasUnicas)

    showResult(quantidadeDeCasasVisitadas)

#Função para saber as casas visitadas pelo Papai Noel e seu auxiliar robô,
#temos um vetor onde cada posição significa um entregador, a posição 0 é o
#Papai Noel e a posição 1 é seu auxiliar robô. Para sabemos quem seguirá 
#tal instrução temos uma flag que é o verificadorDeEntregador que muda com
#base no contadorDeInstrução % 2
def giftDeliveryInstructions(conteudo):
    listaDeCasasVisitadas = []
    contadorDeInstrucao = 0
    verificadorDeEntregador = 0
    casaAtual = []

    casaAtual.append(CasasVisitadas(0, 0))
    casaAtual.append(CasasVisitadas(0, 0))

    listaDeCasasVisitadas.append(casaAtual[0])
    listaDeCasasVisitadas.append(casaAtual[1])

    for instrucao in conteudo:
        verificadorDeEntregador = contadorDeInstrucao % 2

        if instrucao == '^':
            casaAtual[verificadorDeEntregador] = CasasVisitadas(casaAtual[verificadorDeEntregador].x, casaAtual[verificadorDeEntregador].y + 1)

        elif instrucao == 'v':
            casaAtual[verificadorDeEntregador] = CasasVisitadas(casaAtual[verificadorDeEntregador].x, casaAtual[verificadorDeEntregador].y - 1)

        elif instrucao == '>':
            casaAtual[verificadorDeEntregador] = CasasVisitadas(casaAtual[verificadorDeEntregador].x + 1, casaAtual[verificadorDeEntregador].y)

        elif instrucao == '<':
            casaAtual[verificadorDeEntregador] = CasasVisitadas(casaAtual[verificadorDeEntregador].x - 1, casaAtual[verificadorDeEntregador].y)

        listaDeCasasVisitadas.append(casaAtual[verificadorDeEntregador])


        contadorDeInstrucao += 1

    housesWithAtLeastOneGift(listaDeCasasVisitadas)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#que será usada para saber as intruções que o Papai Noel irá seguir.
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    giftDeliveryInstructions(conteudo)    

readFile()
