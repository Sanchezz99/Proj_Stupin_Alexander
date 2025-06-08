#Дан целочисленный список A размера N. Переписать в новый целочисленный список B
#того же размера вначале все элементы исходного списка с четными номерами,
#а затем — с нечетными: A2,  А4,  А6, …,  A1,  A3,  А5, … .
#Условный оператор не использовать. 
import random
def integer_list(A):
    B = A[1::2] + A[::2]
    return B
try:
    N = int(input("Введите количество элементов в списке A: "))
    if N <= 0:
        raise ValueError("Количество элементов должно быть больше 0.")
    A = [random.randint(1, 100) for _ in range(N)]
    modified_list = integer_list(A)
    print("Исходный список:", A)
    print("Результирующий список:", modified_list)
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")