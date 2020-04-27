from colorama import Fore

from models.guests import Guest

class Guest_service():
    def guest_list(self):
        print(Fore.RED, " Guest List ".center(30, "*"), Fore.RESET)
        guests = Guest.objects()
        return guests
        
    def guest_add(self, data):
        print(Fore.RED, " Add Guest ".center(30, "*"), Fore.RESET)
        guest = Guest.objects(name = data['name']).first()

        if not guest:
            guest = Guest()

        guest.name = data['name']
        guest.age = data['age']
        guest.is_card = data['is_card']

        guest.save()
    
    def remove_guest(self, name):
        print(Fore.RED, " Guest removed ".center(30, "*"), Fore.RESET)
        apartments = Guest.objects(name=name)
        apartments.delete()
    
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
