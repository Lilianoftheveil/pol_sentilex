#!/usr/bin/python3
import re  
POL = {}

def sentilex(): 
    with open("sentilex.txt") as f:
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


def sentimento(a):         #total
    lp = re.findall(r"\w+", a)   
    ptotal = 0  # total
    totalp = 0  # positivo
    totaln = 0  # negativo
    totalo = 0  # neutro

    total_pol = 0

    for p in lp:    #total
        if p in POL:
            ptotal = ptotal + POL[p]
            total_pol = total_pol + 1

    for p in lp:    # positivo
        if p in POL:
            if POL[p] == 1 or POL[p] == 0.5:
                totalp = totalp + 1

    for p in lp:    # negativo
        if p in POL:
            if POL[p] == -1 or POL[p] == -0.5:
                totaln = totaln + 1

    for p in lp:    # neutro
        if p in POL:
            if POL[p] == 0 or POL[p] == 0.0:
                totalo = totalo + 1

    if ptotal < 0:
        ptotal = "Negativo"
    elif ptotal == 0 or ptotal ==0.0:
        ptotal = "Neutro"
    elif ptotal > 0:
        ptotal = "Positivo"
    
    return (f"Sentimento Geral: {ptotal}", f"Positivo: {int(round(totalp / total_pol, 2)* 100)}%", f"Neutro: {int(round(totalo / total_pol, 2)* 100)}%", f"Negativo: { int(round(totaln / total_pol, 2)* 100)}%")     


while True:
    x = input("digite 'c' para escrever um texto ou 't' para abrir arquivo .txt: ").lower()
    if x == "t":
        y = input("caminho: ")  
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