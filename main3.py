# 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.

# prekes = [
#     {
#         "preke": "preke1",
#         "kaina": 10
#     },
#     {
#         "preke": "preke2",
#         "kaina": 20
#     },
#     {
#         "preke": "preke3",
#         "kaina": 30
#     }
# ]
#
# brang_prek_kaina = prekes[0]["kaina"]
# brang_preke = prekes[0]["preke"]
# print("Pradine brangiausia preke",prekes[0]["preke"])
# if prekes[1]["kaina"] > brang_prek_kaina:
#     brang_preke = prekes[1]["preke"]
#     print("Brangiausia preke dabar yra", brang_preke)
# if prekes[2]["kaina"] > brang_prek_kaina:
#     brang_prek_kaina = prekes[2]["preke"]
#     print("Brangiausia preke dabar yra", brang_preke)
# print("Brangiausia preke yra",brang_prek_kaina)

# 2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas išlaikė egzaminą;

# stud_paz = [
#     {
#         "vardas": "vardas1",
#         "pazymys": 10
#     },
#     {
#         "vardas": "vardas2",
#         "pazymys": 5
#     },
#     {
#         "vardas": "vardas3",
#         "pazymys": 3
#     }
# ]
# if stud_paz[0]["pazymys"] >= 4:
#     print(f'{stud_paz[0]["vardas"]} egzamina islaike')
# else:
#     print(f'{stud_paz[0]["vardas"]} egzamino neislaike')
# if stud_paz[1]["pazymys"] >= 4:
#     print(f'{stud_paz[1]["vardas"]} egzamina islaike')
# else:
#     print(f'{stud_paz[1]["vardas"]} egzamino neislaike')
# if stud_paz[2]["pazymys"] >= 4:
#     print(f'{stud_paz[2]["vardas"]} egzamina islaike')
# else:
#     print(f'{stud_paz[2]["vardas"]} egzamino neislaike')


# 3. Sukurkite žodyną su kliento informacija ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.

# kl_inf = {
#     "vardas1":{
#         "lesos": 100,
#         "prk_k": 50
#     },
#     "vardas2":{
#         "lesos": 200,
#         "prk_k": 150
#     },
#     "vardas3":{
#         "lesos": 300,
#         "prk_k": 400
#     }
# }
# if kl_inf["vardas1"]["lesos"] >= kl_inf["vardas1"]["prk_k"]:
#     print(f'{"vardas1"} preke nusipirkti gali')
# else:
#     print(f'{"vardas1"} prekes nusipirkti negali')
# if kl_inf["vardas2"]["lesos"] >= kl_inf["vardas2"]["prk_k"]:
#     print(f'{"vardas2"} preke nusipirkti gali')
# else:
#     print(f'{"vardas2"} prekes nusipirkti negali')
# if kl_inf["vardas3"]["lesos"] >= kl_inf["vardas3"]["prk_k"]:
#     print(f'{"vardas3"} preke nusipirkti gali')
# else:
#     print(f'{"vardas3"} prekes nusipirkti negali')






# 4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles:
# pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

pajamos = 5100
if pajamos > 5000:
    print("Mokesciai bus lygus " + str(pajamos * 0.2))
elif pajamos > 1001:
    print("Mokesciai bus lygus " + str(pajamos * 0.15))
else:
    print("Mokesciai bus lygus " + str(pajamos * 0.1))



# for i in range(5):
#     print("Skaicius",i)
#
# tekstas = 'Python data science'
# for raide in tekstas:
#     print(raide)

# zodynas = {"a": 1, "b":2, "c":3}
#
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])

# skaiciai = [10,20,30,40,50]
# suma = sum(skaiciai)
# vidurkis = suma/len(skaiciai)
# for sk in skaiciai:
#     if sk > vidurkis:
#         print(sk)

# sarasas = ["jonas","antanas","ona","marija"]
# for v in sarasas:
#     print(v)
#
# print('\n'.join(sarasas))

# tekstas = "Python"
# n_tekstas = ''
# for i in tekstas:
#     n_tekstas = i + n_tekstas
# print(n_tekstas)



# tekstas = "Python"
# print(len(tekstas))
# print(tekstas[len(tekstas)-1])
# print(tekstas[-1])

# max_sk = 10
# for i in range(1,max_sk+1):
#     for j in range(1,max_sk+1):
#         print(i*j, end='\t')
#     print()

