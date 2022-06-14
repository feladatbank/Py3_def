"""
név;első;utolsó;súly;magasság
Jim Abbott;1989-04-08;1999-07-21;200;75
Kyle Abbott;1991-09-10;1996-08-24;200;76
Joel Adamson;1996-04-10;1998-04-26;185;76
"""
#1-2 Feladat
class Balkez:
    def __init__(self,sor):
        nev,elso,utolso,suly,magassag = sor.strip().split(";")
        self.nev        = nev
        self.elso       = elso
        self.utolso     = utolso
        self.oktober    = utolso[0:7]
        self.suly       = suly
        self.magassag   = int(magassag)

with open("balkezesek.csv" , encoding="latin2")as f:
    r = f.readline()
    lista = [Balkez(sor) for sor in f]

#3. Feladat
def adat_sor(lista):
  hosz = len([sor for sor in lista])
  return hosz

adat_sor = adat_sor(lista)
print(adat_sor)

#4. Feladat
def utoljara99(lista):
  cm = 2.54
  oktober = [sor for sor in lista if sor.oktober == "1999-10"]
  u = [(sor.nev, (sor.magassag * cm)) for sor in oktober]
  return u

utoljara99 = utoljara99(lista)
print(utoljara99)

#5   
def bekeres(lista, ev):
  while True:
      if ev == "":
          continue
      if 1990 <= ev <=1999:
          break
      else:
          continue

bekeres = bekeres(lista, 1992)
print(bekeres)

