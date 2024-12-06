def day_of_week(K):
    day_number = K % 7
    return day_number
K = int(input("Введите номер дня года (1-365): "))
if 1 <= K <= 365:
    print(f"Номер дня недели для {K}-го дня года: {day_of_week(K)}")
else:
    print("Увы, вы ошиблись. Введите число в диапазоне от 1 до 365.")