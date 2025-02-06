#Книжные магазины предлагают следующие коллекции книг.  
#Магистр – Лермонтов, Достоевский, Пушкин, Тютчев 
#ДомКниги – Толстой, Грибоедов, Чехов, Пушкин. 
#БукМаркет – Пушкин, Достоевский, Маяковский. 
#Галерея – Чехов, Тютчев, Пушкин.  
#Определить в каких магазинах 
#нельзя приобрести книги Грибоедова и Маяковского
magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}
stores = {'Магистр': magistr, 'ДомКниги': dom_knigi, 'БукМаркет': bukmarket, 'Галерея': galereya}
stores_without_books = []
for store_name, books_in_store in stores.items():
    book_griboedov = 'Грибоедов' in books_in_store
    book_mayakovsky = 'Маяковский' in books_in_store
    if not (book_griboedov and book_mayakovsky):
       stores_without_books.append(store_name)
print("Магазины, где вы не можете купить книги Грибоедова и Маяковского:", stores_without_books)