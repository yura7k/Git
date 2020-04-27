from colorama import Fore

from models.guests import Guest

class Guest_service():
    def guest_list(self):
        print(Fore.RED, " Guest List ".center(30, "*"), Fore.RESET)
        guests = Guest.objects()
        return guests
        
    def guest_add(self):
        print(Fore.RED, " Add Guest ".center(30, "*"), Fore.RESET)
        min_age = Guest.age.min_value

        guest = Guest()
        guest.name = get_string("Please enter guest name: ")
        guest.age = get_age("Please enter guest age (you must have > {}): ".format(min_age), min_age=min_age)

        guest.save()
        print(Fore.RED, " Apartment Saved".center(30, "*"), Fore.RESET)
    
    def get_guests(self):
        guests = Guest.objects().order_by('name')
       
        rows = []
        for guest in guests:
            rows.append(guest['name'])
        return rows

    def search_guest(self, guest_name):
        print(Fore.RED, " Search Guest ".center(30, "*"), Fore.RESET)

        guest = Guest.objects().filter(name=guest_name)
        
        if guest:
            return (guest[0]['id'])
        else:
            return
