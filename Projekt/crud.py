from Projekt.data import pracownicy_wat, uczestnik_wat, pracownicy_AWL, uczestnik_AWL, pracownicy_poz, uczestnik_poz, wydarzenie_1, wydarzenie_2, wydarzenie_3
import requests
from bs4 import BeautifulSoup
import requests
import folium
import webbrowser
import os

def read(users):
    for user in users[0:]:
        print(f'Aktualne wydarzenia: {user["wydarzenie"]}')

def create_user(users: list[dict]) -> None:
    name: str = input("Podaj nazwe wydarzenia: ")
    location: str = input("Podaj miejsce wydarzenia: ")
    user: dict = {"wydarzenie": name, "location": location}
    users.append(user)
    read(users)

def remove(users:list[dict]) ->None :
    user_name: str = input("Jakie wydarzenie usunąć: ")
    for user in users[0:]:
        if user ["wydarzenie"]==user_name:
            users.remove(user)
            read(users)

def update(users: list[dict]) -> None:
    user_name: str = input("Wybierz wydarzenie: ")
    for user in users[0:]:
        if user["wydarzenie"] == user_name:
            new_user_name = input("Wprowadź nowe nazwę wydarzenia: ")
            user["wydarzenie"] = new_user_name
            new_user_location = input("Wprowadź nowe miejsce wydarzenia: ")
            user["location"] = new_user_location
            read(users)



def search(users: list[dict]) -> None:
    read(users)
    user_name: str = input("Wybierz wydarzenie: ")
    for user in wydarzenie_1:
        if user["event"] == user_name:
            while True:
                print("Menu:")
                print("0. Powrót:")
                print("1. Wyświetl pracowników wydarzenia: ")
                print("2. Wyświetl uczestników wydarzenia: ")
                print("3. Wyświetl uczestników wydarzenia: ")
                menu_option_1: str = input("Wybierz dostępną funkcje z menu: ")
                if menu_option_1 == "0":
                    break
                if menu_option_1 == "1":
                    read_pracownik_WAT(pracownicy_wat)
                if menu_option_1 == "2":
                    read_uczestnik_WAT(uczestnik_wat)
                if menu_option_1 == "3":
                    get_coords_WAT(wydarzenie_1)
    for user in wydarzenie_2:
        if user["event"] == user_name:
            while True:
                print("Menu:")
                print("0. Powrót:")
                print("1. Wyświetl pracowników wydarzenia: ")
                print("2. Wyświetl uczestników wydarzenia: ")
                print("3. Wyświetl uczestników wydarzenia: ")
                menu_option_1: str = input("Wybierz dostępną funkcje z menu: ")
                if menu_option_1 == "0":
                    break
                if menu_option_1 == "1":
                    read_pracownik_AWL(pracownicy_AWL)
                if menu_option_1 == "2":
                    read_uczestnik_AWL(uczestnik_AWL)
                if menu_option_1 == "3":
                    get_coords_AWL(wydarzenie_2)
    for user in wydarzenie_3:
        if user["event"] == user_name:
            while True:
                print("Menu:")
                print("0. Powrót:")
                print("1. Wyświetl pracowników wydarzenia: ")
                print("2. Wyświetl uczestników wydarzenia: ")
                print("3. Wyświetl uczestników wydarzenia: ")
                menu_option_1: str = input("Wybierz dostępną funkcje z menu: ")
                if menu_option_1 == "0":
                    break
                if menu_option_1 == "1":
                    read_pracownik_POZ(pracownicy_poz)
                if menu_option_1 == "2":
                    read_uczestnik_POZ(uczestnik_poz)
                if menu_option_1 == "3":
                    get_coords_POZ(wydarzenie_3)




# def search_mapa (users: list[dict]) -> None:


# Pracownicy

# Warszawa

