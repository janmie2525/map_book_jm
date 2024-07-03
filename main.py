from utils.crud import read, create_user_db, update_user_db, search, remove, update, add_user, read_db, remove_user_db
from models.data import users

import requests
from bs4 import BeautifulSoup
import psycopg2
db_params=psycopg2.connect(
    user="postgres",database="postgres",host="localhost",port="5432",password="geoinformatyka"
)

if __name__ == '__main__':

    print(f"Witaj {users[0]['name']}!")
    while True:
        print("Menu:")
        print("0. Zakończ program:")
        print("1. Pokaż co u znajomych: ")
        print("2. Dodaj znajomego: ")
        print("3. Wyświetl użytkownika: ")
        print("4. Usuń znajomego: ")
        print("5. Uaktualnij znajomego: ")
        menu_option:str=input("Wybierz dostępną funkcje z menu: ")
        if menu_option=="0":
            break
        if menu_option == "1":
            read_db(db_params)
        if menu_option == "2":
            create_user_db(db_params)
        if menu_option == "3":
            search(db_params)
        if menu_option == "4":
            remove_user_db(db_params)
        if menu_option == "5":
            update_user_db(db_params)
