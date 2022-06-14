"""
3. Nobel-díjak            (18pont)

A következő feladatban a Svéd Királyi Tudományos Akadémia által osztott Nobel-díj
napjainkig feljegyzett adatait tartalmazó szöveges állományt kell feldolgoznia.

Az UTF-8 kódolású nobel.csv állomány tartalmazza a kiosztott díjak adatait.
Minden adatsorhoz rendre a következő mezők tartoznak:
_____________________________________________________
• évszám
• típus (fizikai, kémiai, orvosi, irodalmi, béke, közgazdaságtani)
• keresztnév
• vezetéknév
_____________________________________________________
Az adatokat pontosvessző választja el egymástól! Ügyeljen arra, hogy a fájl első sora az adatok fejlécét tartalmazza! Amennyiben a díjat egy szervezet kapta, akkor a
keresztnév mezőben szerepel a szervezet teljes neve, míg a vezetéknév mező ebben az
esetben üres.

3.1. A feladat megoldásához hozzon létre grafikus vagy konzolalkalmazást (projektet)
Nobel azonosítóval!

3.2 Hozzon létre egy osztályt (class), ami reprezentálja az adatok példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 

Olvassa be a nobel.csv állományban található adatokat és tárolja el adatokat egy homogén listába, amely használatával a további feladatok megoldhatók! A terminálra való kiírás legyen a mintának megfelelő! Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 

3.3 Határozza meg és írja ki a képernyőre a minta szerint, hogy Arthur B. McDonald
milyen típusú díjat kapott! Feltételezheti, hogy életében csak egyszer kapott Nobel-
díjat.

3.4 Határozza meg és írja ki a képernyőre a minta szerint, hogy ki kapott 2017-ben
irodalmi Nobel-díjat!

3.5 A Curie család több tagja is kapott díjat. Határozza meg és írja ki a képernyőre a
minta szerint, hogy melyik évben a család melyik tagja milyen díjat kapott!

( Minta / Output )________________________________

3.3 feladat: fizikai
3.4 feladat: Kazuo Ishiguro
3.5 feladat:
         Irène Joliot-Curie(kémiai)
         Marie Curie, née Sklodowska(kémiai)
         Pierre Curie(fizikai)
         Marie Curie, née Sklodowska(fizikai)

__________________________________________________

"""

#év;típus;keresztnév;vezetéknév
#2017;fizikai;Rainer;Weiss
#2017;fizikai;Barry C.;Barish
#2017;fizikai;Kip S.;Thorne

#1-2

class Nobel_dijak:
  def __init__(self,sor):
    ev,tipus,kereszt,vezetek = sor.strip().split(";")
    self.ev = int(ev)
    self.tipus = tipus
    self.kereszt = kereszt
    self.vezetek = vezetek

with open("nobel.csv","r",encoding="utf-8") as f:
  f.readline()
  lista = [Nobel_dijak(sor) for sor in f]

#3 Arthur B. McDonald
def dijazot(lista):
  milyen_tipusu = [sor.tipus for sor in lista if sor.kereszt == "Arthur B." and sor.vezetek == "McDonald"][0]
  return milyen_tipusu

dijazot = dijazot(lista)
print(dijazot)

#4
def irodalmi(lista):
  irodalmi2 = [sor for sor in lista if sor.ev == 2017 and sor.tipus == "irodalmi"]
  x = [(sor.kereszt, sor.vezetek) for sor in irodalmi2]
  return x

irodalmi = irodalmi(lista)
print(irodalmi)

#5
def curie(lista):
  curie = [sor for sor in lista if "Curie" in sor.vezetek or "Curie" in sor.kereszt]
  x = [(sor.kereszt, sor.vezetek, sor.tipus) for sor in curie]
  return x

curie = curie(lista)
print(curie)

