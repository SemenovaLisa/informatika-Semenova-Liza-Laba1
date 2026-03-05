disket_size = 1.44 # объем дичкеты (Мб)
pages = 100 # кол-во страниц в книге
stroki_on_pages = 50 # число строк на странице
simvol_on_stroka = 25 # кол-во символов в строке
hranenie = 4 # необходимое для хранения символа
disket_size_b = disket_size * 1024 * 1024 # Переводим объем из Мб в байты
all_simvol = pages * stroki_on_pages * simvol_on_stroka # Всего символов в книге
book_size = all_simvol * hranenie # Посчитали объем книги в байтах
count_book = int(disket_size_b // book_size)
print("Количество книг, помещающихся на дискету:", count_book)
