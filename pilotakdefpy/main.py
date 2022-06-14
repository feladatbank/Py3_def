"""
                  Pilóták                (18pont)

A következő feladatban a Forma-1 pilótáinak adataiból készített szöveges állományból
kell adatokat kinyernie.

 A pilotak.csv UTF-8 kódolású forrásállomány soraiban a következő sorrendben
találja meg az adatokat:

• a pilóta neve (név), például: Lewis Hamilton
• a pilóta születési dátuma (születési_dátum), például: 1985.01.07
• a pilóta nemzetisége (nemzetiség), például: brit
• a pilóta rajtszáma (rajtszám), például: 44
Csak az aktuális évben aktív pilótáknak van rajtszámuk, a többiek esetében a
rajtszám mező értéke üres. Több pilótának is lehet azonos rajtszáma.

Az állomány első sora a mezőneveket tartalmazza, az adatokat pontosvesszővel
választottuk el.

3.1 Készítsen konzolalkalmazást (projektet) a következő feladatok megoldásához,
melynek projektjét Versenyzők néven mentse el!

3.2 Hozzon létre egy osztályt (class), ami reprezentálja az adatok példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 
Továbbá olvassa be a pilotak.csv állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben (pl. vektor, lista stb.), amely használatával a további
feladatok megoldhatók! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét
tartalmazza!

3.3 Határozza meg és írja ki a képernyőre a minta szerint, hogy az állomány hány adatsort
tartalmaz!

3.4 Határozza meg és írja ki a minta szerint, hogy az állomány utolsó sorában melyik
pilóta neve szerepel!

3.5 Határozza meg és írja ki a minta szerint, hogy mely pilóták születtek a XIX. században
(azaz 1901. január 1-je előtt)! Feltételezheti, hogy a van olyan pilóta, aki 1901 előtt
született. Írja ki a minta szerint a pilóták születési dátumát is!

(Minta Output)  __________________________________

3.3 feladat: 847
3.4 feladat: Alexander Albon
3.5 feladat
       Louis Chiron (1899.08.03)
       Arthur Legat (1898.11.01)
       Hans von Stuck (1900.12.27)
       Philippe Étancelin (1896.12.28)
       Bill Aston (1900.03.29)
       Adolf Brudes (1899.10.15)
       Piero Dusio (1899.10.13)
       Luigi Fagioli (1898.06.09)
       Clemente Biondetti (1898.08.18)

__________________________________________________

"""

#név;születési_dátum;nemzetiség;rajtszám
#Lewis Hamilton;1985.01.07;brit;44
#Nick Heidfeld;1977.05.10;német;

#1-2

class Pilotak:
  def __init__(self,sor):
    nev,szuletes,nemzetiseg,rajtszam = sor.strip().split(";")
    self.nev = nev
    self.szuletes = szuletes
    self.nemzetiseg = nemzetiseg
    self.rajtszam = rajtszam
    self.ev = int(szuletes[0:4])

with open("pilotak.csv","r",encoding="utf-8") as f:
  f.readline()
  lista = [Pilotak(sor) for sor in f]

#3
def adat_sorok(lista):
  return len(lista)

adat_sorok = adat_sorok(lista)
print(adat_sorok)
#4
def pilotak(lista):
  pilotak = [sor.nev for sor in lista][-1]
  return pilotak

pilotak = pilotak(lista)
print(pilotak)

#5(azaz 1901. január 1-je előtt)
def keres(lista):
  kereso = [sor for sor in lista if sor.ev < 1901]
  x = [(sor.nev, sor.szuletes) for sor in kereso]
  return x

keres = keres(lista)
print(keres)