# sarasas = ['Labas', 'rytas','mieli','mokiniai']
# print(sarasas)
# n_sarasas = ''
# for i in sarasas:
#     n_sarasas = n_sarasas + i + ' '
# print(n_sarasas.rstrip())
#
# sarasas = ['Labas', 'rytas','mieli','mokiniai']
# print(sarasas)
# for i in sarasas:
#     print(i, end=' ')

# skaicius = 1
#
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1


# atsakymas = 5
# spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
#
# while spejimas != atsakymas:
#     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta_>"))
# print("Sveikiname, atspejote!")

# ar_veikia = True

#while ar_veikia
# while True:
#     print("----Meniu----")
#     print("1. Atspausdinti pasveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3)_>")
#     if pasirinkimas == '1':
#         print('Labas!')
#     elif pasirinkimas == '2':
#         vardas = input("Iveskite nauja varda_>")
#
#         print("Sekmingai ivedete nauja varda!")
#         print(f'Jusu vardas pakeistas i {vardas}')
#     elif pasirinkimas == '3':
#         print("Aciu, kad naudojotes programa. IKI!")
#         break
#         #ar_veikia = False
#     else:
#         print("Neteisingas pasirinkimas. Bandykite dar karta.")


# slaptz = 'zodis'
#
# band = input('Pabandyk atspeti paslaptinga zodi_>')
# # while True:
# #     if band != slaptz:
# #         band = input('Neatspejai. Bandyk vel_>')
# #     else:
# #         print("Valio! Atspejai")
# #         break
#
# while band != slaptz:
#     band = input('Neatspejai. Bandyk vel_>')
# print("Valio! Atspejai")


#max_skaicius = int(input("Prasome ivesti max skaiciu daugybos lentelei sudaryti_>"))

# for i in range(1, max_skaicius + 1):
#     for j in range(1, max_skaicius +1):
#         print(str(i) + 'x' + str(j) + '=' + str(i*j), end='\t')
#     print()

# i = 1
# j = 1
# while i <= max_skaicius:
#     while j <= max_skaicius:
#         print(str(i) + 'x' + str(j) + '=' + str(i * j), end='\t')
#         j += 1
#     print()
#     i += 1
#     j = 1

# pasirenkamas_skaicius = int(input("pasirinkite skiaciu nuo 1 iki 10->"))
#
# x = range(1,11)
# for i in x:
#     rezultatas = pasirenkamas_skaicius * i
#     print(i, "x", pasirenkamas_skaicius, "=", rezultatas)

# def pasisveikinti(vardas):
#     print(f'Labas')
#
# pasisveikinti('Julius')

# if __name__ == '__main__':
#     pasisveikinti()

# def sum(a,b):
#     return a+b
#
# 5
#
# sum(5,3)

# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knyga")
#     print("2. Perziureti visas knygas")
#     print("3. Ieskoti knygos pagal pavadinima")
#     print("4. Iseiti")
#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskite knygos autoriu_>")
#     knygu_sarasas.append({"pavadinimas":pavadinimas,"autorius":autorius})
#     print(f"Knyga '{pavadinimas}' prideta")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima, kurios ieskote_>")
#     #print("Pavadinimas ivestas: ",ieskomas_pavadinimas)
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'.lower()]]
#     #print("Knygos rastos", rasti_knygas)
#     if rasti_knygas:
#         #print("Yra rastu knygu")
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#     else:
#         print(f"Knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma (1-4)_>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             print("Iki greito!")
#             break
#
# if __name__ == '__main__':
#     main()

#bankine sistema atidaryt/uzdaryt saskaitaidet,isimt pinigus,

#bankine sistema. mes galime atidaryti sas, inesti pin, nusiimti pin, perziureti liktui, uzdaryti sas, iseiti is sistemos:

# banko_saskaitos = {
#
#
# }
# def rodyti_meniu():
#     print("\n=== Mini Banko sistema ===")
#     print("1. Atidaryti naują saskaitą")
#     print("2. Įnešti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Peržiūrėti sąskaitos likutį")
#     print("5. Uždaryti sąskaitą")
#     print("6. Išeiti")
#
# def prideti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite vardą: ")
#     pradinis_likutis = int(input("Įveskite pradinį pinigų likutį: "))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja sąskaita '{saskaitos_nr}' sekmingai prideta!")
#
# def inesti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite įnešamų pinigų sumą: "))
#     banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
#     print(f"Į sąskaitą nr.: '{saskaitos_nr}' sėkmingai įnešta '{suma}' eurai")
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite nusiimamų pinigų sumą: "))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Iš sąskaitos nr.: '{saskaitos_nr}' sėkmingai nusiimta '{suma}' eurai")
#     else:
#         print(f"Jūsų pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"Sąskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")
#
# def istrinti_saskaita(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko sąskaita nr.: '{saskaitos_nr}' buvo ištrinta")
#
#
# def main():
#     paslaugos = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksmą(1-4): ")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")
#
# main()

