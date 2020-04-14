from colorama import Fore
import datetime

from models.booking import Booking
from models.apartments import Apartment
from services.guest_service import Guest_service
from helper.input_helper import (get_string, get_price, get_int)
from helper.output_helper import pretty_print

class Booking_service():
    def booking_list(self):
        print(Fore.RED, " View Booking ".center(30, "*"), Fore.RESET)

    def booking_add(self):
        print(Fore.RED, " Add Booking ".center(30, "*"), Fore.RESET)
        guest = Guest_service()
        guest_id = guest.search_guest()

        booking = Booking()
        booking.guest_id = guest_id
        booking.booked_date = datetime.date.today()

        Apartment.objects(id='5e919e7edae830742803c9bd').update(push__booking=booking)
        #.save()
        print(Fore.RED, " Apartment Saved".center(30, "*"), Fore.RESET)