new_list = []
new_list.append(1)
new_list.append('stroka')
#.append добавляет в список значение
#создаёт лист в листе


second_list = [1,'gg']

third_list = []
third_list.extend(new_list)
#.extend вставляет однов другое
#сливает обе строки в одну


new_list.extend(2,44)
#добавляет значение под определёным индексем
#при этом другие отодвигаются на индекс ниже

new_list.remove(14)
#Удаляет первый значение с таким значением

new_list.pop(2)
#удаляет значение по индексу
#удаляет с конца