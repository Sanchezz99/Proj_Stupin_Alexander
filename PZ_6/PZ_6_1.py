#Дан список A размера N и целое число K (1 < K < N). 
#Преобразовать список, увеличив каждый его элемент на исходное значение элемента AK.
def common_list(A, K):
    if not (1 < K < len(A)):
        raise ValueError("K должно быть больше 1 и меньше размера списка N.")
    increment_value = A[K]
    return [i + increment_value for i in A]
try:
    user_input = input("Введите элементы списка A, разделенные запятыми: ")
    A = [int(x.strip()) for x in user_input.split(',')]
    K = int(input("Введите значение K: "))
    modified_list = common_list(A, K)
    print("Исходный список:", A)
    print("Результирующий список:", modified_list)
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")