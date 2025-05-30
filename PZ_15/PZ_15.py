#Приложение ХИМЧИСТКА для некоторой организации. БД должна содержать 
#таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента, тип 
#чистки, стоимость, скидка. 
import sqlite3 as sq
with sq.connect("PZ_15\dry_cleaning.db") as con:
    tab = con.cursor()
    tab.execute("DROP TABLE IF EXISTS services")
    tab.execute("""CREATE TABLE IF NOT EXISTS services(familiya_master varchar(20) not null, 
    name_master varchar(20) not null, otchestvo_master varchar(20) not null, client_familiya varchar(20) not null,
    client_name varchar(20) not null, client_otchestvo varchar(20) not null, cleaning_type varchar(30) not null, 
    price decimal(10, 2) not null, skidka decimal(10, 2) not null)""")
    information = [
        ("Иванов", "Алексей", "Сергеевич", "Петрова", "Мария", "Николаевна", "Сухая чистка", 1000, 200),
        ("Сидоров", "Дмитрий", "Андреевич", "Смирнова", "Анна", "Владимировна", "Химчистка", 1200, 290),
        ("Кузнецов", "Сергей", "Викторович", "Попова", "Екатерина", "Павловна", "Полная чистка", 675, 100),
        ("Васильева", "Светлана", "Юрьевна", "Лебедев", "Артем", "Олегович", "Химчистка", 500, 65),
        ("Федорова", "Ольга", "Игоревна", "Михайлов", "Николай", "Анатольевич", "Сухая чистка", 1000, 120),
        ("Соколов", "Денис", "Юрьевич", "Зайцева", "Ирина", "Николаевна", "Стирка", 1300, 250),
        ("Орлов", "Евгений", "Максимович", "Зайцева", "Анна", "Павловна", "Стирка", 950, 90),
        ("Морозов", "Савелий", "Андреевич", "Григорьева", "Виктория", "Николаевна", "Глажка", 750, 60),
        ("Волкова", "Ирина", "Михайловна", "Коваленко", "Светлана", "Анатольевна", "Глажка", 1000, 110),
        ("Михайлов", "Олег", "Николаевич", "Белова", "Анна", "Сергеевна", "Химчистка", 1250, 180)
    ]
    tab.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", information)
    #tab.execute("SELECT * FROM services WHERE familiya_master = 'Михайлов'")
    #print(tab.fetchall())
    #tab.execute("SELECT * FROM services WHERE cleaning_type = 'Полная чистка'")
    #print(tab.fetchall())
    #tab.execute("SELECT * FROM services WHERE price > 1250")
    #print(tab.fetchall())

    #tab.execute("DELETE FROM services WHERE client_familiya = ?", ("Михайлов",))
    #tab.execute("DELETE FROM services WHERE price > ?", (1000,))
    #tab.execute("DELETE FROM services WHERE skidka < ?", (100,))

    #tab.execute("UPDATE services SET price = ? WHERE client_familiya = ? AND client_name = ? AND client_otchestvo = ?", (5000, "Михайлов", "Николай", "Анатольевич"))
    #tab.execute("UPDATE services SET skidka = ? WHERE client_familiya = ? AND client_name = ? AND client_otchestvo = ?", (480, "Белова", "Анна", "Сергеевна"))
    #tab.execute("UPDATE services SET cleaning_type = ? WHERE price = ? AND skidka = ?", ("Полная чистка", 1000, 110))