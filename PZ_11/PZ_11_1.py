#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной 
#последовательности из целых положительных и отрицательных чисел. Сформировать 
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
#обработку элементов: 
#Элементы первого и второго файлов: 
#Количество элементов первого и второго файлов: 
#Количество элементов, общих для двух файлов: 
#Количество четных элементов первого файла: 
#Количество нечетных элементов второго файла:
f1 = open("PZ_11/file1.txt", "w")
f1.write("4 5 6 -8 -7 1")
f1.close()

f2 = open("PZ_11/file2.txt", "w")
f2.write("-3 3 4 8 5 6")
f2.close()

f1 = open("PZ_11/file1.txt", encoding="utf-8")
list1 = [int(i) for i in f1.read().split()]
f1.close()

f2 = open("PZ_11/file2.txt", encoding="utf-8")
list2 = [int(i) for i in f2.read().split()]
f2.close()

elements_common = ""
for i in list1:
    elements_common += str(i) + " " 
for i in list2:
    elements_common += str(i) + " "
elements_common = elements_common.strip()

count1 = len(list1)
count2 = len(list2)

common_el = len(set(list1) & set(list2))

numbers_one = 0
for i in list1:
    if i % 2 == 0:
        numbers_one += 1

numbers_two = 0
for i in list2:
    if i % 2 != 0:
        numbers_two += 1

f4 = open("PZ_11/result.txt", "w")
f4.write(f"Элементы первого и второго файлов:\n{elements_common}\n")
f4.write(f"Количество элементов первого и второго файлов: {count1} и {count2}\n")
f4.write(f"Количество элементов, общих для двух файлов: {common_el}\n")
f4.write(f"Количество четных элементов первого файла: {numbers_one}\n")
f4.write(f"Количество нечетных элементов второго файла: {numbers_two}\n")
f4.close()