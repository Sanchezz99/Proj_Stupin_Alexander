#Дан список A размера N и целое число K (1 < K < N). 
#Преобразовать список, увеличив каждый его элемент на исходное значение элемента AK.
def common_list(A, K):
    if not (1 < K < len(A)):
        raise ValueError("K должно быть больше 1 и меньше размера списка N.")
    increment_value = A[K]
    return [i + increment_value for i in A]
try:
    A = [1, 2, 3, 4, 5, 6]
    K = 2
    modified_list = common_list(A, K)
    print("Исходный список:", A)
    print("Результирующий список:", modified_list)
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")