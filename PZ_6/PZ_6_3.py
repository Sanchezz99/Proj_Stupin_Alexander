#Дан список размера N. Осуществить сдвиг элементов списка вправо на одну позицию 
#(при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, 
#a исходное значение последнего элемента будет потеряно). 
#Первый элемент полученного списка положить равным 0. 
import random
def integer_list(A):
    return [0] + A[:-1]
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