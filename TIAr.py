import speech_recognition as sr
import TIAb

def commandlikeconsole(text):
    words = list()
    inword = ""
    quotes = False
    for x in range(0,len(text)):
        if text[x] == " " and not quotes:
            if inword != "":
                words.append(inword)
                inword = ""
        elif text[x] == "\"":
            if quotes:
                quotes = False
            else:
                quotes = True
        else:
            inword += text[x]
    if inword != "":
        words.append(inword)
        del inword
    return words

def toTextToTIACommand(speechtext):
    speechtext = speechtext.replace(speechtext.split(" ")[0],speechtext.split(" ")[0].lower(),1)
    if speechtext.startswith("mostrar "):
        speechtext = "mostrar \"" + speechtext[8:] + "\""
    if speechtext.startswith("decir "):
            speechtext = "decir \"" + speechtext[6:] + "\""
    return speechtext

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(":")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="es-ES")
    except:
        return ""

def analize(words):
    sintax = TIAb.getTipePhrase(len(words))(words)
    sintax.sintax()

while True:
    analize(commandlikeconsole(toTextToTIACommand(listener())))