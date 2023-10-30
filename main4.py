# class Automobilis:
#     def __init__(self, marke, modelis, metai, variklio_turis, kuro_tipas):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.variklio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 200
#
#     def automobilio_pavadinimas(self):
#         return f"Automobilis: {self.marke}\nAutomobilio marke: {self.modelis}\nAutomobilio_pagaminimo_metai: {self.metai}"
#
#     def vaziuoti(self, km):
#         self.rida += km
#         return  f"Vaziuojama {km}km. Bendra rida {self.rida}km"
#
# auto1 = Automobilis("Audi","A8",2021, 3.0, "Benzinas")
# auto2 = Automobilis("Subaru", "Outback", 2015, 2.5, "Dyzelinas")
# print(auto1.automobilio_pavadinimas())
# print(auto1.vaziuoti(150))
#
# class Gyvunas:
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.svoris = svoris
#         self.rusis = rusis
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_aprasymas(self):
#         return f"Gyvunas {self.rusis}\nSvoris {self.svoris}\nAmzius {self.amzius}\nVardas {self.vardas}"
#     def valgyti(self):
#         return f"{self.vardas} valgo"
#
#     def prisistatymas(self):
#         return f"AS esu {self.rusis}. Mano vardas {self.vardas}."
#
# kate = Gyvunas("Siamo katinas",5,5,"Alikas")
# print(kate.gyvuno_aprasymas())
# print(kate.valgyti())
# print(kate.prisistatymas())

# from colorama import init, Fore
#
# init()
#
# class Uzduotis:
#     def __init__(self,pavadinimas, aprasymas):
#         self.pavadinimas = pavadinimas
#         self.aprasymas = aprasymas
#         self.atlikta = False
#
#     def atlikimas(self):
#         self.atlikta = True
#         print(f"{Fore.GREEN}Uzduotis '{self.pavadinimas}' buvo atlikta")
#
#     def info(self):
#         return f"{Fore.CYAN}Pavadinimas {self.pavadinimas},\nAprasymas: {self.aprasymas}\n"
#
# class TodoSarasas:
#     def __init__(self):
#         self.uzduociu_sarasas = []
#
#     def prideti_uzduoti(self,pavadinimas,aprasymas):
#         uzduotis = Uzduotis(pavadinimas,aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print(Fore.RED,"Uzduociu sarasas yra tuscias ")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self,pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas == pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print(f"Uzduotis pavadinimu: '{pavadinimas}' nerasta")
#
# todo_sarasas = TodoSarasas()
#
# while True:
#     print("\nPasirinkite veiksma:")
#     print("1. Prideti uzduoti")
#     print("2. Perziureti uzduotis")
#     print("3. Pazymeti uzduoti kaip atlikta")
#     print("4. Iseiti is uzduociu saraso")
#     pasirinkimas = input()
#
#     if pasirinkimas == "1":
#         pavadinimas = input("Iveskite uzduoties pavadinima_>")
#         aprasymas = input("Iveskite uzduoties aprasyma_>")
#         todo_sarasas.prideti_uzduoti(pavadinimas,aprasymas)
#         print("Uzduotis prideta sekmingai!")
#
#     elif pasirinkimas == "2":
#         todo_sarasas.visos_uzduotys()
#     elif pasirinkimas == "3":
#         pavadinimas = input("Iveskite uzduoties pavadinima, kuria norite pazymeti kaip atlikta")
#         todo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas == "4":
#         print(Fore.YELLOW,"Iseinama...")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")

# class Saskaita:
#     def __init__(self,vardas,pavarde,likutis = 0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.likutis = likutis
#     def info(self):
#         print(f"Saskaitos turetojo vardas: '{self.vardas}' pavarde: '{self.pavarde}' likutis: '{self.likutis}' ")
#
#     def inesti(self, suma):
#         if suma > 0:
#             self.likutis += suma
#             print(f"Jus sekmingai idejote '{suma}' pinigu")
#         else:
#             print("Klaida! Negalima ideti neigiamos sumos.")
#
#     def nusiimti_pinigu(self, suma):
#         print(f"Bandoma nusimti '{suma}' pinigu")
#         if suma < 0:
#             print("Klaida! Negalima nusiimti neigiamos sumos.")
#         elif suma > self.likutis:
#             #print("Suma didesne uz likuti")
#             print(f"Klaida! Operacijai saskaitoje pinigu neuztenka. Saskaitoje yra '{self.likutis}' o bandoma nusiimti '{suma}'. ")
#         else:
#             #print("Suma mazesne arba lygi uz likuti")
#             self.likutis -= suma
#             print(f"Jus sekmingai isemete '{suma}' pinigu")
#
# s1 = Saskaita("Julius", "Serbenta")
# s1.info()
# s1.inesti(400)
# s1.nusiimti_pinigu(200)
# s1.info()

# class studentas:
#     def __init__(self, vardas, pavarde, amzius, studento_numeris,pazymiu_sarasas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#         self.studento_numeris = studento_numeris

