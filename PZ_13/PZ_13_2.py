#В двумерном списке элементы третьей строки заменить элементами из одномерного 
#динамического массива соответствующей размерности.
import random
rows = 3
column = 3
matrix = [[random.randint(0, 9) for i in range(column)] for i in range(rows)]
print("Исходная матрица:")
for i in matrix:
    print(i)
new_matrix = [random.randint(0, 9) for i in range(column)]
print("Элементы для новой матрицы:", new_matrix)
matrix[2] = new_matrix
print("Новая матрица:")
for i in matrix:
    print(i)