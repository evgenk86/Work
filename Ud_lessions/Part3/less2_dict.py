# dict - словари

# список пар: ключ - значение, например: записная книга, где ключ - это фамилия, а номер телефона - это значение
# зная ключ, можно быстро найти его значение
# взять значение по ключу, работает гораздо быстее чем поиск по списку / при условии что мы знаем ключ  

players = {
                'Carlsen': 2842,
                'Caruana': 2822,
                'Mamedyanov': 2801,
                'Ding': 2797,
                'Giri': 2780
          }
print (players)

# если у нас вместо ключей используются просто строчки, а в качестве значений числа, то можно использовать др. вариант записи

players = dict(Carlsen=2842, Caruana=2822, Mamedyanov=2801, Ding=2797, Giri=2780)
print (players)

# для того чтобы вытащить значение по ключу, мы можем использовать синтаксис доступа по индексу, в качестве индекса мы указываем ключ

# Пример поиск по Фамилии для вывода его рейтинга

top1 = players['Carlsen']
print(f"Top chess player's rating is: {top1}")

# можно использовать функцию 'get' - для поиска по ключу

print(players.get('Carlsen'))

# для добавления нового игрока в конец списка

players ['So'] = 2780
print(players)

# можно переназначить значение ключу

players ['So'] = 2781
print(players)

# удаление по ключу

del players ['So']
print(players)

# для просмотра всех ключей словаря используется функция - keys

keys = players.keys()
print(type(keys))           # тип ключей <class 'dict_keys'>
print(keys)                 # dict_keys(['Carlsen', 'Caruana', 'Mamedyanov', 'Ding', 'Giri'])

# иногда более удобно работать со списком ключей, т.к. список иногда предоставляет другие и более удобные функции обработки
# для конвертации используется функция - list

l = list(players.keys())    # передаем в функцию list
print(type(l))              # тип ключей <class 'list'>
print(l)                    # ['Carlsen', 'Caruana', 'Mamedyanov', 'Ding', 'Giri']

# сортировка ключей

print(sorted(players.keys())) # получаем отсортированный по возростанию список ['Carlsen', 'Caruana', 'Ding', 'Giri', 'Mamedyanov']

# для проверки находится ли данный ключ в словаре

print('Carlsen' in players)         # проверка есть ли 'Carlsen' в словаре, т.к. он есть в словаре получаем - True
print('Kramnik' not in players)     # проверка нет ли  'Kramnik' в словаре, т.к. его нет в словаре получаем - True

# можно просмотреть не только список ключей, но и список значений в словаре / функция - values

vals = players.values()
print(type(vals))               # возвращает список типа <class 'dict_values'>
print(vals)                     # dict_values([2842, 2822, 2801, 2797, 2780])

# если хотим поработать со списком, то можно так же вызвать функцию - list

vals1 = list(players.values())
print(type(vals1))               # возвращает список типа <class 'list'>
print(vals1)                     # [2842, 2822, 2801, 2797, 2780]   

# сортировка

print(sorted(players.values()))     # values "скормить" функцию sorted и получить сортированные значения - [2780, 2797, 2801, 2822, 2842]

# создание копии / возвращается поверхностная копия

players_copy = players.copy()
print(players_copy)

# через цикл (объявляем 2 переменные k, v которые будут содержать в себе значения на каждой итерации)

for k, v in players.items():
    print(k, v)


# тип класс

items = players.items()
print(type(items))                  # возвращает список типа class 'dict_items'> / ключ - значение

# для удаления значения по ключу можно использовать рор - передавая ей ключ

players.pop('Giri')
print(players)                      # как видим Giri в списке отсутсвует {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyanov': 2801, 'Ding': 2797}

# для удаления с конца используется - pop.items / возвращает удаляемый элемент

print(players.popitem())
print(players)

# подсчет пар / ключ - значение через функцию len

print(len(players))         # в данном случае у нас "3" пары в словаре

# Функция setdefault - если запрашиваемого значения нет, то она добавляет ключ в словарь, а в качестве его значения вставляет None

players.setdefault('Karjakin')
print(players)              # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyanov': 2801, 'Karjakin': None}


# мы не можем добавлять уже существующие ключи, т.к. они должны быть уникальны, 
# и иметь два элемента с одинаковым ключом словарь запрещает, этого сделать не получится





