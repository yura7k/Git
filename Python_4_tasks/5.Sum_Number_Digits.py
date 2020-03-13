""" Program output lenght and sum digitst of input number

    Input:
        number (int) : any int number

    Print:
        Lenght number
        Sum digits of number
    """
# При потребі можна зробити перевірку на число, але я не хотів повторювати функцію

number = input("Inpun any number: ")

digits = list(str(number))

sum_digits = 0

for i in range(len(digits)):
    sum_digits = sum_digits + int(digits[i])

print("The lenght of number: ", len(digits))
print("The Sum of number digits: ", sum_digits)