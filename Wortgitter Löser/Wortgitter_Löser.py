"""
Programm von: Martin Hager
Datum: 02.09.2020

Ziel: Automatisches finden von Wörtern in einem Wortgitter (in allen Richtungen inkl. schräg und rückwärts)
    wenn wörter in einer Richtung ineindander liegen [E I M  | E R | B S E] werden beide ausgegeben --> Ausgabe Eimer & Erbse, jedoch nich wenn sie nur ein Teil vom Wort sind [E I | S  | E N | B A H N] --> Ausgabe: nur Eisenbahn
"""

import Wortliste

#goodletters_forGrid  = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÄäÜüÖö"
def UmlautWahl():
    Auswahl = 0
    while True:
            try:
                Input = input("Hat das Suchsel Umlaute(Ä) oder keine (AE stat Ä)| 'AE' für keine Umlaute, 'Ä'für Umlaute ")
                if Input=="AE":
                    Auswahl = 0
                    break
                elif Input== "Ä":
                    Auswahl = 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Das war keine gültige Eingabe!! Bitte wiederholen!")
    print('\n')
    return Auswahl

def printGefundenWoerter(Wörterliste):
    richtung = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    richtungStr=""
    print("Result:\n")
    Wörterliste.sort()
    for Wort in Wörterliste:
        Richtung = richtung.index(Wort[2])
        if(Richtung==0):
            richtungStr = "u"
        elif(Richtung==1):
            richtungStr = "ur"
        elif(Richtung==2):
            richtungStr = "r"
        elif(Richtung==3):
            richtungStr = "dr"
        elif(Richtung==4):
            richtungStr = "d"
        elif(Richtung==5):
            richtungStr = "dl"
        elif(Richtung==6):
            richtungStr = "l"
        elif(Richtung==7):
            richtungStr = "ul"

        position = "pos: ("+ str(Wort[1][0]+1) + " | " + str(Wort[1][1]+1)+ ")"
        print(Wort[0],position,richtungStr,len(Wort[0]),sep=' \u2590 ')

    #print(Wörterliste)

def  check_For_letters(string):
    return string.isalpha()        


