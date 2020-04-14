from colorama import Fore

def get_string(message):
    styled_massage = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str = input(styled_massage)
        str = str.strip()
        if len(str) > 1:
            return str

def get_price(message):
    styled_massage = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str = input(styled_massage)
        str = str.strip()
        
        try:
            number = float(str)
            return number
        except:
            print(Fore.YELLOW + "Please, enter number value" + Fore.RESET)         

def get_int(message):
    styled_massage = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str = input(styled_massage)
        str = str.strip()
        
        try:
            number = int(str)
            return number
        except:
            print(Fore.YELLOW + "Please, enter int value" + Fore.RESET)   