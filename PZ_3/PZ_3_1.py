
def coordinates_rectangle(x, y, x1, y1, x2, y2):
    # Проверка корректности координат
    if x1 >= x2 or y1 >= y2:
        raise ValueError("Координаты должны быть корректными: x1 < x2 и y1 < y2.")
    return (x1 < x < x2) and (y1 < y < y2)
x = int(input("Введите координату x: "))
x1 = int(input("Введите координату x1: "))
x2 = int(input("Введите координату x2: "))
y = int(input("Введите координату y: "))
y1 = int(input("Введите координату y1: "))
y2 = int(input("Введите координату y2: "))
try:
    result = coordinates_rectangle(x, y, x1, y1, x2, y2)
    print(result)
except ValueError as e:
    print(f"Ошибка: {e}")