# with open("text.txt", "a") as f:
#     content = f.write("Hello world")

# with open("text.txt", "r") as f:
#     content = f.read()
#     print(content)

# with open("text.txt", "a") as f:
#     content = f.write("Dar viena texto eilute")

# import requests
# from bs4 import BeautifulSoup
#import psycopg2

# headers = {
#     "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
#     "Cookie": "_ga_R9Y1176PTY=GS1.1.1698653079.1.0.1698653079.60.0.0; _ga=GA1.2.1969605624.1698653080; _gid=GA1.2.700276596.1698653080; _gat_UA-11759603-3=1; cf_clearance=exV8I.KqiG0eXLZ.F4jpFO1Z68OL8XT16N8Pmza4SkI-1698653080-0-1-2d004182.d2292f1f.7a011e62-160.2.1698653080; soundestID=20231030080444-LFUpNxjNuWOx7IvYHSExoEPZXsIOFJ1JdiICbgacVdoTsd68Z; omnisendSessionID=6W8glStI4nkFua-20231030080444; page-views=1; _fw_crm_v=a1d0e2fe-fc12-459f-aa15-f91d6dcaeb23; CookieConsent={stamp:%27P3hFz98Eqy3GL63NII3fKbivx1cXIFveRUDej8sHUWpyBPpduh9V+Q==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1698653094526%2Cregion:%27pl%27}; neocsrftoken=84NjjlfSZerRC7gOSmcEHqTnFVSV8kvoE4OLHEqbxKkrnsXACNXKzGVvDVuDK04x"
# }
# url = "https://aruodas.lt"
#response = requests.get(url,headers= headers)
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
#
# content_block = soup.find('div', class_="top-three-adverts__wrapper").text.strip()

# flats_data = []



# print(content_block)
#print(response.status_code)
# print(response.content.strip())

# url = "https://aruodas.lt"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
#
# content_block = soup.find_all('div', class_="top-three-adverts__wrapper")
#
# flats_data = []
#
# for content in content_block:
#     print("Content starts ",content, " content ends")
# #    flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
# #    flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()
#
#     #flats_data.append((flat_title, flat_price))
#
# #print(flats_data)
# #print(content_block)
# import requests
# from bs4 import BeautifulSoup
# import psycopg2
#
# flats_data = []
# def create_and_insert_flats():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="aruodas_info",
#         user="postgres",
#         password="[jUl1u5]"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_top (
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("Table created successfully!")
#
#
#
#     url = "https://aruodas.lt"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     content_block = soup.select('div.top-three-adverts__wrapper div')
#
#     for content in content_block:
#         try:
#             flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()\
#                 .replace("€","").replace(" ","").split(sep="-")[0]
#             print(flat_title,flat_price)
#
#             #print(flat_title, flat_price)
#             #flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO aruodas_top (flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query,(flat_title, flat_price))
#         except AttributeError:
#             continue
#     print("Flats inserted successfully")
#
#     connection.commit()
#
# create_and_insert_flats()

# import requests
# from bs4 import BeautifulSoup
# import psycopg2
#
# flats_data = []
# def create_and_insert_flats():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="aruodas_info",
#         user="postgres",
#         password="[jUl1u5]"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS uzsienio_objektai (
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("Table created successfully!")


# connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="aruodas_info",
#         user="postgres",
#         password="[jUl1u5]"
#     )
#
# cursor = connection.cursor()
#
# create_table_query = """
#     CREATE TABLE IF NOT EXISTS uz_obj (
#         id SERIAL primary key,
#         flat_title VARCHAR(300),
#         flat_price DECIMAL(10,2)
#         )
# """
#
# cursor.execute(create_table_query)
# print("Table created successfully!")

#     url = "https://aruodas.lt/uzsienio-objektai"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     content_block = soup.select('div.project-list-content div')
#
#     for content in content_block:
#         try:
#             flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
#             flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()\
#                 .replace("€","").replace(" ","").split(sep="-")[0]
#             print(flat_title,flat_price)
#
#             #print(flat_title, flat_price)
#             #flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO uzsienio_objektai (flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query,(flat_title, flat_price))
#         except AttributeError:
#             continue
#     print("Flats inserted successfully")
#
#     connection.commit()
#
# create_and_insert_flats()

# kuriame patys su kitais objektais:

import requests
from bs4 import BeautifulSoup
import psycopg2

flats_data = []
def create_and_insert_flats():
    #kuriam connectiona prie duomenu bezes:
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "aruodas_info",
        user="postgres",
        password = "[jUl1u5]"
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
        )
    """

    cursor.execute(create_table_query)
    print("Table created Successfully!")


    url = "https://www.aruodas.lt/uzsienio-objektai/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content_block = soup.select('div.project-list-content div')

    #ct = 0
    #print("Ilgis yra ", len(content_block))
    for content in content_block:
        print("Content start\n", content, " \nContent end\n")
        try:
            #print("Content yra ",content)
            flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
            print("Flat_title yra ", flat_title)
            flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()\
                .split(sep="Kaina:")[1].replace(" ", "").replace("€", "")
            print("Flat_price yra ", flat_price)
            # print(flat_title, flat_price)
            #if flat_title and flat_price:
                #print("ft", flat_title, "fp", flat_price,)

            # flats_data.append((flat_title, flat_price))
            insert_query = "INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)"
            cursor.execute(insert_query, (flat_title, flat_price))

        except AttributeError:
            continue
    print("Flats inserted successfully!")
    #print("Ct yra ", ct)


    connection.commit()

create_and_insert_flats()

