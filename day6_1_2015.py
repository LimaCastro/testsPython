'''
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

https://youtu.be/GS-666L0VLE
'''
import numpy as np

def showResult(resposta):
    print(f"{resposta} luzes acesas")

#conta a quantidade de luzes acesas
def countLightsUp(gridDeLuzes):
    luzesAcesas = np.sum(gridDeLuzes)
    showResult(luzesAcesas)

#função para mudar o estado das luzes no grid de luz
def setLights(gridDeLuzes, comando, xInicial, yInicial, xFinal, yFinal):
    for i in range(xInicial, xFinal + 1):
        for j in range(yInicial, yFinal + 1):
            if comando == "turn on":
                gridDeLuzes[i][j] = 1

            elif comando == "turn off":
                gridDeLuzes[i][j] = 0

            elif comando == "toggle":
                gridDeLuzes[i][j] = 1 - gridDeLuzes[i][j]

#função para processar as instruções
def processInstruction(conteudo):
    gridDeLuzes = np.zeros((1000, 1000), dtype=int)
    linhas = conteudo.splitlines()

    for instrucao in linhas:
        if "turn on" in instrucao:
            comando = "turn on"
            instrucao = instrucao.replace("turn on ", "")

        elif "turn off" in instrucao:
            comando = "turn off"
            instrucao = instrucao.replace("turn off ", "")

        elif "toggle" in instrucao:
            comando = "toggle"
            instrucao = instrucao.replace("toggle ", "")

        partes = instrucao.split(" through ")
        xInicial, yInicial = map(int, partes[0].split(","))
        xFinal, yFinal = map(int, partes[1].split(","))

        setLights(gridDeLuzes, comando, xInicial, yInicial, xFinal, yFinal)

    countLightsUp(gridDeLuzes)

#leitura do arquivo de instrução
def readFile():
    arquivo = open("inputInst.txt", "r")
    
    conteudo = arquivo.read()
    
    arquivo.close()

    processInstruction(conteudo)

readFile()
