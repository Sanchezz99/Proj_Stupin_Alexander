#Дан список A размера N и целое число K (1 < K < N). 
#Преобразовать список, увеличив каждый его элемент на исходное значение элемента AK.
import random
def common_list(A, K):
    if not (1 < K < len(A)):
        raise ValueError("K должно быть больше 1 и меньше размера списка N.")
    increment_value = A[K]
    return [i + increment_value for i in A]
try:
    N = int(input("Введите количество элементов в списке A: "))
    if N <= 0:
        raise ValueError("Количество элементов должно быть больше 0.")
    A = [random.randint(1, 100) for _ in range(N)]
    K = int(input("Введите значение K: "))
    modified_list = common_list(A, K)
    print("Исходный список:", A)
    print("Результирующий список:", modified_list)
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")