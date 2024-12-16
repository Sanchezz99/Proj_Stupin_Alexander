#Дан список размера N. Осуществить сдвиг элементов списка вправо на одну позицию 
#(при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, 
#a исходное значение последнего элемента будет потеряно). 
#Первый элемент полученного списка положить равным 0. 
def shift_elements(A):
     if type(A) is not list:
        raise TypeError("Входные данные должны быть списком.")
     return [0] + A[:-1]
try:
    A = [1, 2, 3, 4, 5, 6]
    modified_list = shift_elements(A)
    print(modified_list)
except TypeError as e:
    print(f"Увы, произошла ошибка: {e}")