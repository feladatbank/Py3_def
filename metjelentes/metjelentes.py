#1-2 Feladat
class Ido_jaras:
  def __init__(self,sor):
    telepules,ido,szel_irany,homerseklet = sor.strip().split(" ")
    self.telepules = telepules
    self.ido = ido
    self.szel_irany = szel_irany
    self.homerseklet = int(homerseklet)
    self.erőség = szel_irany[3:]

with open("tavirathu13.txt","r",encoding="UTF-8") as f:
  cim = f.readline()
  lista = [Ido_jaras(sor) for sor in f]
  
#3 Feladat

def telepules_kodja_utolso_meres(lista, kod):
  utolso_meres = max([sor.ido for sor in lista if kod == sor.telepules])
  return utolso_meres
  
telepules_kodja_utolso_meres = telepules_kodja_utolso_meres(lista, "SM")
print(f" ora: {telepules_kodja_utolso_meres[:2]} perc: {telepules_kodja_utolso_meres[2:]}")

#4 Feladat
def legmagasabb_homerseklet(lista):
  telepules_neve = ""
  ido_pont = ""
  nagy = 0
  for sor in lista:
    if sor.homerseklet > nagy:
      nagy = sor.homerseklet
      telepules_neve = sor.telepules 
      ido_pont = sor.ido
  return telepules_neve, ido_pont[:2], ido_pont[2:], nagy
    
legmagasabb_homerseklet = legmagasabb_homerseklet(lista)
print(legmagasabb_homerseklet)

#5 Feladat
def szelcsend_meres(lista):
  a = []
  for sor in lista:
    if sor.szel_irany == "00000":
      a.append(sor.telepules)
      a.append(sor.ido)
  return a

szelcsend_meres = szelcsend_meres(lista)
print(szelcsend_meres)
