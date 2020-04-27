from colorama import Fore, Back, Style
import datetime

from models.booking import Booking
from models.apartments import Apartment
from services.guest_service import Guest_service
from services import Apartment_service


class Booking_service():
    """ View booking by Apartment name
        
        Input (str) -  name apartment
        Output - print table Apt and table Bookings
        """
    def booking_list(self):
        print(Fore.RED, " View Booking by Apartment ".center(30, "*"), Fore.RESET)
        Apartments = Apartment_service()
        apartments = Apartments.apartments_list()
        rows = []
        
        if not apartments:
            return rows

        for apartment in apartments:
            #  перевіряємо чи є бронювання
            if not apartment.bookings:
                continue
            for booking in apartment.bookings:
                #  Щоб не друкувати на кожне бронювання окрему табличку
                guest = booking.guest_id
                
                if guest:
                    data = {
                        "name": apartment.name,
                        "user_name": guest.name,
                        "is_card": guest.is_card,
                        "check_in": booking.chek_in_date,
                        "check_out": booking.chek_out_date,
                        "price": booking.duration * apartment.price,
                    }
                    rows.append(data)
        return rows
                     
    def booking_add(self, data):
        print(Fore.RED, " Add Booking ".center(30, "*"), Fore.RESET)

        apartment = Apartment.objects(name=data['name']).first()

        if not apartment:
            apartment = Apartment()
        
        booking = Booking()
        booking.guest_id = data['guest_id']
        booking.booked_date = data['booked_date']
        booking.chek_in_date = data['chek_in_date']
        booking.chek_out_date = data['chek_in_date']
        
        apartment.bookings.append(booking)

        apartment.save()    

    def booking_seach_by_name(self):
        """ View booking by Guest name
        
        Input (str) -  guest name
        Output - print table Bookings
        """
        print(Fore.RED, " Seach Booking by Name".center(30, "*"), Fore.RESET)
            
        #  Повертаємо ID гостя
        guest = Guest_service()
        guest_id = guest.search_guest()
        #  це друкую для виключно перевірки
        print(Fore.YELLOW, "You ID = ", guest_id, Fore.RESET)

        columns_apt = ("Name", "price")
        columns_booking = ("guest_id", "chek_in_date", "chek_out_date", "booked_date")
        message = "You haven't bookings yet!"

        #  Перевіряємо чи є бронювання
        for apartment in Apartment.objects(bookings__guest_id=guest_id):
            guest_bookings = []

            #  Перевіряємо чи це бронювання нашого гостя
            for booking in apartment.bookings:
                if booking.guest_id == guest_id:
                    guest_bookings.append(booking)

            #  якщо є бронювання друкуємо назву апартаментів та бронювання
            if len(guest_bookings) > 0:
                print(Fore.YELLOW, "You boking(s) in " + apartment.name, Fore.RESET)
                pretty_print(guest_bookings, columns_booking)
                message = ''
        
        #  якщо зовсім немає бронювань дкукуємо повідомлення
        if message != '':
            print(Fore.YELLOW, message, Fore.RESET)