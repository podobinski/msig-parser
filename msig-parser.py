import os
import datetime
from datetime import datetime


start = datetime.now()

plik = open("monitor-export.txt")
plik_nowy = open("monitor-etap1.txt", "w+")

print ("Rozpoczęto przetwarzanie MSiG")

for linia in plik.readlines():  
    if "PESEL nr " in linia:
        linia_nowa = linia[linia.find("PESEL nr ")+9:linia.find("PESEL nr ")+20]
        plik_nowy.write(linia_nowa)
        plik_nowy.write("\n")
    elif "PESEL: " in linia:
        linia_nowa = linia[linia.find("PESEL")+8:linia.find("PESEL")+19]
        plik_nowy.write(linia_nowa)
        plik_nowy.write("\n")
    elif "PESEL numer " in linia:
        linia_nowa = linia[linia.find("PESEL numer ")+12:linia.find("PESEL numer ")+23]
        plik_nowy.write(linia_nowa)
        plik_nowy.write("\n")
    elif "PESEL" in linia:
        linia_nowa = linia[linia.find("PESEL")+6:linia.find("PESEL")+17]
        plik_nowy.write(linia_nowa)
        plik_nowy.write("\n")
    else:
        pass             

plik_nowy.close()                       
plik.close()
print ("Zakończono przetwarzanie MSiG")
koniec = datetime.now()

print ("Przetwarzanie zajęło: "+str(koniec-start))
input ("Naciśnij dowolny przycisk aby zakończyć")

#wersja 0.001
