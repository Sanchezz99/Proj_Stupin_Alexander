#Даны числа х, у, x1, y1, х2, у2. 
#Проверить истинность высказывания: 
#«Точка с координатами (х, у) лежит внутри прямоугольника, 
#левая верхняя вершина которого имеет координаты (х1, у1), 
#правая нижняя — (х2, у2), а стороны параллельны координатным осям». 
def coordinates_rectangle(x, y, x1, y1, x2, y2):
    if x1 >= x2 or y1 >= y2:
        raise ValueError("Координаты должны быть корректными: x1 < x2 и y1 < y2")
    return (x1 < x < x2) and (y1 < y < y2)
while True:
    try:
        x = int(input("Введите координату x: "))
        x1 = int(input("Введите координату x1: "))
        x2 = int(input("Введите координату x2: "))
        y = int(input("Введите координату y: "))
        y1 = int(input("Введите координату y1: "))
        y2 = int(input("Введите координату y2: "))
        result = coordinates_rectangle(x, y, x1, y1, x2, y2)
        print(result)
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")