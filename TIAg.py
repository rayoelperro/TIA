import os
from Tkinter import *
from tkFileDialog import askopenfilename
from gtts import gTTS

def leerarchivo():
    Tk().withdraw()
    filename = askopenfilename(title="TIA FILE READER")
    return open(filename,'r').read()

def decir(texto):
    try:
        tts = gTTS(text=texto, lang='es-es')
        tts.save("TIAPLAY.mp3")
        os.system("python TIAs.py")
    except:
        print "Error"

class TextReader():
    def __init__(self):
        self.to = None
        self.on = True
        self.root = Tk()
        self.root.title("TIA TEXT READER")
        S = Scrollbar(self.root)
        self.T = Text(self.root, height=7, width=50)
        S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)
        B = Button(self.root, text="Aceptar", command=self.__gettext)
        B.pack()
        mainloop()
    def __gettext(self):
        self.to = self.T.get("1.0",END)
        self.on = False
        self.root.destroy()
    def readandclose(self):
        while True:
            if self.to != None:
                d = self.to
                return d
            elif not self.on:
                return None

def readtext():
    t = TextReader()
    return t.readandclose()