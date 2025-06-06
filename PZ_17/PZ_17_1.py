#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать 
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально 
#приближенный к оригиналу (см. таблицу 1). 
from tkinter import *
from tkinter import ttk
from tkinter import Text
root = Tk()
root.title("Обратная связь")
root.geometry("500x650")
def close():
    root.destroy()
    root.quit()

title = ttk.Label(root, text="Contact Form", font=("Arial", 14, "bold"))
title.pack(anchor='w', padx=20, pady=5)

name_label = ttk.Label(root, text="Name *")
name_label.pack(anchor='w', padx=20, pady=5)
name_entry = ttk.Entry(root, width=40)
name_entry.pack(anchor='w', padx=20)
name_pl = ttk.Label(root, text="First & Last Name", foreground='gray')
name_pl.pack(anchor='w', padx=20)

email_label = ttk.Label(root, text="Email *")
email_label.pack(anchor='w', padx=20, pady=5)
email_entry = ttk.Entry(root, width=40)
email_entry.pack(anchor='w', padx=20)
email_pl = ttk.Label(root, text="Email", foreground='gray')
email_pl.pack(anchor='w', padx=20)

phone_label = ttk.Label(root, text="Phone number *")
phone_label.pack(anchor='w', padx=20, pady=5)
phone_entry = ttk.Entry(root, width=40)
phone_entry.pack(anchor='w', padx=20)
phone_pl = ttk.Label(root, text="Phone number", foreground='gray')
phone_pl.pack(anchor='w', padx=20)

subject_label = ttk.Label(root, text="Subject *")
subject_label.pack(anchor='w', padx=20, pady=5)
subject_entry = ttk.Entry(root, width=40)
subject_entry.pack(anchor='w', padx=20)
subject_pl = ttk.Label(root, text="Select subject", foreground='gray')
subject_pl.pack(anchor='w', padx=20)

message_label = ttk.Label(root, text="Leave us a few words *")
message_label.pack(anchor='w', padx=20, pady=10)
message_text = Text(root, width=40, height=8)
message_text.pack(anchor='w', padx=20)

file_label = ttk.Label(root, text="File Attachements *")
file_label.pack(anchor='w', padx=20, pady=5)
file_frame = Frame(root)
file_frame.pack(anchor='w', padx=20)
file_button = ttk.Button(file_frame, text="Choose Files")
file_button.pack(side=LEFT)
file_text = ttk.Label(file_frame, text="No files chosen", foreground='gray')
file_text.pack(side=LEFT, padx=10)



bot_check_var = IntVar()
bot_check = Checkbutton(root, text="I'm not a robot", variable=bot_check_var)
bot_check.pack(anchor='w', padx=20, pady=(5, 0))

file_button = Button(root, text="Submit", bg="blue", fg="white")
file_button.pack(anchor='w', padx=20, pady=(15, 0))

root.mainloop()