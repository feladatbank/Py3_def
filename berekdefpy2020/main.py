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


