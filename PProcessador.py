from os import system
import sys
from pacotes.funcoes import *


informacao = []
nomeArquivo = []
linha = []
nomeArquivo = (input('Digite o nome do arquivo a ser processado : '))
try:
    arquivo = open(nomeArquivo + '.c', mode='r', encoding="utf-8")
except IOError:
    print('O arquivo não pôde ser aberto')

contador = 0
aux = 0

lelinha(informacao, arquivo, aux, contador)

arquivo.close()

nomeBiblioteca = []
for linha in informacao:
    if '#include' in linha:
        nomeBiblioteca = linha[1]
        nomeBiblioteca = nomeBiblioteca.strip('"')
        try:
            arquivoB = open(nomeBiblioteca, mode='r', encoding="utf-8")
        except IOError:
            print('O arquivo não pôde ser aberto')
        Biblioteca = []
        lelinha(Biblioteca, arquivoB, aux, contador)

arquivoB.close()

includeBibli(Biblioteca, informacao)

BibliotecaMod = []
excluidefine(BibliotecaMod, Biblioteca)

auxiliar = []
for bloco in BibliotecaMod:
    ajuda = ', '.join(bloco)
    auxiliar.append(ajuda)

cont = 0
for linha in informacao:
    if '#include' in linha:
        informacao[cont] = auxiliar
    cont += 1

includeBibli(informacao, informacao)

Resultado = []
excluidefine(Resultado, informacao)


aux2 = []
for linha in Resultado:
    ajuda = ', '.join(linha)
    aux2.append(ajuda)

Result = ', '.join(aux2)

Result = Result.replace(", ","")

with open(nomeArquivo+'Pronto.c', 'w') as output:
    output.write(Result)
    output.close()
