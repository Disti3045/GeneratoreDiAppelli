# ![Generatore di Appelli](https://github.com/Disti3045/GeneratoreDiAppelli/blob/main/GeneratoreDiAppelli.png?raw=true) GeneratoreDiAppelli by Leonardo Di Stefano
Generatore di appelli casuali per corsi universitari, suddivisi in parte teorica e parte scritta.

## Come funziona?
0. Installate la libreria PILLOW sul vostro computer, facendo "pip install pillow" nel prompt di comandi.
2. Scaricare tutta la cartella GeneratoreDiAppelli.zip, in cui sono presenti GeneraAppello.py, Appelli, Teoria, Pratica, ed estrarla.
3. Inserire nella cartella *Teoria* gli screenshot (.png .jpg .jpeg) delle domande di teoria, ATTENZIONE devono essere almeno 3.
4. Inserire nella cartella *Pratica* gli screenshot (") delle domande di pratica, ATTENZIONE devono essere almeno 5.
5. Esegui il programma *GeneraAppello.py*, una volta generato si aprira il file AppelloGeneratoN dove N è il numero di appello generato.
6. In caso chiudeste il file, basta andare nella cartella *Appelli* e ritroverete tutti gli appelli generati fino ad allora.

## Personalizzazione
Nella seconda sezione del codice ci sono una serie di variabili modificabili tra cui: numero di quesiti di teoria e pratica e i path delle cartelle.

## Importante da sapere
Installate la libreria PILLOW sul vostro computer, facendo "pip install pillow" nel prompt di comandi.
Qual'ora eliminaste i pdf degli appelli generati dalla cartella, il prossimo appello generato ripartirà da zero. Se ne eliminate solo uno, eliminate l'ultimo appello generato, altrimenti quando genererete un nuovo appello il penultimo appello verrà rimpiazzato. (Ad esempio se avete 8 Appelli e eliminate "AppelloGenerato4", il prossimo appello che genererete sara AppelloGenerato8 perchè sono presenti 7 appelli nella cartella)
Se volete più quesiti di teoria o pratica basterà giocare con le variabili nel codice, giusto assicuratevi poi di avere almeno il nuovo numero di quesiti messo nella cartella.

## Note
Aggiornerò e rivedrò sicuramente il codice per renderlo più adatto a tutte le situazioni, scalabile e modulare.
