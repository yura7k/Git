""" Program print welcome message for friends 

    Input:
        name (str) : name of friend

    Print:
        Welcome message
    """

friendsList = {'Maks': 'Mukolayovich', 'Yurii': 'Vasilyovich', 'Valerii': 'Ivanovich', 
                'Olya': 'Olegivna', 'Katya': 'Petrivna'}

name = input("Enter you name: ").capitalize()

if name in friendsList.keys():
    print("Hallo, {0} {1}!!!".format(name, friendsList[str(name)]))
else:
    print("Hallo {} !!!".format(name))