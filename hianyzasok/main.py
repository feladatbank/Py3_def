"""
Név;Osztály;Első nap;Utolsó nap;Mulasztott órák
Balogh Péter;6a;1;1;5
Horváth Judit;5a;1;1;5
Juhász János;6a;1;1;5
Lengyel Krisztina;6b;1;1;6
"""

class Szeptember:
    def __init__(self,sor):
        nev,osztaly,elso_nap,utolso_nap,mulasztott_orak = sor.strip().split(";")
        self.nev                = nev
        self.osztaly            = osztaly
        self.elso_nap           = int(elso_nap)
        self.utolso_nap         = int(utolso_nap)
        self.mulasztott_orak    = int(mulasztott_orak)

with open("szeptember.csv", encoding="latin2")as f:
    fejlec  = f.readline()
    lista   = [Szeptember(sor) for sor in f]

#2.feladat
def osszes_mulasztas(lista):
  x = sum([sor.mulasztott_orak for sor in lista])
  return x
osszes_mulasztas = osszes_mulasztas(lista)
print(osszes_mulasztas)

#3.feladat
def nap_nev_bekeres(lista, nap, nev):
  a = nap
  b = nev
  return a, b

nap_nev_bekeres = nap_nev_bekeres(lista, "10", "Kis Katalin")
#print(nap_nev_bekeres)

#4. feladat 
def nev_hianyzas(lista, nev):
  for sor in lista:
    if sor.nev == nev:
      for sor in lista:
        if sor.mulasztott_orak > 0:
          x = "A tanuló hiányzott Szeptemberben!"
    else:
      y = "A tanuló nem hiányzott Szeptemberben!"
  return x or y

nev_hianyzas = nev_hianyzas(lista, "Kis Katalin")
print(nev_hianyzas)


#5.feladat
def nap_hianyzas(lista, nap):
  a = []
  for sor in lista:
    if sor.elso_nap >= nap >= sor.utolso_nap:
      a.append(sor.nev)
      a.append(sor.osztaly)
    else:
      b = "Nem volt hiányzó az nap!"
  return a or b

nap_hianyzas = nap_hianyzas(lista, 19)
print(nap_hianyzas)