def read_pracownik_WAT(pracownicy_wat: list[dict]) -> None:
    for wat in pracownicy_wat[0:]:
        print(f'Pracownik wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl pracowników wydarzenia: ")
        print("2. Dodaj pracownika wydarzenia: ")
        print("3. Usuń pracownika wydarzenia: ")
        print("4. Uaktualnij pracownika wydarzenia: ")
        print("5. Szczegóły pracowników wydarzenia: ")
        menu_option_2:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_2 == "0":
            break
        if menu_option_2 == "1":
            read_pracownik_WAT(pracownicy_wat)
        if menu_option_2 == "2":
            create_user_pracownik_WAT(pracownicy_wat)
        if menu_option_2 == "3":
            remove_pracownik_WAT(pracownicy_wat)
        if menu_option_2 == "4":
            update_pracownik_WAT(pracownicy_wat)
        # if menu_option_2 == "5":
        #     search_pracownik_WAT(pracownicy_wat)

def create_user_pracownik_WAT(pracownicy_wat: list[dict]) -> None:
    name: str = input("Podaj imię pracownika: ")
    surname: str = input("Podaj nazwisko pracownika: ")
    location: str = input("Podaj miasto pracownika: ")
    wat: dict = {"name": name, "surname": surname, "location": location}
    pracownicy_wat.append(wat)
    read_pracownik_WAT(pracownicy_wat)

def remove_pracownik_WAT(pracownicy_wat:list[dict]) ->None :
    user_name: str = input("Jakiego pracownika usunąć: ")
    for wat in pracownicy_wat[0:]:
        if wat ["name"]==user_name:
            pracownicy_wat.remove(wat)
            read_pracownik_WAT(pracownicy_wat)

def update_pracownik_WAT(pracownicy_wat: list[dict]) -> None:
    user_name: str = input("Wybierz Pracownika: ")
    for wat in pracownicy_wat[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię pracownika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko pracownika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe misto pracownika: ")
            wat["location"] = new_user_location
            read_pracownik_WAT(pracownicy_wat)



# Wrocław

def read_pracownik_AWL(pracownicy_AWL: list[dict]) -> None:
    for wat in pracownicy_AWL[0:]:
        print(f'Pracownik wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl pracowników wydarzenia: ")
        print("2. Dodaj pracownika wydarzenia: ")
        print("3. Usuń pracownika wydarzenia: ")
        print("4. Uaktualnij pracownika wydarzenia: ")
        print("5. Szczegóły pracowników wydarzenia: ")
        menu_option_2:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_2 == "0":
            break
        if menu_option_2 == "1":
            read_pracownik_AWL(pracownicy_AWL)
        if menu_option_2 == "2":
            create_user_pracownik_AWL(pracownicy_AWL)
        if menu_option_2 == "3":
            remove_pracownik_AWL(pracownicy_AWL)
        if menu_option_2 == "4":
            update_pracownik_AWL(pracownicy_AWL)
        if menu_option_2 == "5":
            get_cords_pracownik_WAT(pracownicy_AWL)

def create_user_pracownik_AWL(pracownicy_AWL: list[dict]) -> None:
    name: str = input("Podaj imię pracownika: ")
    surname: str = input("Podaj nazwisko pracownika: ")
    location: str = input("Podaj miasto pracownika: ")
    wat: dict = {"name": name, "surname": surname, "location": location}
    pracownicy_AWL.append(wat)
    read_pracownik_AWL(pracownicy_AWL)

def remove_pracownik_AWL(pracownicy_AWL:list[dict]) ->None :
    user_name: str = input("Jakiego pracownika usunąć: ")
    for wat in pracownicy_AWL[0:]:
        if wat ["name"]==user_name:
            pracownicy_AWL.remove(wat)
            read_pracownik_AWL(pracownicy_AWL)

def update_pracownik_AWL(pracownicy_AWL: list[dict]) -> None:
    user_name: str = input("Wybierz Pracownika: ")
    for wat in pracownicy_AWL[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię pracownika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko pracownika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe miasto pracownika: ")
            wat["location"] = new_user_location
            read_pracownik_AWL(pracownicy_AWL)

# Poznań

def read_pracownik_POZ(pracownicy_poz: list[dict]) -> None:
    for wat in pracownicy_poz[0:]:
        print(f'Pracownik wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl pracowników wydarzenia: ")
        print("2. Dodaj pracownika wydarzenia: ")
        print("3. Usuń pracownika wydarzenia: ")
        print("4. Uaktualnij pracownika wydarzenia: ")
        print("5. Szczegóły pracowników wydarzenia: ")
        menu_option_2:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_2 == "0":
            break
        if menu_option_2 == "1":
            read_pracownik_POZ(pracownicy_poz)
        if menu_option_2 == "2":
            create_user_pracownik_POZ(pracownicy_poz)
        if menu_option_2 == "3":
            remove_pracownik_POZ(pracownicy_poz)
        if menu_option_2 == "4":
            update_pracownik_POZ(pracownicy_poz)
        # if menu_option_2 == "5":
            # search_pracownik_POZ(pracownicy_poz)

def create_user_pracownik_POZ(pracownicy_poz: list[dict]) -> None:
    name: str = input("Podaj imię pracownika: ")
    surname: str = input("Podaj nazwisko pracownika: ")
    location: str = input("Podaj miasto pracownika: ")
    wat: dict = {"name": name, "surname": surname, "location": location}
    pracownicy_poz.append(wat)
    read_pracownik_POZ(pracownicy_poz)

def remove_pracownik_POZ(pracownicy_poz:list[dict]) ->None :
    user_name: str = input("Jakiego pracownika usunąć: ")
    for wat in pracownicy_poz[0:]:
        if wat ["name"]==user_name:
            pracownicy_poz.remove(wat)
            read_pracownik_POZ(pracownicy_poz)

def update_pracownik_POZ(pracownicy_poz: list[dict]) -> None:
    user_name: str = input("Wybierz Pracownika: ")
    for wat in pracownicy_poz[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię pracownika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko pracownika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe miasto pracownika: ")
            wat["location"] = new_user_location
            read_pracownik_POZ(pracownicy_poz)





# Uczestnicy

# Warszawa

def read_uczestnik_WAT(uczestnik_wat):
    for wat in uczestnik_wat [0:]:
        print(f'Uczestnicy wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl uczestników wydarzenia: ")
        print("2. Dodaj uczestnika wydarzenia: ")
        print("3. Usuń uczestnika wydarzenia: ")
        print("4. Uaktualnij uczestników wydarzenia: ")
        print("5. Szczegóły uczestników wydarzenia: ")
        menu_option_3:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_3 == "0":
            break
        if menu_option_3 == "1":
            read_uczestnik_WAT(uczestnik_wat)
        if menu_option_3 == "2":
            create_user_uczestnik_WAT(uczestnik_wat)
        if menu_option_3 == "3":
            remove_uczestnik_WAT(uczestnik_wat)
        if menu_option_3 == "4":
            update_uczestnik_WAT(uczestnik_wat)
        # if menu_option_3 == "5":
        #     search_uczestnik_WAT(uczestnik_wat)

def create_user_uczestnik_WAT(uczestnik_wat: list[dict]) -> None:
    name: str = input("Podaj imię pracownika: ")
    surname: str = input("Podaj nazwisko pracownika: ")
    location: str = input("Podaj miasto pracownika: ")
    wat: dict = {"name": name, "surname": surname, "location":location}
    uczestnik_wat.append(wat)
    read_uczestnik_WAT(uczestnik_wat)

def remove_uczestnik_WAT(uczestnik_wat:list[dict]) ->None :
    user_name: str = input("Jakiego pracownika usunąć: ")
    for wat in uczestnik_wat[0:]:
        if wat ["name"]==user_name:
            uczestnik_wat.remove(wat)
            read_uczestnik_WAT(uczestnik_wat)

def update_uczestnik_WAT(uczestnik_wat: list[dict]) -> None:
    user_name: str = input("Wybierz Pracownika: ")
    for wat in uczestnik_wat[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię pracownika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko pracownika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe miasto pracownika: ")
            wat["location"] = new_user_location
            read_uczestnik_WAT(uczestnik_wat)


# Wrocław

def read_uczestnik_AWL(uczestnik_AWL):
    for wat in uczestnik_AWL [0:]:
        print(f'Uczestnicy wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl uczestników wydarzenia: ")
        print("2. Dodaj uczestnika wydarzenia: ")
        print("3. Usuń uczestnika wydarzenia: ")
        print("4. Uaktualnij uczestników wydarzenia: ")
        print("5. Szczegóły uczestników wydarzenia: ")
        menu_option_3:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_3 == "0":
            break
        if menu_option_3 == "1":
            read_uczestnik_AWL(uczestnik_AWL)
        if menu_option_3 == "2":
            create_user_uczestnik_AWL(uczestnik_AWL)
        if menu_option_3 == "3":
            remove_uczestnik_AWL(uczestnik_AWL)
        if menu_option_3 == "4":
            update_uczestnik_AWL(uczestnik_AWL)
        # if menu_option_3 == "5":
        #     search_uczestnik_AWL(uczestnik_AWL)

def create_user_uczestnik_AWL(uczestnik_AWL: list[dict]) -> None:
    name: str = input("Podaj imię pracownika: ")
    surname: str = input("Podaj nazwisko pracownika: ")
    location: str = input("Podaj miasto pracownika: ")
    wat: dict = {"name": name, "surname": surname, "location": location}
    uczestnik_AWL.append(wat)
    read_uczestnik_AWL(uczestnik_AWL)

def remove_uczestnik_AWL(uczestnik_AWL:list[dict]) ->None :
    user_name: str = input("Jakiego pracownika usunąć: ")
    for wat in uczestnik_AWL[0:]:
        if wat ["name"]==user_name:
            uczestnik_AWL.remove(wat)
            read_uczestnik_AWL(uczestnik_AWL)

def update_uczestnik_AWL(uczestnik_AWL: list[dict]) -> None:
    user_name: str = input("Wybierz Pracownika: ")
    for wat in uczestnik_AWL[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię pracownika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko pracownika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe miasto pracownika: ")
            wat["location"] = new_user_location
            read_uczestnik_AWL(uczestnik_AWL)

# Poznań

def read_uczestnik_POZ(uczestnik_poz):
    for wat in uczestnik_poz [0:]:
        print(f'Uczestnicy wydarzenia: {wat["name"]} {wat["surname"]} {wat["location"]}')
    while True:
        print("Menu:")
        print("0. Powrót:")
        print("1. Wyświetl uczestników wydarzenia: ")
        print("2. Dodaj uczestnika wydarzenia: ")
        print("3. Usuń uczestnika wydarzenia: ")
        print("4. Uaktualnij uczestników wydarzenia: ")
        print("5. Szczegóły uczestników wydarzenia: ")
        menu_option_3:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option_3 == "0":
            break
        if menu_option_3 == "1":
            read_uczestnik_POZ(uczestnik_poz)
        if menu_option_3 == "2":
            create_user_uczestnik_POZ(uczestnik_poz)
        if menu_option_3 == "3":
            remove_uczestnik_POZ(uczestnik_poz)
        if menu_option_3 == "4":
            update_uczestnik_POZ(uczestnik_poz)
        # if menu_option_3 == "5":
        #     search_uczestnik_POZ(uczestnik_poz)

def create_user_uczestnik_POZ(uczestnik_poz: list[dict]) -> None:
    name: str = input("Podaj imię uczestnika: ")
    surname: str = input("Podaj nazwisko uczestnika: ")
    location: str = input("Podaj miasto uczestnika: ")
    wat: dict = {"name": name, "surname": surname, "location": location}
    uczestnik_poz.append(wat)
    read_uczestnik_POZ(uczestnik_poz)

def remove_uczestnik_POZ(uczestnik_poz:list[dict]) ->None :
    user_name: str = input("Podaj imię uczestnika do usunięcia: ")
    for wat in uczestnik_poz[0:]:
        if wat ["name"]==user_name:
                uczestnik_poz.remove(wat)
                read_uczestnik_POZ(uczestnik_poz)

def update_uczestnik_POZ(uczestnik_poz: list[dict]) -> None:
    user_name: str = input("Wybierz uczestnika: ")
    for wat in uczestnik_poz[0:]:
        if wat["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię uczestnika: ")
            wat["name"] = new_user_name
            new_user_surname = input("Wprowadź nowe nazwisko uczestnika: ")
            wat["surname"] = new_user_surname
            new_user_location = input("Wprowadź nowe miasto uczestnika: ")
            wat["location"] = new_user_location
            read_uczestnik_POZ(uczestnik_poz)


# kordy

# def get_coords_WAT(users):
#     for user in users:
#         location = user["location"]
#         adres_url = f'https://pl.wikipedia.org/wiki/{location}'
#         response = requests.get(adres_url)
#         response_html = BeautifulSoup(response.text, 'html.parser')
#         # print  (response_html)
#         latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
#         longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
#         print([latitude, longitude])
#         return latitude, longitude
#
# def get_coords_AWL(users):
#     for user in users:
#         location = user["location"]
#         adres_url = f'https://pl.wikipedia.org/wiki/{location}'
#         response = requests.get(adres_url)
#         response_html = BeautifulSoup(response.text, 'html.parser')
#         # print  (response_html)
#         latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
#         longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
#         print([latitude, longitude])
#         return latitude, longitude
# def get_coords_POZ(users):
#     for user in users:
#         location = user["location"]
#         adres_url = f'https://pl.wikipedia.org/wiki/{location}'
#         response = requests.get(adres_url)
#         response_html = BeautifulSoup(response.text, 'html.parser')
#         # print  (response_html)
#         latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
#         longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
#         print([latitude, longitude])
#         return latitude, longitude


def dms_to_decimal(dms):
    # Extract degrees, minutes, and seconds from the DMS string
    parts = re.split('[°′″]', dms)
    degrees = float(parts[0])
    minutes = float(parts[1]) if parts[1] else 0
    seconds = float(parts[2]) if parts[2] else 0
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    return decimal

#Funkcja do wydobywania współrzędnych geograficznych
def get_cords_pracownik_WAT(pracownicy_wat):
    name = input("Podaj nazwę restauracji, której lokalizację chcesz wyszukać: ")
    restaurant_found = False
    for user in pracownicy_wat:
        if user['name'] == name:
            adres_url = f'https://pl.wikipedia.org/wiki/{user["location"]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            # Extract latitude and longitude in DMS format
            latitude_dms = response_html.select('.latitude')[0].text
            longitude_dms = response_html.select('.longitude')[0].text

            # Convert DMS to decimal
            latitude = dms_to_decimal(latitude_dms)
            longitude = dms_to_decimal(longitude_dms)

            print([latitude, longitude])
            restaurant_found = True
            # Call the function to display a map
            display_map(latitude, longitude, pracownicy_wat["location"])
            return latitude, longitude
    if not restaurant_found:
        print(f"{pracownicy_wat["location"]} nie znaleziono na liście")

#Funkcja do do wyświetlania mapy
def display_map(latitude, longitude, miasto):
    # Create a map centered at the given latitude and longitude
    map_ = folium.Map(location=[latitude, longitude], zoom_start=12)
    # Add a marker for the city center
    for user in users:
        folium.Marker([latitude, longitude], tooltip=user["location"]).add_to(map_)
    # Save the map as an HTML file
    map_file = f"{miasto}_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))


#Funkcja do wyświetlana współrzędnych gościa
def get_cords_AWL(users):
    for user in users:
        if user['name'].lower() == name.lower():
            restaurant_found = True
            for guest in user['guests']:
                if 'city' not in guest or not guest['city']:
                    print(f"Gość {guest['name']} nie ma podanego miasta.")
                    continue

                adres_url = f'https://pl.wikipedia.org/wiki/{guest["city"][0]}'
                response = requests.get(adres_url)
                response_html = BeautifulSoup(response.text, 'html.parser')

                try:
                    latitude_dms = response_html.select('.latitude')[0].text
                    longitude_dms = response_html.select('.longitude')[0].text

                    # Convert DMS to decimal
                    latitude = dms_to_decimal(latitude_dms)
                    longitude = dms_to_decimal(longitude_dms)

                    guest_locations.append((guest["name"], guest["city"][0], latitude, longitude))
                    print(f"Koordynaty gościa {guest['name']}: [{latitude}, {longitude}]")
                except IndexError:
                    print(f"Koordynaty dla {guest['city'][0]} nie znalezione na Wikipedii.")
            break

    if restaurant_found and guest_locations:
        display_map_guests(guest_locations, name)
    elif not restaurant_found:
        print(f"Restauracja {name} nie została znaleziona na liście.")

#Funkcja do wyświetlenia mapy gościa
def display_map_guests(guest_locations, restaurant_name):
    if guest_locations:
        avg_latitude = sum([loc[2] for loc in guest_locations]) / len(guest_locations)
        avg_longitude = sum([loc[3] for loc in guest_locations]) / len(guest_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    # Add markers for each guest
    for name, city, latitude, longitude in guest_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city})"
        ).add_to(map_)

    # Save the map as an HTML file
    map_file = f"{restaurant_name}_guest_locations_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))


#Funkcja do określenia współrzędnych pracowników restauracji
def get_cords_workers(restaurants):
    name = input("Podaj nazwę restauracji, której lokalizację pracowników chcesz wyszukać: ")
    restaurant_found = False
    worker_locations = []

    for restaurant in restaurants:
        if restaurant['name'].lower() == name.lower():
            restaurant_found = True
            for worker in restaurant['workers']:
                if 'city' not in worker or not worker['city']:
                    print(f"Gość {worker['name']} nie ma podanego miasta.")
                    continue

                adres_url = f'https://pl.wikipedia.org/wiki/{worker["city"][0]}'
                response = requests.get(adres_url)
                response_html = BeautifulSoup(response.text, 'html.parser')

                try:
                    latitude_dms = response_html.select('.latitude')[0].text
                    longitude_dms = response_html.select('.longitude')[0].text

                    # Convert DMS to decimal
                    latitude = dms_to_decimal(latitude_dms)
                    longitude = dms_to_decimal(longitude_dms)

                    worker_locations.append((worker["name"], worker["city"][0], latitude, longitude))
                    print(f"Koordynaty gościa {worker['name']}: [{latitude}, {longitude}]")
                except IndexError:
                    print(f"Koordynaty dla {worker['city'][0]} nie znalezione na Wikipedii.")
            break

    if restaurant_found and worker_locations:
        display_map_workers(worker_locations, name)
    elif not restaurant_found:
        print(f"Restauracja {name} nie została znaleziona na liście.")

#Funkcja do wyświetlania mapy pracowników
def display_map_workers(worker_locations, restaurant_name):
    if worker_locations:
        avg_latitude = sum([loc[2] for loc in worker_locations]) / len(worker_locations)
        avg_longitude = sum([loc[3] for loc in worker_locations]) / len(worker_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    # Add markers for each guest
    for name, city, latitude, longitude in worker_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city})"
        ).add_to(map_)

    # Save the map as an HTML file
    map_file = f"{restaurant_name}_worker_locations_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))


def get_cords_all(restaurants):
    coordinates = []
    for restaurant in restaurants:
        adres_url = f'https://pl.wikipedia.org/wiki/{restaurant["city"]}'
        response = requests.get(adres_url)
        response_html = BeautifulSoup(response.text, 'html.parser')

        try:
            latitude_dms = response_html.select('.latitude')[0].text
            longitude_dms = response_html.select('.longitude')[0].text

            latitude = dms_to_decimal(latitude_dms)
            longitude = dms_to_decimal(longitude_dms)

            coordinates.append((latitude, longitude, restaurant["name"], restaurant["city"]))
            print(f'{restaurant["name"]} in {restaurant["city"]}: [{latitude}, {longitude}]')

        except (IndexError, ValueError) as e:
            print(f"Coordinates not found for {restaurant['name']} in {restaurant['city']}")

    if coordinates:
        display_map_all(coordinates)


def display_map_all(coordinates):
    # Center the map on Poland for better view
    map_ = folium.Map(location=[52.13, 19.40], zoom_start=6)

    for lat, lon, name, city in coordinates:
        folium.Marker([lat, lon], tooltip=f'{name}, {city}').add_to(map_)

    # Save the map as an HTML file
    map_file = f"restaurants_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))


def dms_to_decimal_guest_all(dms_str):
    """Convert DMS (degrees, minutes, seconds) to decimal format."""
    # Regular expression to match DMS strings
    dms_regex = re.compile(
        r"(?P<degrees>-?\d+)[°\s]"
        r"(?P<minutes>\d+)?[′\s]?"
        r"(?P<seconds>\d+(\.\d+)?|)[″\s]?"
        r"(?P<direction>[NSEW])?"
    )

    match = dms_regex.match(dms_str)
    if not match:
        raise ValueError(f"Invalid DMS string: {dms_str}")

    parts = match.groupdict()

    degrees = float(parts['degrees'])
    minutes = float(parts['minutes']) if parts['minutes'] else 0
    seconds = float(parts['seconds']) if parts['seconds'] else 0
    direction = parts['direction']

    decimal = degrees + minutes / 60 + seconds / 3600

    # Adjust for direction
    if direction in ('S', 'W'):
        decimal = -decimal

    return decimal

def get_cords_guests_all(restaurants):
    guest_locations = []

    for restaurant in restaurants:
        for guest in restaurant['guests']:
            if 'city' not in guest or not guest['city']:
                print(f"Gość {guest['name']} z restauracji {restaurant['name']} nie ma podanego miasta.")
                continue

            adres_url = f'https://pl.wikipedia.org/wiki/{guest["city"][0]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            try:
                latitude_dms = response_html.select('.latitude')[0].text
                longitude_dms = response_html.select('.longitude')[0].text

                # Convert DMS to decimal
                latitude = dms_to_decimal(latitude_dms)
                longitude = dms_to_decimal(longitude_dms)

                guest_locations.append((guest["name"], guest["city"][0], latitude, longitude, restaurant["name"]))
                print(f"Koordynaty gościa {guest['name']} z restauracji {restaurant['name']} w {guest['city'][0]}: [{latitude}, {longitude}]")
            except (IndexError, ValueError):
                print(f"Koordynaty dla {guest['city'][0]} nie znalezione lub błędne na Wikipedii.")

    if guest_locations:
        display_map_guests_all(guest_locations)
    else:
        print("Nie znaleziono żadnych lokalizacji gości.")

# Function to display map of all guests including restaurant name
def display_map_guests_all(guest_locations):
    if guest_locations:
        avg_latitude = sum([loc[2] for loc in guest_locations]) / len(guest_locations)
        avg_longitude = sum([loc[3] for loc in guest_locations]) / len(guest_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    # Add markers for each guest
    for name, city, latitude, longitude, restaurant in guest_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city}) - {restaurant}"
        ).add_to(map_)

    # Save the map as an HTML file
    map_file = f"all_guests_locations_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))



def dms_to_decimal_workers_all(dms_str):
    """Convert DMS (degrees, minutes, seconds) to decimal format."""
    dms_regex = re.compile(
        r"(?P<degrees>-?\d+)[°\s]"
        r"(?P<minutes>\d+)?[′\s]?"
        r"(?P<seconds>\d+(\.\d+)?|)[″\s]?"
        r"(?P<direction>[NSEW])?"
    )

    match = dms_regex.match(dms_str)
    if not match:
        raise ValueError(f"Invalid DMS string: {dms_str}")

    parts = match.groupdict()

    degrees = float(parts['degrees'])
    minutes = float(parts['minutes']) if parts['minutes'] else 0
    seconds = float(parts['seconds']) if parts['seconds'] else 0
    direction = parts['direction']

    decimal = degrees + minutes / 60 + seconds / 3600

    if direction in ('S', 'W'):
        decimal = -decimal

    return decimal


def get_cords_workers_all(restaurants):
    worker_locations = []

    for restaurant in restaurants:
        for worker in restaurant['workers']:
            if 'city' not in worker or not worker['city']:
                print(f"Pracownik {worker['name']} z restauracji {restaurant['name']} nie ma podanego miasta.")
                continue

            adres_url = f'https://pl.wikipedia.org/wiki/{worker["city"][0]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            try:
                latitude_dms = response_html.select('.latitude')[0].text
                longitude_dms = response_html.select('.longitude')[0].text

                # Convert DMS to decimal
                latitude = dms_to_decimal(latitude_dms)
                longitude = dms_to_decimal(longitude_dms)

                worker_locations.append((worker["name"], worker["city"][0], latitude, longitude, restaurant["name"]))
                print(f"Koordynaty pracownika {worker['name']} z restauracji {restaurant['name']} w {worker['city'][0]}: [{latitude}, {longitude}]")
            except (IndexError, ValueError):
                print(f"Koordynaty dla {worker['city'][0]} nie znalezione lub błędne na Wikipedii.")

    if worker_locations:
        display_map_workers_all(worker_locations)
    else:
        print("Nie znaleziono żadnych lokalizacji pracowników.")


# Function to display map of all workers
def display_map_workers_all(worker_locations):
    if worker_locations:
        avg_latitude = sum([loc[2] for loc in worker_locations]) / len(worker_locations)
        avg_longitude = sum([loc[3] for loc in worker_locations]) / len(worker_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    # Add markers for each worker
    for name, city, latitude, longitude, restaurant in worker_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city}) - {restaurant}"
        ).add_to(map_)

    # Save the map as an HTML file
    map_file = f"all_workers_locations_map.html"
    map_.save(map_file)
    # Open the map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))


# def dms_to_decimal(dms):
#     parts = dms.split('°')
#     degrees = float(parts[0])
#     parts = parts[1].split('′')
#     minutes = float(parts[0])
#     parts = parts[1].split('″')
#     seconds = float(parts[0])
#     direction = parts[1].strip()
#
#     decimal_degrees = degrees + minutes / 60 + seconds / 3600
#
#     if direction in ['S', 'W']:
#         decimal_degrees *= -1
#
#     return decimal_degrees
#
# def wydarzenia_mapa(users):
#     map = folium.Map(location=[52, 20], zoom_start=7)
#     for user in users:
#         wydarzenie = user['wydarzenie']
#         location = user['location']
#         url = f"https://pl.wikipedia.org/wiki/{location}"
#
#         response = requests.get(url)
#         response_html = BeautifulSoup(response.text, 'html.parser')
#
#         latitude_tag = response_html.find('span', {'class': 'latitude'})
#         longitude_tag = response_html.find('span', {'class': 'longitude'})
#
#         if latitude_tag and longitude_tag:
#             latitude = dms_to_decimal(latitude_tag.text)
#             longitude = dms_to_decimal(longitude_tag.text)
#             print(
#                 f" {wydarzenie}, Lokalizacja: {location}, Szerokość geograficzna: {latitude}, Długość geograficzna: {longitude}")
#             folium.Marker(
#                 location=[latitude, longitude],
#                 popup=f"{wydarzenie},\n{location}",
#                 icon=folium.Icon(color='red')
#             ).add_to(map)
#
#
#     map_dir = 'models/maps'
#     os.makedirs(map_dir, exist_ok=True)
#
#     map_file = os.path.join(map_dir, 'location.html')
#     map.save(map_file)
#     webbrowser.open(map_file)
#
