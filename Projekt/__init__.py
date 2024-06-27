from Projekt.crud import  read, create_user, remove, update, search, read_pracownik_WAT, read_pracownik_POZ, read_pracownik_AWL, read_uczestnik_WAT, read_uczestnik_AWL, read_uczestnik_POZ, create_user_pracownik_WAT, remove_pracownik_WAT, update_pracownik_WAT, create_user_pracownik_AWL, remove_pracownik_AWL, update_pracownik_AWL, create_user_pracownik_POZ, remove_pracownik_POZ, update_pracownik_POZ, get_cords_pracownik_WAT

from Projekt.data import users, wydarzenie_1, wydarzenie_2, wydarzenie_3, pracownicy_wat, uczestnik_wat, pracownicy_AWL, uczestnik_AWL, pracownicy_poz, uczestnik_poz


import requests
from bs4 import BeautifulSoup
import requests
import folium
import webbrowser
import os

if __name__ == '__main__':

    print(f"Witaj!")
    while True:
        print("Menu:")
        print("0. Zakończ program:")
        print("1. Wyświetl wydarzenia sportowe: ")
        print("2. Dodaj wydarzenie sportowe: ")
        print("3. Usuń wydarzenie sportowe: ")
        print("4. Uaktualnij wydarzenie sportowe: ")
        print("5. Szczegóły wydarzenia sportowego")
        print("6. Mapa wszystkich wydarzeń sportowych")
        menu_option:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option=="0":
            break
        if menu_option == "1":
            read(users)
        if menu_option == "2":
            create_user(users)
        if menu_option == "3":
            remove(users)
        if menu_option == "4":
            update(users)
        if menu_option == "5":
            search(users)
        if menu_option == "6":
            wydarzenia_mapa(users)

