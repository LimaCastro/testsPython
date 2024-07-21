'''
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?

https://youtu.be/p03BWB5SN4M
'''
def showResult(resposta):
    print(f"O Papai Noel entrou no subsolo na instrução {resposta}")

#função para determinar o número da instrução que levará o Papai Noel ao 
#subsolo. Tem a variável instrucaoParaSubSolo que serve para guardar a
#instrução que leva o Papai Noel ao subsolo, ela se inicia em 1 e a cada
#instrução nova lida incrementa 1 a essa variável. A outra variável é a 
#andarAtual, que serve para determinar o andarAtual que o Papai Noel se 
#encontra, caso o andarAtual for -1 a um break no laço. O laço lê
#instrução a instrução da lista de instruções.
def basementIndicator(conteudo):
    instrucaoParaSubSolo = 1
    andarAtual = 0

    for instrucao in conteudo:
        if instrucao == ')':
            andarAtual -= 1
        else:
            andarAtual += 1

        if andarAtual == -1:
            break
        
        instrucaoParaSubSolo += 1

    showResult(instrucaoParaSubSolo)

#Essa função serve para armazenar todo o conteúdo do arquivo em uma variável
#e passar essa variável para a função que irá determinar a instrução em que o
#papai Noel entra no subsolo
def readFile():
    arquivo = open("inputInst.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    basementIndicator(conteudo)

readFile()
