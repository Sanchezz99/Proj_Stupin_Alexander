#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте 
#методы для определения дня недели, проверки на високосный год и определения 
#количества дней в месяце.
import datetime 
class Kalendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.rusday = {
            "Monday": "Понедельник",
            "Tuesday": "Вторник",
            "Wednesday": "Среда",
            "Thursday": "Четверг",
            "Friday": "Пятница",
            "Saturday": "Суббота",
            "Sunday": "Воскресенье"
        }
    def visok_year(self):
        return (self.year % 400 == 0) or (self.year % 4 == 0 and self.year % 100 != 0)
    def kolvo_day(self):
        if self.month == 2:
            return 29 if self.visok_year() else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else: 
            return 31
    def day_of_week(self):
        date = datetime.date(self.year, self.month, self.day)
        engday = date.strftime("%A")
        return self.rusday[engday]
    def main_information(self):
        print(f"Дата: {self.day}, {self.month}, {self.year}")
        print("Нынешний год високосный" if self.visok_year() else "Нынешний год не високосный")
        print(f"В этом месяце {self.kolvo_day()} дней")
        print(f"День недели: {self.day_of_week()}")
information = Kalendar(2025, 1, 6)
information.main_information()