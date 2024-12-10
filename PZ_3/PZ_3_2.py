#На числовой оси расположены три точки: A, B, C. 
#Определить, какая из двух последних точек (B или C) расположена ближе к A, 
#и вывести эту точку и ее расстояние от точки A.
def numeric_axis(A, B, C):
    A = float(A)
    B = float(B)
    C = float(C)
    if A < 0 or B < 0 or C < 0:
        raise ValueError("Числа не должны быть отрицательными")
    if A > B:
        distance_B = A - B
    else:
        distance_B = B - A
    if A > C:
        distance_C = A - C
    else:
        distance_C = C - A
    if distance_B < distance_C:
        axis_point = "B"
        main_distance = distance_B
    else:
        axis_point = "C"
        main_distance = distance_C
    return axis_point, main_distance
while True:
    try:
        A = int(input("Введите точку A: "))
        B = int(input("Введите точку B: "))
        C = int(input("Введите точку C: "))

        axis_result = numeric_axis(A, B, C)
        print(f"Самая близкая точка к A: {axis_result[0]}")
        print(f"Расстояние от точки A: {axis_result[1]}")
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")