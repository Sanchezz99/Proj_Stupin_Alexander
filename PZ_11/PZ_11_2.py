# Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое, 
#количество символов в тексте. Сформировать новый файл, в который поместить текст в 
#стихотворной форме предварительно поставив последнюю строку между второй и третьей.
f1 = open("PZ_11/text18-29.txt", "r", encoding="utf-16")
lines = f1.readlines()
f1.close()

print("Содержимое файла text18-29.txt:")
for i in lines:
    print(i.strip())

count_str = 0
for i in lines:
    count_str += len(i)
print(f"Количество символов в тексте: {count_str}")

last_line = lines.pop(-1)
result_line = lines[:2] + [last_line + "\n"] +lines[2:]

f2 = open("PZ_11/new_text18-29.txt", "w", encoding="utf-16")
f2.writelines(result_line)
f2.close()
