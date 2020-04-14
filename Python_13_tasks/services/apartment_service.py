from colorama import Fore
from models.apartments import Apartment
from helper.input_helper import (get_string, get_price)
from helper.output_helper import pretty_print

class Apartment_service():
        
    def apartments_list(self):
        print(Fore.RED, " Apartment List ".center(30, "*"), Fore.RESET)

        apartments = Apartment.objects()
        columns = ('Name', 'Description', 'Price', 'Smoke_allowed')

        pretty_print(apartments, columns)

    def apartments_add(self):
        print(Fore.RED, " Add Apartment ".center(30, "*"), Fore.RESET)
        
        apartment = Apartment()
        apartment.name = get_string("Please, enter apartment name: ")
        apartment.description = get_string("Please, enter apartment descrintion: ")
        apartment.price = get_price("Please, enter apartment price: ")

        apartment.save()
        print(Fore.RED, " Apartment Saved".center(30, "*"), Fore.RESET)
    
    def search_apartment(self, name=''):
        print(Fore.RED, " Apartment Search ".center(30, "*"), Fore.RESET)

        if name == '':
            name = get_string("Pleace, enter apartment name: ")

        apartment = Apartment.objects() \
                        .filter(name = name)

        columns = ('Name', 'Description', 'Price', 'Smoke_allowed')

        pretty_print(apartment, columns)

        return apartment