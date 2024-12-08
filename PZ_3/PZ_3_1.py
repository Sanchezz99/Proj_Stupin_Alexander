#Даны числа x, y, x1, y1, x2, y2. 
#Проверить истинность высказывания: "Точка с координатами (x, y) лежит внутри прямоугольника, 
#левая верхняя вершина которого имеет координаты (x1, y1), правая нижняя - (x2, y2), 
#а стороны параллельны координатным осям".
def coordinates_rectangle(x, y, x1, y1, x2, y2):
    try:
        x = float(x)
        x1 = float(x1)
        x2 = float(x2)
        y = float(y)
        y1 = float(y1)
        y2 = float(y2)
    except ValueError:
        raise ValueError("Вы должны вводить числа.")
    if x1 >= x2 or y1 >= y2:
        raise ValueError("Координаты должны быть корректными: x1 < x < x2 и y1 < y < y2.")
    return (x1 < x < x2) and (y1 < y < y2)
x = 4
x1 = 3
x2 = 5
y = 8
y1 = 7
y2 = 9
try:
    result = coordinates_rectangle(x, y, x1, y1, x2, y2)
    print(result)
except ValueError as e:
    print(f"Ошибка: {e}")