# class Studentas:
#     def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai=None):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#         self.studento_numeris = studento_numeris
#         self.pazymiai = pazymiai if pazymiai else []
#
#     def studento_vidurkis(self):
#         return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0
#
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#
#     def studento_informacija(self):
#         return (f'Studento vardas {self.vardas}, studento pavarde {self.pavarde}, amzius {self.amzius}, '
#                 f'studento numeris {self.studento_numeris}, pazymiai {self.pazymiai}')
#
#     def pasalinti_pazymi(self,pazymys):
#         if 0 <= pazymys < len(self.pazymiai):
#             del self.pazymiai[pazymys]
#         else:
#             print("Toks pazymys nerastas")
#
# class StudentuValdymoSistema:
#     def __init__(self):
#         self.studentu_sarasas = []
#
#     def prideti_studenta(self, studentas):
#         self.studentu_sarasas.append(studentas)
#         print("Studentas sekmingai pridetas")
#
#     def pasalinti_studenta(self,studento_numeris):
#         naujas_studentu_sarasas = []
#         for s in self.studentu_sarasas:
#             if s.studento_numeris != studento_numeris:
#                 naujas_studentu_sarasas.append(s)
#         self.studentu_sarasas = naujas_studentu_sarasas
#
#     def visi_studentai(self):
#         return self.studentu_sarasas
#
#     def __str__(self):
#         return "\n ".join(str(studentas) for studentas in self.studentu_sarasas)
#
# studentu_sistema = StudentuValdymoSistema()
# studentas1 = Studentas("Jonas", "Jonaitis", 23, 102)
# studentas2 = Studentas("Petras", "Petraitis", 21, 105)
# studentas1.prideti_pazymi(7)
# studentas1.prideti_pazymi(3)
# studentas1.prideti_pazymi(5)
# studentas2.prideti_pazymi(8)
# studentas2.prideti_pazymi(6)
# print(studentas1.studento_informacija())
# studentas1.pasalinti_pazymi(0)
# print(studentas1.studento_informacija())
# print(studentas2.studento_informacija())
# studentu_sistema.pasalinti_studenta(105)
#
# for studentas in studentu_sistema.visi_studentai():
#     print(studentas)

# Sukurkite metoda kuris isves studento vidurki;
# sukurkite metoda kad galetumete prideti studenta;
# Sukurkite metoda kad galetumete prideti pazymi studentui;
# Sukurkite metoda kad galetumete pasalinti pazymi;
# Sukurkite metoda kuris grazins visa studento info;
# Sukurkite metoda kuris pasalintu studenta;
# Sukurkite metoda kad galetumete rikiuoti studentus pagal jų pažymių vidurkį, vardą ar kitą kriterijų.
# Sukurkite metoda leidžianti filtruoti studentus pagal jų pažymių vidurkį (pvz., visi studentai, kurių vidurkis didesnis už 8).

class Studentas:
    def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai=None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.studento_numeris = studento_numeris
        self.pazymiai = pazymiai if pazymiai else []

    def studento_vidurkis(self):
        return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0

    def prideti_pazymi(self, pazymys):
        self.pazymiai.append(pazymys)

    def studento_informacija(self):
        return (f'Studento vardas {self.vardas}, studento pavarde {self.pavarde}, amzius {self.amzius}, '
                f'studento numeris {self.studento_numeris}, pazymiai {self.pazymiai}')

    def pasalinti_pazymi(self,pazymys):
        if 0 <= pazymys < len(self.pazymiai):
            del self.pazymiai[pazymys]
        else:
            print("Toks pazymys nerastas")



class StudentuValdymoSistema:
    def __init__(self):
        self.studentu_sarasas = []

    def prideti_studenta(self, studentas):
        self.studentu_sarasas.append(studentas)
        print("Studentas sekmingai pridetas")

    def pasalinti_studenta(self,studento_numeris):
        naujas_studentu_sarasas = []
        for s in self.studentu_sarasas:
            if s.studento_numeris != studento_numeris:
                naujas_studentu_sarasas.append(s)
        self.studentu_sarasas = naujas_studentu_sarasas

    def filtravimas_pagal_vidurki(self, ivestas_vidurkis):

        for i in self.visi_studentai():
            if i.studento_vidurkis() > ivestas_vidurkis:
                print(i.studento_informacija())

    def rikiavimas(self, ):

    def visi_studentai(self):
        return self.studentu_sarasas

    # def __str__(self):
    #     return "\n ".join(str(studentas) for studentas in self.studentu_sarasas)

studentu_sistema = StudentuValdymoSistema()
studentas1 = Studentas("Jonas", "Jonaitis", 23, 102)
studentas2 = Studentas("Petras", "Petraitis", 21, 105)
studentas1.prideti_pazymi(7)
studentas1.prideti_pazymi(3)
studentas1.prideti_pazymi(5)
studentas2.prideti_pazymi(8)
studentas2.prideti_pazymi(6)
print(studentas1.studento_informacija())
studentas1.pasalinti_pazymi(0)
print(studentas1.studento_informacija())
print(studentas2.studento_informacija())
studentu_sistema.prideti_studenta(studentas1)
studentu_sistema.prideti_studenta(studentas2)

studentu_sistema.filtravimas_pagal_vidurki(3)

# for i in studentu_sistema.visi_studentai():
#     if i.studento_vidurkis() > 5:
#         print(i.studento_informacija())
#studentu_sistema.pasalinti_studenta(105)

# for studentas in studentu_sistema.visi_studentai():
#     print(studentas)