""" Program print winner of lotery

    Print:
        Number and Name of winner
    """

import random

dictMembers = {0: 'Maks', 1: 'Yurii', 2: 'Valerii', 3: 'Olya', 4: 'Katya',
                5: 'Petya', 6: 'Sasha', 7: 'Natali', 8: 'Oleg', 9: 'Tanya'}

listNumMembers = []

for i in range(len(dictMembers)):
    listNumMembers.append(i)

numWinner = random.choice(listNumMembers) 
# чомусь numWinner = random.choice(dictMembers.keys()) працювати не хотіло

print("List members:")
print(dictMembers)
print(f"Winner number is {numWinner} his(her) name is {dictMembers[numWinner]} ")