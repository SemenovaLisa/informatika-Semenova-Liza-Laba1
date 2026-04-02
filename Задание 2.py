import csv
import json
from io import StringIO

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

# Исходные данные CSV
csv_data = """longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value
-122.050000,37.370000,27.000000,3885.000000,661.000000,1537.000000,606.000000,6.608500,344700.000000
-118.300000,34.260000,43.000000,1510.000000,310.000000,809.000000,277.000000,3.599000,176500.000000
-117.810000,33.780000,27.000000,3589.000000,507.000000,1484.000000,495.000000,5.793400,270500.000000
-118.360000,33.820000,28.000000,67.000000,15.000000,49.000000,11.000000,6.135900,330000.000000"""

def task() -> None:
    csv_file_izn = StringIO(csv_data)  # Переделываем CSV данные
    csv_reader = csv.DictReader(csv_file_izn) # Используем DictReader для чтения CSV данных
    data = list(csv_reader) # Преобразуем данные в список словарей

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file: # Записываем данные в JSON файл с отступами равными 4
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__': # Реализовываем конвертер из csv в json формата
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")