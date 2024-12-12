def swap(X, Y):
    return Y, X
def function_input(swapping):
    while True:
        try:
            value = float(input(swapping))
            return value
        except ValueError:
            print("Увы, произошла ошибка. Введите число")
A = function_input("Введите значение A: ")
B = function_input("Введите значение B: ")  
C = function_input("Введите значение C: ") 
D = function_input("Введите значение D: ")  
A, B = swap(A, B)
C, D = swap(C, D)
B, C = swap(B, C)
print(f"Новые значения для переменных: A = {A}, B = {B}, C = {C}, D = {D}")