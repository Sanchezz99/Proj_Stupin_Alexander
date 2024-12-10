#Даны положительные числа A, B, C. 
#На прямоугольнике размера A х B 
#размещено максимально возможное количество квадратов со стороной C (без наложений). 
#Найти количество квадратов, размещенных на прямоугольнике. 
#Операции умножения и деления не использовать.
def count_squares(A, B, С):
    try:
        if A <= 0 or B <= 0 or C <= 0:
            raise ValueError("Длина и ширина должны быть положительными, а сторона больше 0")
        count = 0
        while B >= C:
            width_count = 0
            remaining_width = A
            while remaining_width >= C:
                width_count += 1
                remaining_width -= C
            count += width_count
            B -= C
        return count
    except ValueError as e:
        print(f"Увы, произошла ошибка: {e}")
        return None
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
result = count_squares(A, B, C)
if result is not None:
    print("Колличество квадратов, размещенных на прямоугольнике:", result)