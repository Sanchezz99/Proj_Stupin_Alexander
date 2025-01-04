#Дан символ C и строки S, S0. После каждого вхождения символа C в строку S 
#вставить строку S0.
def common_line(S, C, S0):
    if len(C) != 1:
        raise ValueError("Строка C должна содержать один символ.")
    if S == "":
        raise ValueError("Строка S не должна быть пустой.")
    if S0 == "":
        raise ValueError("Строка S0 не должна быть пустой.")
    result = ""
    for char in S:
        result += char
        if char == C:
            result += S0
    return result
S = input("Введите строку S: ")
C = input("Введите символ C (один символ): ")
S0 = input("Введите строку S0: ")
try:
    common_result = common_line(S, C, S0)
    print(f"Исходная строка: '{S}'")
    print(f"Результат: '{common_result}'")
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")