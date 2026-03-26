def find_item_index(items_list, target_item):
    for index, item in enumerate(items_list):
        if item == target_item:
            return index
    return None # В случае, если товар не найден, то возвращаем
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # Список

for find_item in ['банан', 'груша', 'персик']: # Список товаров, которые нужно найти
    index_item = find_item_index(items_list, find_item) # Ищем нужный товар
    if index_item is not None: # Проверим результат
        # Если товар найден, то выводим результат
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
        # Если товар не найден, то пишем "Товар не найден"
    else:
        print(f"Товар '{find_item}' не найден в списке.")
