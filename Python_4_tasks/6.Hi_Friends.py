""" Program output welcome message for friends 

    Input:
        name (str) : name of friend

    Print:
        Welcome message
    """

dictFriends = ['maks', 'yurii', 'valerii', 'olya', 'katya']

name = input("Enter you name: ")

if name.lower() in dictFriends:
    print("Hallo, {}!".format(name))
else:
    print("Hallo Guest!")