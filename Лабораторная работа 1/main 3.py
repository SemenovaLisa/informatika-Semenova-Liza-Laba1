list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
middle_index = len(list_players) // 2 # находим индекс середины
# Делим на две команды:
first_team = list_players[:middle_index] # первая команда
second_team = list_players[middle_index:] # вторая команда

print(first_team)
print(second_team)