def Grid_einlesen():
    #Definition Variablen:
    Zeile = ""#Eingegebener Input
    Zeile_Liste =  []#Eingegebener Input als Liste
    Grid = []#Grid Litse aus Listen
    indexLoop = 0 #index der durchgelaufenen Loops
    FileExists = 0 #true wenn File mit Wortgitter vorhanden
    SkipFileEnter = 0 #wenn der User das Gitter in der DAtei verwenden möchte
    #öffnet file
    try:
        gridFile = []#speichert das fromatierte Gitter
        fileName = input("Name der einzulesenden Datei angeben[mit Dateierweiterung(.txt)][Bitte in UTF8 formatiert](wenn keine Datei eingelesen werden solll leer lassen und Enter drücken): ")
        GitterFile = open(fileName,encoding="UTF-8", mode="r").readlines()#öffnet File und speichert Inhalt in GitterFile
        #formatiert das Gitter
        for zeile in GitterFile:
            ZeileF = []
            for buchstabe in zeile:
                if check_For_letters(buchstabe)==1: 
                    ZeileF.append(buchstabe)
            gridFile.append(ZeileF)
        FileExists=1#wenn erstmal File gelesen existiert es
        #print(gridFile) #DEBUG
        #checkt ob das Gitter gültig ist(gibt Fehler wenn leer)
        if not gridFile: 
            print("Datei konnte nicht gelesen werden.(Ist leer) Bitte Wortgitter manuell eingeben [err1.1]")#Fehler1.1
            raise NameError
        elif not gridFile[0]: 
            print("Datei konnte nicht gelesen werden.(Ist leer) Bitte Wortgitter manuell eingeben [err1.2]")#Fehler1.2
            raise NameError
        else:
            pass   
        #prüft ob alle Zeilen Gleichlang sind   
        for zeileF in gridFile:#checkt ob das Gitter gültig ist
            if len(zeileF)!=len(gridFile[0]):
                print("Grid ist ungültig. Bitte Wortgitter manuell eingeben [err2]")#Fehler2
                raise NameError
    #Fehler exceptions:
    except FileNotFoundError:#wenn kein File vorhanden ist wird FileExists auf 0 gesetzt
        FileExists=0
    except NameError:#Wenn Grid ungültig ist
        FileExists=0
    except:
        raise NameError("Datei konnte nicht gelesen werden. Bitte Datei korrigieren oder löschen.")
        FileExists=0
    #Wenn file mit Gitter vorhanden skip die Hauptloop, wenn von User gewünscht
    if FileExists==1:
        while True:
            try:
                Input = input("Ein Wortgitter ist vorhanden, dieses verwenden? [Y/N] \nWenn NEIN geben sie es dann manuell ein: ")
                if Input=="Y":
                    SkipFileEnter = 1
                    Grid=gridFile
                    break
                elif Input== "N":
                    SkipFileEnter = 0
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Das war keine gültige Eingabe!! Bitte wiederholen!")
    #für jede Zeile [Hauptloop]            
    while (True&SkipFileEnter==0): 
        Zeile = input("Geben sie die erste Zeile des Gitters ein (ohne Abtrennung)[BSP: 'RATUISF']")#input
        if indexLoop > 0:#dass alle Zeilen gleich lang sind
            if len(Zeile) != len(Grid[0]):
                länge = "lang" if (len(Zeile)>len(Grid[0])) else "kurz";
                print("Die Zeile ist zu " + länge + "!!! \nBitte Zeile erneut eingeben: ")
                Zeile=""
                Zeile_Liste = []
                continue
        if check_For_letters(Zeile)==0:#schaut ob nur Buchstaben eingegeben worden sind
            print("Ungültige Zeichen! Es sind nur Buchstaben und Umlaut erlaubt\nBitte Zeile erneut eingeben: ")#wenn nicht, Fehlermeldung und Schleife neu beginnen
            Zeile=""
            Zeile_Liste = []
            continue
        for buchstabe in Zeile:#wandelt string in Liste um
            Zeile_Liste.append(buchstabe)
        Grid.append(Zeile_Liste)#fügt Zeile zum Grid hinzu
        print("Fertig!")
        
        while (True):#für den Input danach
            answer = input("\nn - drücken um die nächste Zeile einzugeben | e - drücken wenn Sie fertig mit eingeben des Gitters sind: ")#input
            if answer=="n":#wenn man eine neue Zeile eingeben will wiederholt sich die Hauptloop
                Zeile=""
                Zeile_Liste = []
                indexLoop += 1
                a=0
                break
            elif answer == "e":#wenn man fertig ist beendet sich die Hauptloop
                a=1
                break
            else:
                print("Fehler! Nur 'n' oder 'e' eingeben!")#wenn man ungültiges eingibt, wiederholt sich diese loop
        if a==0: #sorgt für den exit oder neu Anfang der Hauptloop
            continue
        elif a==1:
            break
    #Die Doppel Schleife macht alle Buchstaben zu Großbuchstaben, damit auch wenn man Groß/- und Kleinbuchstaben verwendet hat alle einheitlich sind
    for Zeile in Grid:
        for i in range(len(Zeile)):
            Zeile[i]=Zeile[i].upper()
 
    return Grid#gibt das fertige Grid zurück
 
def WortPruefung(Wort,Wortliste):
    laengeWort = len(Wort)
    for LexWort in Wortliste:
        
        find = LexWort.find(Wort)
        laengeLexWort = len(LexWort)
        if find<=-1 or find>0:
            pass
        else:
           if laengeWort != laengeLexWort:
               return 0
           elif laengeWort == laengeLexWort:
               return 1
    return -1
            
        #Fälle:
        #   Fall1: Wort ist nicht in LexWort (x.find(y)==-1) 
        #   Fall2: Wort ist in Lexwort, aber nicht vorne (x.find(y)>0) 
        #   Fall3: Wort ist in Lexwort, steht am Anfang (x.find(y)==0) AND len(Wort)!=len(LexWort)
        #   Fall4: -||-                                               AND len(Wort)==len(LexWort)     
        #Return:
        #   -1: Fall1; Fall2
        #   0: Fall3
        #   1: Fall4     


