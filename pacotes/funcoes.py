def lelinha (auxiliar, arquivo, aux, contador):
    for line in arquivo:
        linha = line.strip('\n') 
        linha = linha.replace("*/","/*")

        linhaux = ''
        if '//' in linha:
            barrinha = 0
            for palavra in linha:
                if palavra != '/':
                    barrinha = 0
                    linhaux = linhaux + palavra
                else:
                    barrinha = barrinha + 1
                    if barrinha == 2:
                        linhaux2 = linhaux.split()
                        auxiliar.append(linhaux2)
                        pass
        elif '/*' in linha:
            contador = contador + 1
            if linha.count('/*') == 2:
                contador = contador - 1
            del (linha)
            aux = contador%2
        elif aux == 1:
            del (linha)
        else:
            linha = linha.split()
            auxiliar.append(linha)


def includeBibli (Biblioteca, informacao):
    for palavra in Biblioteca:
     if '#define' in palavra:
        defineNome = palavra[1]
        if '"' in palavra[2]:
            tamanho = len(defineNome) + 9
            AuxiliarString = []
            AuxiliarString = ' '.join(palavra)
            AuxiliarString = AuxiliarString[tamanho:]
            defineValor = [] 
            defineValor = AuxiliarString
        else:
            defineValor = palavra[2]
        for Linha in informacao:
            for Palavra in Linha:
                if defineNome in Palavra:
                    indexLinha = informacao.index(Linha)
                    indexPalavra = informacao[indexLinha].index(Palavra)
                    informacao[indexLinha][indexPalavra] = informacao[indexLinha][indexPalavra].replace(defineNome, defineValor)

def excluidefine (auxiliar, Biblioteca):
    for Linha in Biblioteca:
        if '#define' in Linha:
            pass
        else:
            auxiliar.append(Linha)

def excluiinclude (auxiliar, Biblioteca):
    for Linha in Biblioteca:
        if '#include' in Linha:
            pass
        else:
            auxiliar.append(Linha)