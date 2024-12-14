#Дан целочисленный список A размера N. Переписать в новый целочисленный список B
#того же размера вначале все элементы исходного списка с четными номерами,
#а затем — с нечетными: A2,  А4,  А6, …,  A1,  A3,  А5, … .
#Условный оператор не использовать. 
def integer_list(A):
    if type(A) is not list:
        raise ValueError("Входные данные должны быть списком.")
    B = A[::2] + A[1::2]
    return B
try:
    A = [2, 4, 6, 8, 10, 12]
    modified_list = integer_list(A)
    print(modified_list)
except ValueError as e:
    print(f"Увы, произошла ошабка: {e}")
