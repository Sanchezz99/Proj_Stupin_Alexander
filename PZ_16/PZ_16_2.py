#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте 
#методы для определения дня недели, проверки на високосный год и определения 
#количества дней в месяце. 
class Kalendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def visok_year(self):
        return self.year % 4
    def kolvo_day(self):
        if self.month == 2:
            return 29 if self.visok_year else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else: 
            return 31
    def main_information(self):
        print(f"Дата: {self.day}, {self.month}? {self.year}")
        print("Нынешний год високосный" if self.visok_year() else "Нынешний год не високосный")
        print(f"В этом месяце {self.month} дней")
information = Kalendar(2025, 11, 6)
information.main_information()