from colorama import Fore

from models.guests import Guest

from helper.input_helper import (get_string, get_price, get_age)
from helper.output_helper import pretty_print

class Guest_service():
    def guest_list(self):
        print(Fore.RED, " Guest List ".center(30, "*"), Fore.RESET)

        guests = Guest.objects()
        columns = ('Id', 'Name', 'Age', 'Is_Card')

        pretty_print(guests, columns)


    def guest_add(self):
        print(Fore.RED, " Add Guest ".center(30, "*"), Fore.RESET)
        min_age = Guest.age.min_value

        guest = Guest()
        guest.name = get_string("Please enter guest name: ")
        guest.age = get_age("Please enter guest age (you must have > {}): ".format(min_age), min_age=min_age)

        guest.save()
        print(Fore.RED, " Apartment Saved".center(30, "*"), Fore.RESET)

    def search_guest(self):
        print(Fore.RED, " Search Guest ".center(30, "*"), Fore.RESET)

        name = get_string("Enter you name: ")

        guest = Guest.objects().filter(name=name)
        
        if guest:
            return (guest[0]['id'])
        else:
            self.guest_add()
