import os
import TIAi
import TIAg

saludo = lambda nm: "Hola, " + nm
encantado = lambda nm: "Encantado, " + nm

def getTipePhrase(count):
    if count == 1:
        return oneW
    elif count == 2:
        return twoW
    elif count == 3:
        return threeW
    elif count == 4:
        return fourW
    else:
        return moreW

class oneW:
    def __init__(self,words):
        self.word = words[0]
    def sintax(self):
        if self.word == "hola":
            TIAg.decir(saludo(TIAi.info["name"]))
        elif self.word in TIAi.saves:
            TIAg.decir(TIAi.saves[self.word])
        elif self.word == "recita":
            TIAg.decir(TIAg.readtext())

class twoW:
    def __init__(self,words):
        self.words = words
    def sintax(self):
        if self.words[0] == "soy":
            TIAi.info["name"] = self.words[1]
            TIAg.decir(encantado(TIAi.info["name"]))
        elif self.words[0] == "anclado":
            TIAi.handlers[self.words[1]]()
        elif self.words[0] == "mostrar":
            print Sintax(self.words[1])
        elif self.words[0] == "instalar" and self.words[1] == "paquetes":
            if TIAi.isPIPInstall():
                TIAi.installPackages(TIAg.readtext().split(","))
        elif self.words[0] == "decir":
            if self.words[1] == "mi nombre":
                TIAg.decir(TIAi.info["name"])
            else:
                TIAg.decir(Sintax(self.words[1]))

class threeW:
    def __init__(self,words):
        self.words = words
    def sintax(self):
        if self.words[0] == "repetir" and self.words[2] == "veces":
            toasay = TIAg.readtext()
            for x in range(0,int(self.words[1])):
                TIAg.decir(toasay)
        if self.words[0] == "ejecutar":
            if self.words[1] == "comando":
                os.system(self.words[2])

class fourW:
    def __init__(self,words):
        self.words = words
    def sintax(self):
        if self.words[0] == "anclar" and self.words[2] == "a":
            exec "TIAi.handlers[self.words[3]] = " + self.words[1]
        elif self.words[0] == "guardar" and self.words[2] == "como":
            TIAi.saves[self.words[3]] = self.words[1]
        elif self.words[0] == "guardar" and self.words[1] == "archivo" and self.words[2] == "en":
            TIAi.saves[self.words[3]] = TIAg.leerarchivo()
        elif self.words[0] == "registrar" and self.words[1] == "texto" and self.words[2] == "como":
            TIAi.saves[self.words[3]] = TIAg.readtext()

class moreW:
    def __init__(self,words):
        self.words = words
    def sintax(self):
        pass

def Sintax(word):
    for d in TIAi.saves:
        if "variable " + d in word:
            word = word.replace("variable " + d,TIAi.saves[d])
    return word