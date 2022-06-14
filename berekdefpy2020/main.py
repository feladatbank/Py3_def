"""
3. feladat                       Összesen: 20 pont

                  Bérek 2020


Ebben a feladatban egy cég dolgozóinak 2020-as adatai állnak rendelkezésünkre,
melyekkel programozási feladatokat kell megoldania.

A bérek2020.txt UTF-8 kódolású forrásállomány soraiban egy-egy dolgozó adatait
tároltuk a következő sorrendben:

neve, például: Beri Dániel
neme: nő vagy férfi
a részleg, ahol dolgozik, például: beszerzés
a belépés éve, például: 1979
a dolgozó bére (fizetése), például: 222943

Az állomány első sora a mezőneveket tartalmazza, az adatokat pontosvesszővel
választottuk el:

Név; Neme; Részleg; Belépés; Bér
Beri Dániel; férfi; beszerzés; 1979; 222943
Csavar Pista; férfi; pénzügy; 1995; 234074
Lakatos Pál; férfi; beszerzés; 1986;159538
Devon Mihály; férfi; asztalosműhely; 2007; 161533
Él Ilona; nő; beszerzés; 1982;299965
...

 1. Készítsen grafikus vagy konzolalkalmazást (projektet) a következő feladatok
megoldásához, amelynek projektjét Bérek2020 néven mentse el!

2. Olvassa be a bérek2020.txt állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben, amely használatával a további feladatok megoldhatók!
Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! 

3. Határozza meg és írja ki a képernyőre, hogy hány dolgozó adatai találhatók a
forrásállományban!

4. Határozza meg és írja ki a képernyőre a 2020-as átlagbéreket! Az eredményt ezer
forintban, egy tizedesjegyre kerekítve jelenítse meg!

5. Kérje be egy részleg nevét a felhasználótól a minta szerint!

6. Az előző feladatban megadott részlegen keresse meg és írja ki a legnagyobb bérrel
(fizetéssel) rendelkező dolgozó adatait! Ha a megadott részleg nem létezik a cégnél,
akkor a A megadott részleg nem létezik a cégnél!" feliratot jelenítse meg!
Feltételezheti, hogy nem alakult ki ,,holtverseny" egy-egy részlegen dolgozók fizetése
között!

Minta: Output: ___________________________________

3.feladat: Dolgozók száma: 170 fő
4.feladat: Bérek átlaga: 250,3 eFt
5.feladat: Kérem egy részleg nevét: beszerzés

6.feladat: A legtöbbet kereső a megadott részlegen:
       Név: Czeczei Zsolt
       Neme: férfi
       Belépés: 1981
       Bér: 452042 Forint

____________________________________________________
"""

#Név;Neme;Részleg;Belépés;Bér
#Beri Dániel;férfi;beszerzés;1979;222943
#Csavar Pista;férfi;pénzügy;1995;234074

#2

class Berek:
  def __init__(self,sor):
    nev,neme,reszleg,belepes,ber = sor.strip().split(";")
    self.nev = nev
    self.neme = neme
    self.reszleg = reszleg
    self.belepes = belepes
    self.ber = int(ber)

with open("berek2020.txt","r",encoding="utf-8") as f:
  fejlecc = f.readline()
  lista = [Berek(sor) for sor in f]

#3
def dolgozok_szama(lista):
  return len(lista)

dolgozok_szama = dolgozok_szama(lista)
print(dolgozok_szama)

#4
def atlag(lista):
  berek = [sor.ber for sor in lista] 
  ossz = sum(berek)
  atlag = ossz / len(berek)
  atlag = atlag / 1000
  atlag = f"{atlag:.1f}"
  atlag = str(atlag)
  atlag = atlag.replace(".",",")

  return atlag

atlag = atlag(lista)
print(atlag)

#5-6
def reszleg(lista, bekeres):
  legnagyobb = [(sor.ber,sor) for sor in lista if sor.reszleg == bekeres]

  if len(legnagyobb) > 0:
    nagy,adat = max(legnagyobb)

  if len(legnagyobb) > 0:
    return bekeres, adat.nev, adat.neme, adat.belepes, nagy
  else:
    x = "A részleg nem létezik!"
  return x

reszleg = reszleg(lista, "beszerzés")
print(reszleg)


