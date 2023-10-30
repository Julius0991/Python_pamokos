# importuojamos bibliotekos VISUOMET rasomos pirmose eilutese
# import os
#
# dabartinis_katalogas = os.getcwd()
# print(dabartinis_katalogas)
#
# norimas_aplankas = input ("Iveskite aplanko pavadinima, kurio turini norite matyti_> ")
#
# try:
#     #bandome gauti aplanko turini
#     turinys = os.listdir(norimas_aplankas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print (f"Deja aplankas '{norimas_aplankas}' nerastas")

# import os
#
# dabartinis_katalogas = os.getcwd()
# print(dabartinis_katalogas)
#
# #norimas_aplankas = input ("Iveskite aplanko pavadinima, kurio turini norite matyti_> ")
# naujas_katalogas = input("Prasome nurodyti katalogo lokacija_> ")
# keiciam_kataloga = os.chdir(naujas_katalogas)
# try:
#     #bandome gauti aplanko turini
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print (f"Deja aplankas '{naujas_katalogas}' nerastas")
#
# import os
#
# dabartinis_katalogas = os.getcwd()
# print(dabartinis_katalogas)
#
# #norimas_aplankas = input ("Iveskite aplanko pavadinima, kurio turini norite matyti_> ")
# naujas_katalogas = input("Prasome nurodyti katalogo lokacija_> ")
# try:
#     keiciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     #bandome gauti aplanko turini
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print (f"Deja aplankas '{naujas_katalogas}' nerastas")

import os
import shutil

EXTENSION_MAP = {
    '.jpg': "Images",
    '.jpeg': "Images",
    '.png': "Images",
    '.gif': "Images",
    '.pdf': "Documents",
    '.txt': "Documents"
}

filename = input("Please enter the name of the file you want to organize_> ")

file_extension = os.path.splitext(filename)[1]

try:
    if os.path.exists(filename) and file_extension in EXTENSION_MAP:
        directory_name = EXTENSION_MAP[file_extension]

        # create the directory if it does not exist
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        # move the file
        shutil.move(filename, os.path.join(directory_name,filename))
        print(f"{filename} has been moved to {directory_name}")
    else:
        print("The file does not exits or its extension is not recognized")
except FileNotFoundError:
    print(f"Error: {filename} was not found")
except PermissionError:
    print(f"Error: You don't have permissions to move '{filename}")