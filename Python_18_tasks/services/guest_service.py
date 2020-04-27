from colorama import Fore
from models.guests import Guest
from helpers.input_helper import (get_string, get_price, get_age)
from helpers.output_helper import (pretty_print)

class Guest_service():
    def guest_list(self):
        print("Guest List")
        guests = Guest.objects()
        columns = ('Name', 'Age', 'Is_card')
        
        pretty_print(guests, columns)

    def get_guests(self):
        guests = Guest.objects().order_by('name')
       
        rows = []
        for guest in guests:
            rows.append(guest['name'])
        return rows

    def add_guest(self):
        min_age = Guest.age.min_value
        age_retrieve_message = "Please, enter you age: {}".format(min_age)

        name = get_string("Please, enter you name: ")
        age = get_age(age_retrieve_message, min_age = min_age)

        guest = Guest(name = name, age = age)

        guest.save()
        
        print(Fore.GREEN, "Guest added", Fore.RESET)