from colorama import Fore
import datetime

from models.booking import Booking
from models.apartments import Apartment
from services.guest_service import Guest_service
from services import Apartment_service
from helper.input_helper import (get_string, get_price, get_age, get_int, get_date)
from helper.output_helper import pretty_print

class Booking_service():
    def booking_list(self):
        print(Fore.RED, " View Booking by Apartment ".center(30, "*"), Fore.RESET)
        columns_apt = ("Name", "price")
        columns_booking = ("guest_id", "chek_in_date", "chek_out_date", "booked_date")

        Apartments = Apartment_service()
        apartments = Apartments.search_apartment()

        for apartment in apartments:
            guest_bookings = []
            if apartment.bookings:
                for booking in apartment.bookings:
                     guest_bookings.append(booking)
                pretty_print(guest_bookings, columns_booking)


    def booking_add(self):
        print(Fore.RED, " Add Booking ".center(30, "*"), Fore.RESET)
        guest = Guest_service()
        guest_id = guest.search_guest()

        Apartments = Apartment_service()
        apartments = Apartments.search_apartment()
       
        rowIdx = get_int("Please select apt number: ", 0, len(apartments))
        apartment = apartments[rowIdx]
        apartment_price = apartment.price

        booking = Booking()
        booking.guest_id = guest_id
        booking.booked_date = datetime.datetime.now()
        booking.chek_in_date = get_date("Input Data")
        booking.chek_out_date = get_date("Input Data")
        
        if (apartments == None or len(apartments) == 0):
            print("Error")
            return

        apartment.bookings.append(booking)

        apartment.save()    
        
        columns = ("Chek_in_date", "Chek_out_date", "Booked_date")
        pretty_print([booking], columns)

        print("{}Booking duration is {} day(s).{}".format(Fore.YELLOW, booking.duration, Fore.RESET))
        print("{}TOTAL Price {} USD.{}".format(Fore.YELLOW, apartment_price * booking.duration, Fore.RESET))
    
        print(Fore.RED, " Apartment Saved".center(30, "*"), Fore.RESET)

    def booking_seach_by_name(self):
        print(Fore.RED, " Seach Booking by Name".center(30, "*"), Fore.RESET)
            
        guest = Guest_service()
        guestID = guest.search_guest()
        
        print(Fore.YELLOW, "You ID = ", guestID, Fore.RESET)

        columns_apt = ("Name", "price")
        columns_booking = ("guest_id", "chek_in_date", "chek_out_date", "booked_date")
        guest_bookings = []

        for apartment in Apartment.objects():
            # tmp = Apartment_service()
            # tmp.search_apartment(name=apartment.name)
            for booking in apartment.bookings:
                if booking.guest_id == guestID:
                    guest_bookings.append(booking)

        if len(guest_bookings) > 0:
            pretty_print(guest_bookings, columns_booking)
        else:
            print(Fore.YELLOW, "You hasn't bookings yet!", Fore.RESET)

        #  Все працює, тобто виводить список бронювань гостя,
        #  але, хочеться щоб виводило ще назву кімнати чи готелю, якщо є бронювання
        #  пробував так - яле трохи не те
        """ for apartment in Apartment.objects():
            pretty_print([apartment], columns_apt)
            for booking in apartment.bookings:
                if booking.guest_id == guestID:
                    pretty_print([booking], columns_booking)"""