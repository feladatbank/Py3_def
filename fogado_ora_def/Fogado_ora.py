#1-2 class


class Fogado_ora:
  def __init__(self,sor):
    vezetek,uto,lefoglalt_ido,foglalas_ido = sor.strip().split(" ")
    self.vezetek = vezetek
    self.uto = uto
    self.lefoglalt_ido = lefoglalt_ido
    self.foglalas_ido = foglalas_ido

with open("fogado.txt","r",encoding="utf-8") as f:
  f.readline()
  lista = [Fogado_ora(sor) for sor in f]

#3
def foglalasok_a_listaban(lista):
  x = len(lista)
  return x

  
foglalasok_a_listaban = foglalasok_a_listaban(lista)
print(f"Foglalások száma:{foglalasok_a_listaban}")

#4

def A_tanarok_foglalasai(lista, vezeteknev, keresztnev):
  kereso = len([sor for sor in lista if sor.vezetek == vezeteknev and sor.uto == keresztnev])
  if kereso:
    return kereso
  else:
    return 0

A_tanarok_foglalasai = A_tanarok_foglalasai(lista, "Nagy", "Ferenc")
print(f"A Tanárnak {A_tanarok_foglalasai} időpontfoglalás(a) van.")

#5 



def Tanarok_foglalasai(lista, ervenyes_ido):
  a = []
  kereso2 = [(sor.vezetek,sor.uto) for sor in lista if sor.lefoglalt_ido == ervenyes_ido]
  for sor in kereso2:
    a.append(sor)
  return a

Tanarok_foglalasai = Tanarok_foglalasai(lista, "17:40")
print(Tanarok_foglalasai)

#6

def legkorábban_lefoglalt_időpont(lista):
  t = []
  korai = str(lista[-1:-5])
  for sor in lista:
    if sor.foglalas_ido < korai:
      korai = sor.foglalas_ido
      nev1 = sor.vezetek
      nev2 = sor.uto
      lefoglalt = sor.lefoglalt_ido
      t.append(korai)
      t.append(nev1)
      t.append(nev2)
      t.append(lefoglalt)
  return t

legkorábban_lefoglalt_időpont = legkorábban_lefoglalt_időpont(lista)
print(legkorábban_lefoglalt_időpont)
