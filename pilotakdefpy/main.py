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
