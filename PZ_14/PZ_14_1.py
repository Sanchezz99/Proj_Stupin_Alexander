#В исходном текстовом файле(hotline1.txt) найти все номера телефонов, 
#соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных 
#элементов. После фразы «Горячая линия» добавить фразу «Министерства
#образования Ростовской области», выполнив манипуляции в новом файле.
import re
phone_number = r"8\(\d{3}\)\d{3}-\d{2}-\d{2}"
with open("PZ_14/hotline1.txt", "r", encoding="utf-8") as file:
    information = file.read()
phone_number_f = re.findall(phone_number, information)
count = len(phone_number_f)
print("Кол-во номеров в файле hotline.txt:", count)
new_hotline = information.replace("Горячая линия", "Горячая линия Министерства образования Ростовской области")
with open("PZ_14/new_hotline.txt", "w", encoding="utf-8") as new_file:
    new_file.write(new_hotline)