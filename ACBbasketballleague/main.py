'''
hazai	idegen	hazai_pont	idegen_pont	helysz�n	id�pont
7up Joventut	Adecco Estudiantes	81	73	Palacio Mun. De Deportes De Badalona	2005-04-03
'''

class Project():
    def __init__(self, sor):
        hazai, idegen, hazai_pont, idegen_pont, helyszin, idopont = sor.strip().split(";")
        self.hazai = hazai
        self.idegen = idegen
        self.hazai_pont = hazai_pont
        self.idegen_pont = idegen_pont
        self.helyszin = helyszin
        self.idopont = idopont
        
with open("eredmenyek.txt", "r", encoding="latin2") as f:
    cim_sor = f.readline()
    lista = [Project(sor) for sor in f]


#3
def csapatok(lista, csapat):
  hazai = [sor for sor in lista if sor.hazai == csapat]
  vendeg = [sor for sor in lista if sor.idegen == csapat]
  x = len(hazai) 
  y = len(vendeg)
  return csapat, x, y

csapatok = csapatok(lista, "Real Madrid")
print(f"{csapatok}")


#4
def volt_e_dotettlen(lista):
  dontettlen = [sor for sor in lista if sor.hazai_pont == sor.idegen_pont]
  if len(dontettlen) == 0:
    x = "4. Feladat: Volt döntettlen? Igen"
  else:
    y = "4. Feladat: Volt döntettlen? Nem"
  return x or y

volt_e_dotettlen = volt_e_dotettlen(lista)
print(volt_e_dotettlen)

#5
def csapat_neve(lista, csapat):
  neve = [sor.hazai for sor in lista if csapat in sor.hazai][0]
  return neve

csapat_neve = csapat_neve(lista, "Barcelona")
print(csapat_neve)
