from colorama import Fore
import datetime

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

def get_age(message, min_age):
    styled_massage = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    
    while True:
        str = input(styled_massage)
        str = str.strip()
        
        try:
            number = int(str)
            assert number >= min_age, "Please, enter age > {}".format(min_age)
            return number
        except ValueError:
            print(Fore.YELLOW + "Please, enter int value" + Fore.RESET) 
        except Exception:
            print(Fore.YELLOW + "Please, enter age > {}".format(min_age) + Fore.RESET)

def get_int(message, min_val, max_val):
    error_message = "{}Please, enter value {} between {}{}".format(Fore.YELLOW, min_val, max_val, Fore.RESET)
    styled_massage = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    
    while True:
        str = input(styled_massage)
        str = str.strip()
        
        try:
            number = int(str)
            assert number >= min_val and number < max_val, error_message
            return number
        except ValueError:
            print(Fore.YELLOW + "Please, enter int value" + Fore.RESET) 
        except Exception:
            print(error_message)

def get_date(message):
    styled_massage = "{}{}(YYYY-MM-DD){}".format(Fore.BLUE, message, Fore.RESET)

    while True:
        str_date = input(styled_massage)
        try:
            year, month, day = map(int, str_date.split('-'))
            new_date = datetime.date(year, month, day)
            return new_date
        except:
            print("Please, enter date (YYYY-MM-DD)")
