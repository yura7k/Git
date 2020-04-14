from colorama import Fore
from switchlang import switch
from services import Apartment_service, Guest_service, Booking_service

import services.mongo_setup as db_setup

def main():
    db_setup.global_init()
    print(Fore.BLUE, "Hotel service", Fore.RESET)

    commands()

    apartments = Apartment_service()
    guests = Guest_service()
    bookings = Booking_service()

    while True:
        action = get_action()
        with switch(action) as s:
            s.case('l', apartments.apartments_list)
            s.case('a', apartments.apartments_add)
            s.case('s', apartments.search_apartment)
            s.case('v', guests.guest_list)
            s.case('g', guests.guest_add)
            s.case('b', bookings.booking_list)
            s.case('sg', bookings.booking_seach_by_name)
            s.case('m', bookings.booking_add)
            s.case('?', commands)
            s.case('e', exit)
            s.default(lambda: print("Sory? this is not comand"))

def commands():
    print("What action would you like to do?")
    print("Apartments [L]ist")
    print("[A]dd apartments")
    print("[S]earch apartment")
    print("[V]iew guest")
    print("Add [G]uest")
    print("[B]ooking info")
    print("[SG]Search by guest")
    print("[M]ake booking")
    print("[?] Help")
    print("[E]xit")

def get_action():
    print(Fore.YELLOW + "> " + Fore.RESET, end='')
    action = input()
    return action.strip().lower()

if __name__ == '__main__':
    main()