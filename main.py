'''#amzius = 30
amzius = "30"
vardas = "Jonas"
ar_jonas_moka_programuoti = False
ar_registruotas = False
jono_pirkiniu_krepselio_suma = 34.5

"miau"
Multikomentaras


#print("amzius " + str(amzius))
print("Mano draugo vards yra " + vardas + " Jo amzius " + amzius, ar_jonas_moka_programuoti, jono_pirkiniu_krepselio_suma)
print(type(jono_pirkiniu_krepselio_suma))
'''
# vaisiai = ["Obuolys","Arbuzas","Bananas","Kriause"]
# print(vaisiai)
# print(type(vaisiai))
# ilgis = len(vaisiai)
# print(ilgis)
# print(vaisiai[1:2])
# pridedame_vaisiu = vaisiai.append("Melionas")
# vaisiai.insert(0,"Melionas")
#vaisiai[1]="Kivis"
# print(vaisiai)
# indeksas = vaisiai.index("Arbuzas")
#vaisiai.remove("Bananas")
# vaisiai.pop(2)
# print(vaisiai)
#dictionary - structure = my_dict = {key1:value1, key2:value2}

# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# zodynas["ar_studentas"] = True
# print(zodynas)
# del zodynas["Miestas"]
# print(zodynas)

# studentai ={
#     "Jonas": {
#         "Amzius": 32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#     },
#     "Ona": {
#         "Amzius": 25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#     },
#     "Antanas": {
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#     }
# }
#
# #print(studentai)
# print(studentai["Jonas"])

# studentai = [
#     {
#         "Vardas": "Jonas",
#         "Amzius": 32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#     },
#     {
#         "Vardas": "Ona",
#         "Amzius": 25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#     },
#     {
#         "Vardas": "Antanas",
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#     }
# ]
#
# naujas_studentas = {
#     "Vardas": "Petras",
#     "Amzius": 36,
#     "Miestas": "Kaunas",
#     "Profesija": "Siuvejas"
# }
#
# studentai.append(naujas_studentas)
# print(studentai)

#print(studentai)
#print(studentai[0])

#vaisiai = ["bananas", "kivis", "obuolys"]

# amzius = 20
# if not amzius < 18:
#     print("Asmuo yra pilnametis")
# elif amzius > 13:
#     print("Asmuo yra paauglys")
# else:
#     print("Asmuo nera pilnametis")

# vaisiai = ["obuolys", "kivis", "kriause"]
#
# if "kivis" in vaisiai:
#     print("Vaisius kivis")
# elif not "kivis" in vaisiai:
#     print("Vaisius nerastas")
# else:
#     print("Vaisiu sarasas tuscias")

# vaisiai = ["kriause"]
#
# if not vaisiai:
#     print("Vaisiu sarasas tuscias")
# elif"kivis" in vaisiai:
#     print("Vaisius kivis")
# else:
#     print("Vaisius kivis nerastas, taciau sarase yra elementu")

# age = 18
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("Gali balsuoti")
#     else:
#         print("Jums reikia asmens tapatybes korteles")
# else:
#     print("Jums dar negalima balsuoti")
#
# prekiu_kategorijos = ['Vaisiai', 'Mesa', 'Darzoves']
#
# print(f'Mano parduotuves prekiu kategorijos "{prekiu_kategorijos}" is kuriu galite rinktis')
#
# prekes = {
#     'Vaisiai': ['Obuoliai','Bananai'],
#     'Mesa': ['Kiauliena','Vistiena'],
#     'Darzoves': ['Bulves','Pomidorai']
# }
#
#
# norima_kategorija = 'Mesa'
# norima_preke = 'Vistiena'
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_preke in prekes[norima_kategorija]:
#         print(f"Parduotuveje yra {norima_preke}")
#     else:
#         print(f"Parduotuveje nera {norima_preke}")
# else:
#     print(f"Parduotuveje nera prekiu kategorijos ")

#1.1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi.
#1.2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi:
# "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).

# sarasas = [
#     {
#         "vardas": "Jonas",
#         "amzius": 20
#     },
#     {
#         "vardas": "Petras",
#         "amzius": 15
#     },
#     {
#         "vardas": "Zigmas",
#         "amzius": 10
#     }
# ]
# studentas = sarasas[2]
# #test_amzius = studentas["amzius"]
# #vardas = studentas["vardas"]
#
# if studentas["amzius"] > 18:
#     print(f'{studentas["vardas"]} yra pilnametis')
# elif studentas["amzius"] > 12:
#     print(f'{studentas["vardas"]} yra nepilnametis')
# else:
#     print(f'{studentas["vardas"]} yra vaikas')
#
# sarasas = {
#     "Jonas": {"amzius": 20},
#     "Petras": {"amzius": 15},
#     "Zigmas":{"amzius": 10}
# }
# test_vardas = "Zigmas"

#print(sarasas[test_vardas]["amzius"])

# if sarasas[test_vardas]["amzius"] > 18:
#     print(f'{test_vardas} yra pilnametis')
# elif sarasas[test_vardas]["amzius"] > 12:
#     print(f'{test_vardas} yra nepilnametis')
# else:
#     print(f'{test_vardas} yra vaikas')

# 2 užduotis:
# 1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
# 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"), padidinkite jo atlyginimą 10%.
# Jei jis nėra "inžinierius", palikite atlyginimą nepakeistą.

# darbuotojai = {
#     "Jonas": {
#         "atlyginimas": 1000,
#         "pareigos": "taksistas"
#     },
#     "Petras": {
#         "atlyginimas": 1500,
#         "pareigos": "inžinierius"
#     },
#     "Zigmas": {
#         "atlyginimas": 2000,
#         "pareigos": "programuotojas"
#     }
# }
#
#
#
# vardas = "Petras"
# darbuotojas = darbuotojai[vardas]
#
# print(vardas,darbuotojas["atlyginimas"])
# if darbuotojas["pareigos"] == "inžinierius":
#     darbuotojas["atlyginimas"] = darbuotojas["atlyginimas"] * 1.10
#     #darbuotojas["atlyginimas"] *= 1.10
# print(vardas, darbuotojas["atlyginimas"])

# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;

# knygos = [
#     {
#         "pavadinimas": "Tulpiu karalius",
#         "isl_metai": 1998
#     },
#     {
#         "pavadinimas": "Tigras karalius",
#         "isl_metai": 2010
#     },
#     {
#         "pavadinimas": "Netikras karalius",
#         "isl_metai": 1960
#     }
# ]
#
# kng_is_m = int(input("Kuriais metais isleista knyga?_>"))

knygos = [
    {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
    {"pavadinimas": "Ziedu valdovas", "isleidimo metai": 1997},
    {"pavadinimas": "Mody Dick", "isleidimo metai": 1851},
    {"pavadinimas": "Metai", "isleidimo metai": 2002}
]
knyga = knygos[0]
# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus, kuriu ieskote_> "))
# print(knyga_pagal_ieskomus_metus)
# if knyga["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knyga['pavadinimas']}")

try:
    knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))

    if knygos[0]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
        print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
    elif knygos[1]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
        print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
    elif knygos[2]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
        print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
    else:
        print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
except ValueError:
    print("Blogas ivesties formatas")