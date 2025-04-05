#В двумерном списке элементы последнего столбца заменить на -1.
import random
rows = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов: "))
matrix = [[random.randint(0, 9) for i in range(column)] for i in range(rows)]
print("Исходная матрица: ")
for i in matrix:
    print(i)
print("Новая матрица: ")
new_matrix = [i[:-1] + [-1] for i in matrix]
for i in new_matrix:
    print(i)