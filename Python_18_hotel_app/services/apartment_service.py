from colorama import Fore
from models.apartments import Apartment

class Apartment_service():
    def apartments_list(self):
        print(Fore.RED, " Apartment List ".center(30, "*"), Fore.RESET)
        apartments = Apartment.objects()     
        return apartments

    def get_apartments(self):
        print(Fore.RED, " Apartment Added ".center(30, "*"), Fore.RESET)
        apartments = Apartment.objects().order_by('name')
        rows = []
        for apartment in apartments:
            rows.append(apartment.name)
        return rows
   
    def search_apartment(self, name=''):
        print(Fore.RED, " Apartment Search ".center(30, "*"), Fore.RESET)

        if name == '':
            return

        apartment = Apartment.objects() \
                        .filter(name = name)

        return apartment

    def update_data(self, data):
        apartment = Apartment.objects(name=data['name']).first()

        if not apartment:
            apartment = Apartment()
        
        apartment.name = data['name']
        apartment.description = data['description']
        apartment.price = float(data['price'])
        apartment.save()

    def remove_apartment(self, name):
        print(Fore.RED, " Apartment removed ".center(30, "*"), Fore.RESET)
        apartments = Apartment.objects(name=name)
        apartments.delete()