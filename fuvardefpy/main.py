"""
3.                                                     Fuvar                                 (18pont)
Az UTF-8 kódolású fuvar.csv állomány a 2016-os chicagói taxis fuvarozások adatait tartalmazza. 

A feladatok megoldása előtt tanulmányozza az állomány szerkezetét! Az adatok következő minta szerint vannak eltárolva:


• taxi azonosítója (egész szám, pl.: 8192)
• indulás időpontja (időbélyegző, melyben minden adat előnullázott, akár
szövegként is kezelhető, pl.: 2016-12-02 07:45:00)
• az utazás időtartama (egész szám, az adatok másodpercben értendőek, pl. 900)
• a megtett távolság (valós szám, az adatok mérföldben értendőek, pl. 1,5)
viteldíj (valós szám, az adatok dollárban értendőek, pl. 7,5)
• borravaló (valós szám, az adatok dollárban értendőek, pl. 4,15)
• a fizetés módja (szöveges, pl. ,,bankkártya")


Az adatokat pontosvessző választja el egymástól. Ügyeljen arra, hogy a fájl első sora az
adatok fejlécét tartalmazza!!! Olvassa be a fuvar.csv állományban található adatokat és
tárolja el egy megfelelően megválasztott adatszerkezetben (listába)!


3.1 A feladat megoldásához hozzon létre grafikus vagy konzolalkalmazást (projektet) Fuvar azonosítóval!

3.2 Hozzon létre egy osztályt (class), ami reprezentálja az adatok példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 
Olvassa be a fuvar.csv állományban található adatokat és tárolja el adatokat egy homogén listába, amely használatával a további feladatok megoldhatók! A terminálra való kiírás legyen a mintának megfelelő!

3.3 Határozza meg és írja ki a képernyőre a minta szerint, hogy hány utazás került
feljegyzésre az állományban!

3.4 Határozza meg és írja ki a képernyőre a minta szerint, hogy a 6185-ös azonosítójú
taxisnak mennyi volt a bevétele, és ez hány fuvarból állt! Feltételezheti, hogy van ilyen
azonosítójú taxis.

3.5 Programjával határozza meg az állomány adataiból a fizetési módokat, majd összesítse,
hogy az egyes fizetési módokat hányszor választották az utak során! Ezeket az
eredményeket a minta szerint írja a képernyőre! A kiírás során a fizetési módok sorrendje
bármilyen lehet.


Minta / output: _____________________________________________________

3.3 feladat: 1859 fuvar
3.4 feladat: 4 fuvar alatt: 33,75$
3.5 feladat:
      bankkártya: 793
      Készpénz: 1050
      vitatott: 4
      ingyenes: 10
      ismeretlen: 2

_______________________________________________________________________

"""

# taxi_id;
#indulas;
#idotartam;
#tavolsag;
#viteldij;
#borravalo;
#fizetes_modja
# 5240;2016-12-15 23:45:00;900;2,5;10,75;2,45;bankkártya

#1-2

class Fuvar:
  def __init__(self,sor):
    taxi_id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes_modja = sor.strip().split(";")
    self.taxi_id = int(taxi_id)
    self.indulas = indulas
    self.idotartam = int(idotartam)
    self.tavolsag = float(tavolsag.replace(",","."))
    self.viteldij = float(viteldij.replace(",","."))
    self.borravalo = float(borravalo.replace(",","."))
    self.fizetes_modja = fizetes_modja

with open("fuvar.csv","r",encoding="utf-8") as f:
  fejlec = f.readline()
  lista = [Fuvar(sor) for sor in f]


#3
def utazasok(lista):
  return len(lista)

utazasok = utazasok(lista)
print(utazasok)

#4
def dij(lista):
  taxi = [ sor.viteldij for sor in lista if sor.taxi_id == 6185]

  mennyi = sum(taxi)
  hanyszor = len(taxi)
  mennyi = str(mennyi)
  mennyi = mennyi.replace(".",",")

  return hanyszor, mennyi

dij = dij(lista)
print(dij)

#5
def fizetes(lista):
  bank = len([sor for sor in lista if sor.fizetes_modja == "bankkártya"])
  keszpenz = len([sor for sor in lista if sor.fizetes_modja == "készpénz"])
  vitatott = len([sor for sor in lista if sor.fizetes_modja == "vitatott"])
  ingyenes = len([sor for sor in lista if sor.fizetes_modja == "ingyenes"])
  ismeretlen = len([sor for sor in lista if sor.fizetes_modja == "ismeretlen"])

  return bank, keszpenz, vitatott, ingyenes, ismeretlen

fizetes = fizetes(lista)
print(fizetes)