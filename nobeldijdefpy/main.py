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

