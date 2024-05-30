#!/usr/bin/python3
import re   # importa o módulo de expressões regulares
POL = {}

def sentilex(): # abre o sentilex e cria uma lista com os lemas / expressões e suas respectivas polaridades 
    with open("sentilexjj.txt") as f:
        for linha in f:
            linha = re.sub(r"ANOT=.*", "", linha)
            lista = re.split(r";",linha)
            if len(lista) == 5:
                pallemapos, flex, assina, pol, junk = lista
                pal = re.split(r",",pallemapos)[0]
                pol = int( re.sub(r"POL:N[01]=", "", pol) )
                POL[pal] = pol
            elif len(lista) == 6:
                pallemapos, flex, assina, pol1, pol2, junk = lista
                pal = re.split(r",",pallemapos)[0]
                pol1 = int( re.sub(r"POL:N[01]=", "", pol1) )
                pol2 = int( re.sub(r"POL:N[01]=", "", pol2) )
                POL[pal] = (pol1+pol2)/2 
            else:
                print(lista)
                exit()

sentilex()


def sentimento(a):  # calcula a polaridade total do texto          
    lp = re.findall(r"\w+", a)   
    ptotal = 0
    
    for p in lp:    
        if p in POL:
            ptotal = ptotal + POL[p] 

    return (ptotal, len(lp))    # retorna a polaridade final e o número total de lemas 


while True:
    x = input("digite 'c' para escrever um texto ou 't' para abrir arquivo .txt: ").lower()
    if x == "t":
        y = input("caminho: ")  # nome do arquivo.txt - devidamente inserido no mesmo diretório do código -
        z = open(y).read()
        print(sentimento(z))
        break
    elif x == "c":
        y = input("texto: ")    
        print(sentimento(y))
        break
    else:
        print("entrada inválida.")
        continue

        
