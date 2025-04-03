#В двумерном списке элементы последнего столбца заменить на -1.
import random
rows = 3
column = 3
matrix = [[random.randint(0, 9) for i in range(column)] for i in range(rows)]
new_matrix = [i[:-1] + [-1] for i in matrix]
for i in new_matrix:
    print(i)