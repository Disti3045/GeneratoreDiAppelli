"""
Created on Fri Feb  7 13:21:28 2025

@author: Leonardo Di Stefano
"""
import os
import PIL
import random

teoria = os.path.expanduser("~\OneDrive\Desktop\GeneratoreDiAppelli\Teoria")
pratica = os.path.expanduser("~\OneDrive\Desktop\GeneratoreDiAppelli\Pratica")
totGen = len(os.listdir(os.path.expanduser("~\OneDrive\Desktop\GeneratoreDiAppelli\Appelli")))
pdf = list()
###############################################################################
def DefinizioneImmagini(cartella):
    #Estrazione dei file dalla cartella
    estensioni = [".png", ".jpg", ".jpeg"]
    listaFile = os.listdir(cartella)
    #Rimozione elementi non validi dalla lista
    for img in listaFile:
        if img.lower().endswith(estensioni):
            listaFile.append(os.path.join(cartella, img))
            listaFile.remove(img)
        else:
            listaFile.remove(img)
    return listaFile
def SelezioneQuesiti(maxLista, tipo):
    indici = list()
    if tipo == "Teoria":
        nQuesiti=3
    else:
        nQuesiti=5
    #Estrazioe Quesiti
    for i in range(1, nQuesiti):
        nmb = random.randint(0, maxLista-1)
        if nmb not in indici:
            indici.append(nmb)
        else:
            while nmb in indici:
                nmb = random.randint(0, maxLista-1)
            indici.append(nmb)
    return indici
def EstrazionePercorsi(nmb, lista, listaFinale, totGen):
    pdfList = list()
    for i in nmb:
        pdfList.append(lista[i])
    listaFinale += pdfList 
def CreazionePdf(lista, totGen):
    for img in lista:
        img = PIL.Image.open(img).convert("RGB")
        
    lista[0].save(f"AppelloGenerato{totGen+1}", save_all=True, append_images=lista[1:])
    pdfPath = os.path.join(os.path.expanduser("~\OneDrive\Desktop\GeneratoreDiAppelli\Appelli"), f"AppelloGenerato{totGen+1}.pdf")
    return pdfPath
###############################################################################
listaTeoria = DefinizioneImmagini(teoria)
listaPratica = DefinizioneImmagini(pratica)
if len(listaTeoria)>3 and len(listaPratica)>5:
    nmbT = SelezioneQuesiti(len(listaTeoria), "Teoria")
    nmbP = SelezioneQuesiti(len(listaPratica), "Pratica")
else:
    print("Invalid elements")
if len(nmbT)>1 and len(nmbP)>1:
    EstrazionePercorsi(nmbT, listaTeoria, pdf)
    EstrazionePercorsi(nmbP, listaPratica, pdf)
else:
    print("Invalid numbers")

os.open(CreazionePdf(pdf, totGen))