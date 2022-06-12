"""
            Meteorológiai jelentés           (18 pont)
{{{{ Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! }}}}
ÜGYELJEN arra hogy az tavirathu13.txt fálj beolvasásánál van fejléc!!!
telepules,ido,szel_irany,homerseklet,erőség

1. A feladat megoldásához hozzon létre programot metjelentes azonosítóval(néven)!

2.  Olvassa be a tavirathu13.txt állományban található adatokat és tárolja el adatokat egy listába,ügyeljen arra, hogy az állomány fejlécet tartalmaz! amely használatával a további feladatok megoldhatók! A kimenet a mintának megfelelő adatot adja vissza! Lehetőség szerint CLASS HASZNÁLATÁVAL! Ha nem CLASS-sal oldod meg, akkor is érvényes, de nem kaphatsz a feladatra maximális pontot.

3. Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett az utolsó mérési adat! A kiírásban az idöpontot óó:pp formátumban jelenítse meg!

4. Határozza meg, hogy mikor mérték a legmagasabb hőmérsékletet! Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és a hőmérsékletet! Amennyiben több legnagyobb érték van, akkor elég az egyiket kiírnia.

5. Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor a „Nem volt szélcsend a mérések idején." szöveget írja ki! A kiírásnál a település kódját és az időpontot jelenítse meg.

Output / kimenet______________________________________
3. feladat
Adja meg egy település kódját! Település: SM
Az utolsó mérési adat a megadott településről 23:45-kor érkezett.
4. feladat
A legmagasabb hőmérséklet: DC 13:15 35 fok.
5. feladat
BP 01:00
DC 02:15
SN 03:15
BC 04:45
DC 04:45
SN 05:15
SN 05:45
KE 08:45
BC 11:45
_____________________________________________________

"""
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

def telepules_kodja(lista, kod):
  utolso_meres = max([sor.ido for sor in lista if kod == sor.telepules])
  return utolso_meres
  
telepules_kodja = telepules_kodja(lista, "SM")
print(f" ora: {telepules_kodja[:2]} perc: {telepules_kodja[2:]}")

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
