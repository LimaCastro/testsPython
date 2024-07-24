'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

https://youtu.be/XWdWWBiVdqM
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

#Função para saber as casas visitadas pelo Papai Noel, primeiro se adiciona a
#lista de CasasVisitadas a posição de origem do Papai Noel e a partir disso,
#calcular a casa onde ele entregará o próximo presente. Cada visita é 
#guardada na lista de casas
def giftDeliveryInstructions(conteudo):
    listaDeCasasVisitadas = []

    casaAtual = CasasVisitadas(0, 0)

    listaDeCasasVisitadas.append(casaAtual)

    for instrucao in conteudo:
        if instrucao == '^':
            casaAtual = CasasVisitadas(casaAtual.x, casaAtual.y + 1)

        elif instrucao == 'v':
            casaAtual = CasasVisitadas(casaAtual.x, casaAtual.y - 1)

        elif instrucao == '>':
            casaAtual = CasasVisitadas(casaAtual.x + 1, casaAtual.y)

        elif instrucao == '<':
            casaAtual = CasasVisitadas(casaAtual.x - 1, casaAtual.y)

        listaDeCasasVisitadas.append(casaAtual)

    housesWithAtLeastOneGift(listaDeCasasVisitadas)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#que será usada para saber as intruções que o Papai Noel irá seguir.
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    giftDeliveryInstructions(conteudo)    

readFile()
