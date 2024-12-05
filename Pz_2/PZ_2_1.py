def day_of_week(k):
    day_number = k % 7
    return day_number
k = int(input("Введите номер дня года (1-365): "))
if 1 <= k <= 365:
    print(f"Номер дня недели для {k}-го дня года: {day_of_week(k)}")
else:
    print("Увы, вы ошиблись. Введите число в диапазоне от 1 до 365.")