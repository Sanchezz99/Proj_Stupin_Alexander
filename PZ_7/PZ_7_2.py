#Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку, 
#расположенную между первым и вторым пробелом исходной строки. Если строка 
#содержит только один пробел, то вывести пустую строку.
def common_line(input_string):
    if not input_string.strip():
      raise ValueError("Строка не должна быть пустой.")
    words = input_string.split()
    if len(words) < 3:
        return "", words
    return words[1], words
try:
    input_string = input("Введите строку: ")
    common_result, common_string = common_line(input_string)
    print(f"Исходный список слов: {common_string}")
    print(f"Результирующее слово: '{common_result}'")
except ValueError as e:
    print(f"Увы, произошла ошибка: {e}")