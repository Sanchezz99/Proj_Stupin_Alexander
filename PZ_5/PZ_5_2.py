#Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y 
#(X и Y — вещественные параметры, являющиеся одновременно входными и выходными). 
#С ее помощью для данных переменных A, B, C, D последовательно 
#поменять содержимое следующих пар: 
#A и B, C и D, B и C и вывести новые значения A, B, C, D.
def swap(X, Y):
    return Y, X
def function_input(swapping):
    while True:
        try:
            value = float(input(swapping))
            return value
        except ValueError:
            print("Увы, произошла ошибка. Пожалуйста, введите действительное число.")
A = function_input("Введите значение A: ")
B = function_input("Введите значение B: ")  
C = function_input("Введите значение C: ") 
D = function_input("Введите значение D: ")  
A, B = swap(A, B)
C, D = swap(C, D)
B, C = swap(B, C)
print(f"Новые значения для переменных: A = {A}, B = {B}, C = {C}, D = {D}")