numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
None_number = numbers.index(None) # находим элемент None
summa = sum(numbers[0:None_number]) + sum(numbers[None_number + 1:]) # сумма всех чисел, кроме пропущенного (None)
count = len(numbers) # Считаем кол-во элементов в изначальном списке
average = summa / (count) # Считаем среднее арифметическое
numbers[None_number] = average # Меняем пропущенный элемент None на среднее арифметическое
print("Измененный список:", numbers)
