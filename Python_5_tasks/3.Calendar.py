""" Необхідно створити програму для підрахунку днів у вказаному місяці та зазначити чи день є вихідним.
    
    Input data:
    • Дата у вигляді: 02-07-2019 (день-місяць-рік)
    
    Output data:
    • Кількість днів у місяці
    • Який дель вихідний чи будний
    """
import calendar
from  datetime import date

dateUser = input("Input date in format yyyy-mm-dd: ")

dateUser = date.fromisoformat(dateUser) #  переведення стрічки в формат дати, іншого не знайшов
parsDate = dateUser.timetuple() #  парсить дані з введеної дати повертає список значень
year = dateUser.year
month = dateUser.month
day = dateUser.day
weekdays = [0, 1, 2, 3, 4]
months = ["Січні", "Лютому", "Березні", "Квітні", "Травні", "Червні",
            "Липні", "Серпні", "Вересні", "Жовтні", "Листопаді", "Грудні"]
countDays = calendar.monthrange(year, month)

if calendar.weekday(year, month, day) in weekdays:
    strDay = "будний день"
else:
    strDay = "вихідний день"

print("У {} {} року - {} день".format(months[month], year, countDays[1]))
print("{} - {}".format(dateUser.strftime("%d-%m-%y"), strDay))