#Составить генератор (yeild), который преобразует все буквенные символы в строчные.
import string
def new_function(input_string):
    for i in input_string:
        if i in string.ascii_letters:
            yield i.lower()
        elif i == ' ':
            yield i
first_string = "hEllo mY DeAr friend"
new_string = "".join(new_function(first_string))
print("Исходный текст:", first_string)
print("Измененный текст:", new_string)