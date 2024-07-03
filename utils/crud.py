# def read(users: list[dict]) -> None:
#     for user in users[1:]:
#         print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')


def add_user(users: list[dict]) -> None:
    name: str = input("Podaj imię użytkownika: ")
    surname: str = input("Podaj nazwisko użytkownika: ")
    posts: int = int(input("Podaj liczbę postów: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)


def search(users: list[dict]) -> None:
    user_name: str = input("Kogo szukasz: ")
    for user in users[1:]:
        if user["name"] == user_name:
            print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')


def remove(users:list[dict]) ->None :
    user_name: str = input("Kogo szukasz: ")
    for user in users[1:]:
        if user ["name"]==user_name:
            users.remove(user)

def update(users: list[dict]) -> None:
    user_name: str = input("Kogo szukasz: ")
    for user in users[1:]:
        if user["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię: ")
            new_user_surname = input("Wprowadź nowe nazwisko: ")
            new_user_posts = input("Wprowadź nową ilość postów: ")
            user["name"] = new_user_name
            user["surname"] = new_user_surname
            user["posts"] = new_user_posts



import requests
from bs4 import BeautifulSoup
import psycopg2

db_params=psycopg2.connect(
    user="postgres",database="postgres",host="localhost",port="5432",password="geoinformatyka"
)

def get_coordinates(nazwa_miejscowosci)->list:

    url:str=f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    response=requests.get(url)
    # print(response.text)
    response_html=BeautifulSoup(response.text,'html.parser')
    # print(response_html)
    response_html_lat:list=response_html.select('.latitude')[1].text.replace(',','.')
    response_html_lng:list=response_html.select('.longitude')[1].text.replace(',','.')
    print (response_html_lat)
    print (response_html_lng)
    return [response_html_lat,response_html_lng]

# get_coordinates()

def create_user_db(db_params)-> None:

    name: str = input("Enter your name: ")
    surname: str = input("Enter your surname: ")
    posts: int = int(input("Enter your number of posts: "))
    location: str = input("Enter your location: ")
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    longitude,latitude=get_coordinates(location)
    cursor=db_params.cursor()
    sql=f"INSERT INTO public.users(name, surname, posts, location, coords) VALUES('{name}', '{surname}',{posts}, '{location}', 'SRID=4326;POINT({latitude} {longitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()


# create_user(db_params)

def read_db(db_params)-> None:
    cursor=db_params.cursor()
    sql=f"SELECT * FROM public.users"
    cursor.execute(sql)
    users=cursor.fetchall()
    cursor.close()
    for user in users:
        print(user)



def remove_user_db(db_params)-> None:
    cursor=db_params.cursor()
    sql=f"DELETE FROM public.users WHERE name='{input('Kogo usunąć?: ')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()

def update_user_db(db_params) -> None:
    new_name: str = input("New name: ")
    new_surname: str = input("New surname: ")
    new_posts: int = int(input("New number of posts: "))
    new_location: str = input("New location: ")
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    longitude, latitude = get_coordinates(new_location)
    cursor = db_params.cursor()
    sql = f"UPDATE public.users SET name='{new_name}', surname='{new_surname}', posts='{new_posts}', location='{new_location}', coords='SRID=4326;POINT({latitude} {longitude})' WHERE name='{input('Kogo uaktualnić?: ')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()