# def atd_sask(s_sar):
#     vardas = input("Iveskite saskaitos turetojo varda_>")
#     s_lik = float(input("Iveskite pradini saskaitos likuti_>"))
#     s_sar.append({"saskaitos_turetojas":vardas, "saskaitos_likutis": s_lik})
#     print(f"Klientui '{vardas}' prideta saskaita; pinigu likutis joje: '{s_lik}'")
#
# def in_pin(s_sar):
#     vardas = input("Kieno vardu bus ideti pinigai?_>")
#     s_in = float(input("Kiek pinigu noretumete inesti?_>"))
#     for i in s_sar:
#         if i["saskaitos_turetojas"] == vardas:
#             temp = i
#             i["saskaitos_likutis"] += s_in
#     print(f"Kliento '{vardas}' vardu buvo inesta '{s_in}' pinigu. Naujas pinigu likutis joje: '{temp["saskaitos_likutis"]}'")
#
# def nus_pin(s_sar):
#         vardas = input("Kieno vardu bus nuimami pinigai?_>")
#         s_num = float(input("Kiek pinigu noretumete nuimti?_>"))
#         while True:
#             for i in s_sar:
#                 if i["saskaitos_turetojas"] == vardas:
#                     temp = i
#                     i["saskaitos_likutis"] -= s_num
#             if temp["saskaitos_likutis"] < 0:
#                 i["saskaitos_likutis"] += s_num
#                 s_num = float(input("Siam veiksmui saskaitoje per mazai pinigu. Kiek pinigu noretumete nuimti?_>"))
#             else:
#                 break
#         print(f"Kliento '{vardas}' vardu buvo inesta '{s_num}' pinigu. Naujas pinigu likutis joje: '{temp["saskaitos_likutis"]}'")
#
# def perz_lik(s_sar):
#     temp = False
#     vardas = input("Kienu vardu noretumete pamatyti likuti?_>")
#     #print("Ivestas vardas: ",vardas)
#     for i in s_sar:
#         print(i)
#         if i["saskaitos_turetojas"] == vardas:
#             print("Saskaitos turetojas yra")
#             temp = i
#     if temp != False:
#         print(f"Kliento '{vardas}' saskaitoje siuo metu yra '{temp["saskaitos_likutis"]}' pinigu.")
#     else:
#         print("Tokios saskaitos nera")
#
# def uzd_sask(s_sar):
#     temp = False
#     vardas = input("Kienu vardu noretumete uzdaryti saskaita?_>")
#     for i in s_sar:
#         if i["saskaitos_turetojas"] == vardas:
#             temp = i
#         if temp != False:
#             s_sar.remove(i)
#             print(f"Kliento '{vardas}' saskaita buvo istrinta.")
#         else:
#             print("Tokios saskaitos nera")
#
#
# #     )pavadinimas = input("Iveskite knygos pavadinima_>"
# #     autorius = input("Iveskite knygos autoriu_>")
# #     knygu_sarasas.append({"pavadinimas":pavadinimas,"autorius":autorius})
# #     print(f"Knyga '{pavadinimas}' prideta")
#
# def rodyti_meniu():
#     print("-----Mini banko sistema-----")
#     print("1. Atidaryti nauja saskaita")
#     print("2. Inesti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Perziureti saskaitos likuti")
#     print("5. Uzdaryti saskaita")
#     print("6. Iseiti")
#
# sask_sar = []
#
# def main():
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma (1-6)_>")
#         if pasirinkimas == "1":
#             atd_sask(sask_sar)
#         elif pasirinkimas == "2":
#             in_pin(sask_sar)
#         elif pasirinkimas == "3":
#             nus_pin(sask_sar)
#         elif pasirinkimas == "4":
#             perz_lik(sask_sar)
#         elif pasirinkimas == "5":
#             uzd_sask(sask_sar)
#         elif pasirinkimas == "6":
#             print("Geros dienos")
#             break
#
# if __name__ == '__main__':
#     main()
#
#

def pvm_skaiciuokle(kaina):
    print("Kaina su PVM", kaina*1.21)
    return kaina*1.21

pvm_skaiciuokle(10)
print(pvm_skaiciuokle(10))