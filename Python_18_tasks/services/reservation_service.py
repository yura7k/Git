from colorama import Fore
from typing import List, Optional
from models.apartments import Apartment
from models.reservations import Reservation
from helpers.input_helper import (get_date, get_int)
from helpers.output_helper import (pretty_print)
from services import Apartment_service
import datetime

class Reservation_service():
    def reservation_list(self):
        print("View Reservations")
        Apartments = Apartment_service()
        apartments = Apartments.apartments_list()
        rows = []
        if not apartments:
            return rows
        for apartment in apartments:
            if not apartment.reservations:
                continue
            for reservation in apartment.reservations:
                guest = reservation.guest
                if guest:
                    data = {
                        "name": apartment.name,
                        "user_name": guest.name,
                        "is_card": guest.is_card,
                        "check_in": reservation.check_in_date,
                        "check_out": reservation.check_out_date,
                        "price": reservation.duration * apartment.price,
                    }
                    rows.append(data)

        return rows


    def add_reservation(self):
        print("Add Reservation")

        Apartments = Apartment_service()
        apartments = Apartments.search_apartment()

        if (apartments == None or len(apartments) == 0):
            print(Fore.YELLOW, "Apatrments not found", Fore.RESET)
            return
        
        rowIdx = get_int("Please, select apt number: ", 0, len(apartments))

        apartment = apartments[rowIdx]
    
        reservation = Reservation()

        reservation.booked_date = datetime.datetime.now()
       
        reservation.check_in_date = get_date("Please, enter check in date: ")
        reservation.check_out_date = get_date("Please, enter check out date: ")

        apartment.reservations.append(reservation)

        apartment.save()

        columns = ('Check_in_date', 'Check_out_date', 'Booked_date')
        pretty_print([reservation], columns)
        print("{} Booking duration is {} day(s). {}".format(Fore.BLUE, reservation.duration, Fore.RESET))

        print(Fore.GREEN, "Reservation saved", Fore.RESET)
