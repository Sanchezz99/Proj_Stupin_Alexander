#Разработать программу с применением пакета tk, взяв в качестве условия одну 
#любую задачу из ПЗ №№ 2 – 9. 
from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Генератор символов")
root.geometry("500x250")
def close():
    root.destroy()
    root.quit()

def generate():
    result = ""
    for _ in range(40):
        result += chr(random.randint(32, 126))
    label.config(text=result)

button = ttk.Button(root, text="Сгенерировать 40 символов", command=generate)
button.pack(pady=10)

label = ttk.Label(root, text="")
label.pack(pady=10)

root.mainloop()