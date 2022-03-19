# named tuples именованные кортежи

players = [('Carlsen', 1990, 2842), ('Caruana', 1992, 2822), ('Mamedyarov', 1985, 2801)]
print(players[0])
# Если захотим обратиться по индексу и имени

# print (players[0].name) # Выдаст ошибку - AttributeError: 'tuple' object has no attribute 'name'

# нужно импортировать коллекции 'namedtuple'

from collections import namedtuple
Player = namedtuple('Player', 'name age rating') # передаем имя класса и имена элементов
players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]

print(players[0]) # если мы обратимся по [0] то получим tuple - Player(name='Carlsen', age=1990, rating=2842), к которому можно обратиться по 'name', 'age' или 'rating'

print (players[1].name)
print (players[1].age)
print (players[1].rating)

# т.о. мы получаем класс Player с атрибутами которые не могут быть изменены