def Woerter_finden(Grid,umlaut):#umlaut = 0 --> AE statt Ä | umlaut = 1 es sind umlaut im gitter Ä
    #Definition Variablen
    richtung = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] #gibt den offset an für nächsten Buchstaben | Richtung = 0 -> nach oben ; geht im Uhrzeigersinn
    zeile = 0 #zeile des aktuellen Buchstabens (anfangsbuchstabe)
    spalte = -1 #spalte des aktuellen Buchstabens (anfangsbuchstabe)
    a=0 #Offset Zeile
    b=0 #Offset Spalte
    l=1 #multiplikator des offset (bestimmt größe)
    x=0 #Position im Grid
    y=0 #Position im Grid
    result = -1 # 
    gefundeneWoerter=[]#Liste aller gefunden Wörter (gespeichert pro Wort: ["Wort",[X.ersterBuchstabe,Y.ersterBuchstabe],Richtung(0-7)])
    moeglWort = ""#wenn schon eins gefunden wurde (nicht sofort ende wegen mögl. auf längeres, aber gespeichert falls nicht (kein längeres))
    aktWort = ""#aktuelle Zeichenfolge
    #wählt die Wortliste
    WList = Wortliste.WortListe_ohneUmlaut_mitAE if (umlaut==0) else Wortliste.WortListe_mitUmlaut#legt fest ob im Grid AE statt Ä steht
    print('Lädt! Bitte warten...')
    for num in range((len(Grid))*(len(Grid[0]))):
        print (num)
        if spalte+1<len(Grid[0]):
            spalte+=1
        else:
            spalte=0
            zeile+=1
        #zeile+1
        #spalte+1
        #print((len(Grid))*(len(Grid[0])))
        #print(Grid)
        #print(zeile)
        #print(spalte)
        print(spalte,zeile,sep='|')
        aktWort= Grid[zeile][spalte]
        for richt in richtung:#für jede Richtung 
            a = richt[0]
            b = richt[1]
            
            while(True):#sucht in der Richtung in jeder möglichen Zeichenfolge(von anfangsbuchstabe) nach übereinstimmung in Wortliste
                x = zeile+l*a
                y = spalte+l*b
                if ( (x<0) or (x>len(Grid)-1) ) or ( (y<0) or (y>len(Grid[0])-1) ):
                    if moeglWort:
                        gefundeneWoerter.append((moeglWort,[zeile,spalte],richt))
                    #print("out of index",x,y,sep=', ')
                    break
                else:
                    aktWort = aktWort + Grid[x][y]
                    result = WortPruefung(aktWort,WList)
                    if (not moeglWort) and result == -1:
                        break
                    elif (not moeglWort) and result == 0:
                        pass
                    elif (not moeglWort) and result == 1:
                        moeglWort=aktWort
                    elif moeglWort and result == -1:
                        gefundeneWoerter.append((moeglWort,[zeile,spalte],richt))
                        break
                    elif moeglWort and result == 0:
                        pass
                    elif moeglWort and result == 1:
                        moeglWort=aktWort
                    #print("in index",x,y,Grid[x][y],sep=', ')
                    #print(Grid[x][y],end='')
                
                l+=1
            aktWort=Grid[zeile][spalte]
            result = -1
            l=1
            moeglWort=""
            #print("\n")
        aktWort=""
    return gefundeneWoerter  
        
    


Umlaut = UmlautWahl()
Grid = Grid_einlesen()
#print(Grid[18])
WortListe= Woerter_finden(Grid,Umlaut)#0: AE | 1: Ä
#print(Wortliste.WortListe_ohneUmlaut_mitAE)
printGefundenWoerter(WortListe)
print(len(Grid),len(Grid[0]),sep=';')

wait = input("Zum beenden Eingabe Taste drücken")