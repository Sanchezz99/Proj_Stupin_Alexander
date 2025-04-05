#Организовать и вывести последовательность на N произвольных целых 
#элементов, сформировать новую последовательность куда поместить положительные 
#четные элементы, найти их сумму и среднее арифметическое. 
elements = list(map(int, input("Введите числа через пробел: ").split()))
first_elements = list(filter(lambda x: x > 0 and x % 2 == 0, elements))
second_elements = sum(first_elements)
third_elements = second_elements / len(first_elements)
print("Изначальная последовательность:", elements)
print("Новая последовательность:", first_elements)
print("Сумма новой последовательности:", second_elements)
print("Среднее арифметическое новой последовательности:", third_elements)