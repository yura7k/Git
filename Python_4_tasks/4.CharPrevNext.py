""" Program output previos and next elements of input symbol

    Input:
        symbol - any symbol

    Print:
        Previos symbol
        Curent symbol
        Next symbol
        Or Error if enter many symbol
    """

while True:
    try:
        symbol = input("Input any symbol: ")
        symbol = ord(symbol)
        break
    except Exception:
        print("You print so many symbols! Try again")

print("Previos symbol is ", chr(symbol-1))
print("Curent symbol is ", chr(symbol))
print("Next symbol is ", chr(symbol+1))