from tkinter import *
import tkintermapview
from geopy.geocoders import Nominatim
from Data import events

# APLIKACJA DO ZARZĄDZANIA Wydarzeniami sportowymi "EventsManager"


dane_logowania = {
    "Jan": "2137"
}


# klasa LoginWindow odpowiada za logowanie do aplikacji
class LoginWindow:
    def __init__(self, root, on_login_success):  # definiowanie klasy
        self.root = root
        self.root.title("Login")
        self.on_login_success = on_login_success

        self.frame_login = Frame(root, padx=10, pady=10)
        self.frame_login.pack()

        self.label_username = Label(self.frame_login, text='Username')
        self.entry_username = Entry(self.frame_login)
        self.label_password = Label(self.frame_login, text='Password')
        self.entry_password = Entry(self.frame_login, show='*')

        self.button_login = Button(self.frame_login, text='Login', command=self.login)

        self.label_username.grid(row=0, column=0, pady=5)
        self.entry_username.grid(row=0, column=1, pady=5)
        self.label_password.grid(row=1, column=0, pady=5)
        self.entry_password.grid(row=1, column=1, pady=5)
        self.button_login.grid(row=2, columnspan=2, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username in dane_logowania and dane_logowania[username] == password:
            self.on_login_success()  # funkcja wywołana przy poprawnym logowaniu
        else:
            self.label_error = Label(self.frame_login, text='Invalid username or password',
                                     fg='red')  # fg oznacza foreground i okresla kolor w jakim ma byc data zmienna
            self.label_error.grid(row=3, columnspan=2, pady=5)

        # klasa EventsManager odpowiada za aplikację


class EventsManager:
    def __init__(self, root):  # definiowanie klasy
        self.root = root
        self.root.state('zoomed')  # Aplikacja włącza się w pełnym ekranie
        self.root.title("Events Manager")

        self.events = events
        self.geolocator = Nominatim(
            user_agent="event_manager")  # Nominatim to klasa biblioteki geopy, user_agent to wymagany parametr do uzywania tej aplikacji

        # Frames
        self.frame_list = Frame(root, width=300, height=800, padx=10, pady=10)
        self.frame_details = Frame(root, width=700, height=800, padx=10, pady=10)
        self.frame_map = Frame(root, width=800, height=800, padx=10, pady=10)

        self.frame_list.grid(row=0, column=0, padx=10, pady=10, sticky=N + S)
        self.frame_details.grid(row=0, column=1, padx=10, pady=10, sticky=N + S)
        self.frame_map.grid(row=0, column=2, padx=10, pady=10, sticky=N + S + E + W)

        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Setup frames
        self.setup_list_frame()
        self.setup_details_frame()
        self.setup_map_frame()

        self.selected_event = None
        self.selected_member = None

        self.show_all_events_on_map()

        # ustawienie listy eventów oraz przycisków do zarządzania nimi

        # sekcja odpowiedzialna za to co one pokazują

    def setup_list_frame(self):
        self.label_list = Label(self.frame_list, text='Lista Wydarzeń Sportowych')
        self.listbox_events = Listbox(self.frame_list, width=40, height=25)
        self.button_show_details = Button(self.frame_list, text='Pokaż szczegóły', command=self.show_event_details)

        self.button_add_event = Button(self.frame_list, text='Dodaj Wydarzenie', command=self.add_event)
        self.button_remove_event = Button(self.frame_list, text='Usuń Wydarzenie', command=self.remove_event)
        self.button_update_event = Button(self.frame_list, text='Edytuj Wydarzenie', command=self.update_event)
        self.button_show_all_event = Button(self.frame_list, text='Pokaż Wszystkie Wydarzenia',
                                              command=self.show_all_events_on_map)
        self.button_show_all_members = Button(self.frame_list, text='Pokaż Wszystkich Uczestników ',
                                              command=self.show_all_members_on_map)
        self.button_show_all_employees = Button(self.frame_list, text='Pokaż Wszystkich Pracowników ',
                                              command=self.show_all_employees_on_map)

        self.label_list.pack(pady=5)  # .pack układa wszystko jedno po drugim lub jedno pod drugim
        self.listbox_events.pack(pady=5)
        self.button_show_all_event.pack(pady=5)
        self.button_show_all_members.pack(pady=5)
        self.button_show_all_employees.pack(pady=5)
        self.button_show_details.pack(side=LEFT, padx=5)
        self.button_add_event.pack(side=LEFT, padx=5)
        self.button_remove_event.pack(side=LEFT, padx=5)
        self.button_update_event.pack(side=LEFT, padx=5)


        self.refresh_event_list()

        # ustawienie szczegółów centrum (klienci, pracownicy, rezerwacje) i przycisków do nich

        # sekcja odpowiedzialna za to co one pokazują

    def setup_details_frame(self):
        self.label_details = Label(self.frame_details,
                                   text='Szczegóły Wydarzeń')  # np: ta linijka odpowiada za to jak nazywa się cała sekcja szczegółów
        self.label_name = Label(self.frame_details,
                                text='Nazwa Wydarzenia')  # np: ta linijka odpowiada za to jak nazywa się pole, w którym wyświetla się nazwa centrum
        self.entry_name = Entry(self.frame_details, width=40)  # tu wyświetla się nazwa eventu
        self.label_location = Label(self.frame_details, text='Miejscowość')  # reszta analogicznie
        self.entry_location = Entry(self.frame_details, width=40)
        self.label_members = Label(self.frame_details, text='Uczestnicy')
        self.listbox_members = Listbox(self.frame_details, width=30, height=10)
        self.label_employees = Label(self.frame_details, text='Pracownicy')
        self.listbox_employees = Listbox(self.frame_details, width=30, height=10)


        self.entry_member_name = Entry(self.frame_details, width=30)
        self.entry_member_miejscowosc = Entry(self.frame_details, width=30)
        self.entry_employee_name = Entry(self.frame_details, width=30)
        self.entry_employee_miejscowosc = Entry(self.frame_details, width=30)


        # sekcja odpowiedzialna za to jak nazywaja sie przyciski

        self.button_add_member = Button(self.frame_details, text='Dodaj Uczestnika', command=self.add_members)
        self.button_remove_member = Button(self.frame_details, text='Usuń Uczestnika', command=self.remove_member)
        self.button_edit_member = Button(self.frame_details, text='Edytuj Uczestnika', command=self.edit_member)
        self.button_add_employee = Button(self.frame_details, text='Dodaj Pracownika', command=self.add_employee)
        self.button_remove_employee = Button(self.frame_details, text='Usuń Pracownika', command=self.remove_employee)
        self.button_edit_employee = Button(self.frame_details, text='Edytuj Pracownika', command=self.edit_employee)

        self.button_edit_member_miejscowsc = Button(self.frame_details, text='Edytuj Lokalizacje Uczestnika', command=self.edit_member_miejscowosc)

        self.button_edit_employee_miejscowsc = Button(self.frame_details, text='Edytuj Lokalizacje Pracownika', command=self.edit_employee_miejscowosc)

        self.button_show_members_map = Button(self.frame_details, text='Pokaż Uczestników  ',
                                              command=self.show_members_on_map)

        self.button_show_employee_map = Button(self.frame_details, text='Pokaż Pracowników  ',
                                               command=self.show_employee_on_map)

        # sekcja odpowiedzialna za to gdzie się znajdują

        self.label_details.grid(row=0, columnspan=2, pady=10)  # .grid układa w formie siatki (wiersze i kolumny)
        self.label_name.grid(row=1, column=0, sticky=W)
        self.entry_name.grid(row=1, column=1, columnspan=1, pady=5, sticky=W)
        self.label_location.grid(row=2, column=0, sticky=W)
        self.entry_location.grid(row=2, column=1, columnspan=1, pady=5, sticky=W)
        self.label_members.grid(row=3, column=0, pady=5)
        self.listbox_members.grid(row=4, column=0, pady=5)
        self.label_employees.grid(row=3, column=1, pady=5)
        self.listbox_employees.grid(row=4, column=1, pady=5)


        self.entry_member_name.grid(row=5, column=0, pady=5)
        self.entry_member_miejscowosc.grid(row=6, column=0, pady=5)
        self.entry_employee_name.grid(row=5, column=1, pady=5)
        self.entry_employee_miejscowosc.grid(row=6, column=1, pady=5)


        self.button_add_member.grid(row=7, column=0, pady=5)
        self.button_remove_member.grid(row=8, column=0, pady=5)
        self.button_edit_member.grid(row=9, column=0, pady=5)
        self.button_add_employee.grid(row=7, column=1, pady=5)
        self.button_remove_employee.grid(row=8, column=1, pady=5)
        self.button_edit_employee.grid(row=9, column=1, pady=5)


        self.button_edit_member_miejscowsc.grid(row=10, column=0, pady=5)
        self.button_show_members_map.grid(row=11, column=0, pady=5)



        self.button_edit_employee_miejscowsc.grid(row=10, column=1, pady=5)
        self.button_show_employee_map.grid(row=11, column=1, pady=5)


    # ustawienie mapy i jej położenia

    def setup_map_frame(self):
        self.map_widget = tkintermapview.TkinterMapView(self.frame_map, width=800, height=800, corner_radius=0)
        self.map_widget.pack(fill=BOTH, expand=True)

    # Główne funkcje odpowiadające za poprawne działanie programu

    # odświeżenie listy z eventami
    def refresh_event_list(self):
        self.listbox_events.delete(0, END)
        for event in self.events:
            self.listbox_events.insert(END, event['name'])

        # pokazanie szczegółów danego eventu

    def show_event_details(self):
        selected_index = self.listbox_events.curselection()
        if selected_index:
            event = self.events[selected_index[0]]
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, event['name'])
            self.entry_location.delete(0, END)
            self.entry_location.insert(0, event['locations'])
            self.listbox_members.delete(0, END)
            for member in event['members']:
                self.listbox_members.insert(END, member['name'])
            self.listbox_employees.delete(0, END)
            for employee in event['employees']:
                self.listbox_employees.insert(END, employee['name'])
            self.selected_event = event

            self.show_selected_event_on_map()

        # pokazanie markera wybranego eventu na mapie

    def show_selected_event_on_map(self):
        self.map_widget.set_zoom(6)  # centrowanie mapy z zoomem 6
        self.map_widget.set_position(52.2297, 19.0122)  # centrowanie mapy na centrum Polski
        self.map_widget.delete_all_marker()

        location = self.geolocator.geocode(
            self.selected_event['locations'])  # używanie jednej z metod Nominatim 'geocode'
        if location:  # do przekształcenia lokalizacji na współrzędne, które są potem ustawiane na mapie
            self.map_widget.set_position(location.latitude, location.longitude)
            self.map_widget.set_marker(location.latitude, location.longitude, text=self.selected_event['name'])



        # dodanie eventu do listy eventów

    def add_event(self):
        name = self.entry_name.get()
        location = self.entry_location.get()
        if name and location:
            self.events.append({"name": name, "locations": location, "members": [], "employees": []})
            self.refresh_event_list()
            self.show_all_events_on_map()

        # usunięcie wydarzeń z listy wydarzeń

    def remove_event(self):
        selected_index = self.listbox_events.curselection()
        if selected_index:
            self.events.pop(selected_index[0])
            self.refresh_event_list()
            self.show_all_events_on_map()

        # aktualizacja danych dla wybranego eventu

    def update_event(self):
        selected_index = self.listbox_events.curselection()
        if selected_index:
            self.events[selected_index[0]] = {"name": self.entry_name.get(), "locations": self.entry_location.get(),
                                               "members": self.selected_event['members'],
                                               "employees": self.selected_event['employees']}
            self.refresh_event_list()
            self.show_all_events_on_map()

        # dodanie uczestnika do listy uczestnikow

    def add_members(self):
        if not self.selected_event:
            return
        member_name = self.entry_member_name.get()
        member_location = self.entry_member_miejscowosc.get()  # Pobranie miejscowości z pola Entry

        if member_name and member_location:  # Sprawdzenie czy oba pola są uzupełnione
            self.selected_event['members'].append(
                {"name": member_name, "miejscowosc": member_location})  # Dodanie słownika z nazwą i miejscowością
            self.refresh_member_list()  # Odświeżenie listy uczestników
            self.show_event_details()  # Wyświetlenie szczegółów wydarzenia
            self.entry_member_name.delete(0, END)  # Wyczyszczenie pola nazwy uczestnika
            self.entry_member_miejscowosc.delete(0, END)  # Wyczyszczenie pola miejscowości uczestnika

        # usunięcie uczestnikow z listy uczestnikow

    def remove_member(self):
        selected_index = self.listbox_members.curselection()
        if not selected_index:
            return
        del self.selected_event['members'][selected_index[0]]
        self.listbox_members.delete(selected_index[0])
        self.show_event_details()

        # aktualizacja danych wybranego uczestnika

    def edit_member(self):
        selected_index = self.listbox_members.curselection()
        if not selected_index:
            return
        new_name = self.entry_member_name.get()
        if new_name:
            self.selected_event['members'][selected_index[0]]['name'] = new_name
            self.listbox_members.delete(selected_index[0])
            self.listbox_members.insert(selected_index[0], new_name)
            self.entry_member_name.delete(0, END)

        # dodanie pracownika do listy pracowników

    def add_employee(self):
        if not self.selected_event:
            return

        employee_name = self.entry_employee_name.get()
        employee_location = self.entry_employee_miejscowosc.get()  # Pobranie miejscowości pracownika

        if employee_name and employee_location:
            self.selected_event['employees'].append({"name": employee_name, "miejscowosc": employee_location})
            self.refresh_employee_list()  # Odświeżenie listy pracowników w interfejsie
            self.show_event_details()  # Ponowne wyświetlenie szczegółów wydarzenia po dodaniu pracownika
            self.entry_employee_name.delete(0, END)  # Wyczyszczenie pola nazwy pracownika
            self.entry_employee_miejscowosc.delete(0, END)  # Wyczyszczenie pola miejscowości pracownika

        # usunięcie pracownika z listy pracowników

    def remove_employee(self):
        selected_index = self.listbox_employees.curselection()
        if not selected_index:
            return
        del self.selected_event['employees'][selected_index[0]]
        self.listbox_employees.delete(selected_index[0])
        self.show_event_details()

        # aktualizacja danych wybranego pracownika

    def edit_employee(self):
        selected_index = self.listbox_employees.curselection()
        if not selected_index:
            return
        new_name = self.entry_employee_name.get()
        if new_name:
            self.selected_event['employees'][selected_index[0]]['name'] = new_name
            self.listbox_employees.delete(selected_index[0])
            self.listbox_employees.insert(selected_index[0], new_name)
            self.entry_employee_name.delete(0, END)






        # aktualizacja lokalizacji uczestnikow

    def edit_member_miejscowosc(self):
        selected_member_index = self.listbox_members.curselection()
        if selected_member_index:
            selected_member_index = selected_member_index[0]
            selected_member = self.selected_event['members'][selected_member_index]
            new_location = self.entry_member_miejscowosc.get()
            if new_location:
                # Tylko aktualizacja lokalizacji, bez zmiany nazwy
                self.selected_event['members'][selected_member_index]['miejscowosc'] = new_location
                self.refresh_member_list()
                self.entry_member_miejscowosc.delete(0, 'end')




        # aktualizacja danych wybranego pracownika

    def edit_employee_miejscowosc(self):
        selected_employee_index = self.listbox_employees.curselection()
        if selected_employee_index:
            selected_employee_index = selected_employee_index[0]
            selected_employee = self.selected_event['employees'][selected_employee_index]
            new_location = self.entry_employee_miejscowosc.get()
            if new_location:
                # Tylko aktualizacja lokalizacji, bez zmiany nazwy
                self.selected_event['employees'][selected_employee_index]['miejscowosc'] = new_location
                self.refresh_employee_list()
                self.entry_employee_miejscowosc.delete(0, 'end')

    def refresh_member_list(self):
        self.listbox_members.delete(0, END)
        for member in self.selected_event.get('members', []):
            self.listbox_members.insert(END, f"{member['name']} - {member['miejscowosc']}")

    def refresh_employee_list(self):
        self.listbox_employees.delete(0, END)
        for employee in self.selected_event.get('employees', []):
            self.listbox_employees.insert(END, f"{employee['name']} - {employee['miejscowosc']}")

        # czyszczenie pól ze szczegółami

    def clear_details(self):
        self.entry_name.delete(0, END)
        self.entry_location.delete(0, END)
        self.listbox_members.delete(0, END)
        self.listbox_employees.delete(0, END)


        # pokazanie markerów wszystkich eventow na mapie

    def show_all_events_on_map(self):
        self.map_widget.delete_all_marker()
        self.map_widget.set_position(52.2296756, 19.0122287)
        self.map_widget.set_zoom(6)
        for event in self.events:
            location = self.geolocator.geocode(event['locations'])  # używanie jednej z metod Nominatim 'geocode'
            if location:  # do przekształcenia lokalizacji na współrzędne, które są potem ustawiane na mapie
                self.map_widget.set_marker(location.latitude, location.longitude, text=event['name'])
                self.clear_details()
    def show_all_members_on_map(self):
        self.map_widget.delete_all_marker()
        self.map_widget.set_position(52.2296756, 19.0122287)
        self.map_widget.set_zoom(6)
        for event in self.events:
            for member in event['members']:
                location = self.geolocator.geocode(member['miejscowosc']) # używanie jednej z metod Nominatim 'geocode'
                if location: # do przekształcenia lokalizacji na współrzędne, które są potem ustawiane na mapie
                    self.map_widget.set_marker(location.latitude, location.longitude,
                                               text=f"{member['name']} ({event['name']})")
                    self.clear_details()
    def show_all_employees_on_map(self):
        self.map_widget.delete_all_marker()
        self.map_widget.set_position(52.2296756, 19.0122287)
        self.map_widget.set_zoom(6)
        for event in self.events:
                for employee in event['employees']:  # używanie jednej z metod Nominatim 'geocode'
                    location = self.geolocator.geocode(employee['miejscowosc'])
                    if location: # do przekształcenia lokalizacji na współrzędne, które są potem ustawiane na mapie
                        self.map_widget.set_marker(location.latitude, location.longitude,
                                                   text=f"{employee['name']} ({event['name']})")
                        self.clear_details()

    def show_members_on_map(self):
        if self.selected_event:
            self.map_widget.delete_all_marker()
            self.map_widget.set_position(52.2296756, 19.0122287)
            self.map_widget.set_zoom(6)

            for member in self.selected_event['members']:
                location = self.geolocator.geocode(member['miejscowosc'])
                if location:
                    self.map_widget.set_marker(location.latitude, location.longitude,
                                               text=f"{member['name']} ({self.selected_event['name']})")

            self.clear_details()

    def show_employee_on_map(self):
        if self.selected_event:
            self.map_widget.delete_all_marker()
            self.map_widget.set_position(52.2296756, 19.0122287)
            self.map_widget.set_zoom(6)

            for employee in self.selected_event['employees']:
                location = self.geolocator.geocode(employee['miejscowosc'])
                if location:
                    self.map_widget.set_marker(location.latitude, location.longitude,
                                               text=f"{employee['name']} ({self.selected_event['name']})")
            self.clear_details()


        # Uruchomienie aplikacji


def main():
    root = Tk()  # tworzenie głównego okna aplikacji, 'root' to główne okno

    # funkcja wywoływana po udanym zalogowaniu
    def on_login_success():
        login_window.frame_login.pack_forget()  # usunięcie okna logowania
        EventsManager(root)  # utworzenie głównego okna aplikacji poprzez przywołanie 'root'

    login_window = LoginWindow(root,
                               on_login_success)  # utworzenie okna logowania, 'on_login_succes' używane dopiero po poprawnym zalogowaniu
    root.mainloop()  # uruchomienie głównej pętli Tkinter, czyli utrzymanie aplikacji w aktywnym stanie, aby odpowiadała na polecenia

    # sprawdzenie czy kod jest uruchamiany bezpośrednio, jeśli tak - wywołuje main(), co włącza aplikację


if __name__ == '__main__':
    main()