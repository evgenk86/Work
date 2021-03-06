# Цикл FOR
# используется для прохождения по коллекции элементов
# не только по листу, а  по итерируемому 

# Создадим лист 

import enum


numbers = [1,2,3,4,5]
# конечно можно вывести просто
print(numbers) # но в выводе мы увидим [1, 2, 3, 4, 5] в квадратных скобках

# вывести список по строчно
for i in numbers: # для i из numbers
    print(i) # выводит каждое значение присваивая его i

# можно возвести каждое значение из списка в квадрат

for i in numbers:
    print(i*i)

# Функция range

numbers = range(1,6) # тот же список от 1 до 5, если список до 100, то "range(1,101)"
for i in numbers:
    print(i)

#
for i in range(1,6): # можно ее сразу встроить в цикл 'for'
    print(i)

#  внутри цикла можно делать ветвления с помощью операторов if / else
# 
for i in range(1, 6):
    if i % 2 == 0:                  # если i делится без остатка и оно четное
        print(f'{i} is even')
    else:
        print(f'{i} is odd')        # в протичном случае нечетное


# 

numbers = [1,3,5,7,9]                     # создадим список, и чтобы изменить список и записать в него квадраты этих чисел 
for i, item in enumerate(numbers):        # введем 2 переменные. первая будет содержать текущий элемент, а вторая его же индекс
                                          # вызываем функцию enumerate в которую передаем итерируемый список
    numbers[i] *= 2

print(numbers)

# 
# можно аботать не только с числами, но и со строками
name = 'John'
for l in name: # цикл для прохода по строчке
    print(l)

# можно не вводить переменную

for _ in range(5):
    print('Alarm!') # выведет 5 раз слово "Alarm!"

# можно циклом проходиться по tuple

person = ('John', 'Silver', 22)
for item in person:                 # выводя каждый элемент
    print(item)

# список list, который содержит tuple (содержащий в себе имя и возраст) т.е. список не изменяемых объектов

persons = [('John', 22), ('Bob', 32), ('Alice', 21)]
print(len(persons)) # если мы запросим длинну списка. то получим "3", а не "6", т.к. каждый tuple считается отдельным элементом

# и чтобы достать какой либо элемент из tuple - используется tuple unpacking 

for (name, age) in persons:                     # вводим столько переменных сколько значений используется в tuple
    print(f'{name} is {age} years old')         # и можно использовать наши именованные переменные чтобы выводить определенные значения из tuple


# цикл for относительно словарей

players = dict(Carlsen = 2842, Caruana = 2822, Mamedyarov = 2801)
for item in players:                            # чтобы пройтись по ключам можно просто использовать цикл for и 1 переменную "item" и просто передать словарь
    print(item)                                 # получим именно ключи

# можно использовать функцию items чтобы получить список ключей и значений

for item in players.items():
    print(item)                                 # получаем набор tuple и тут уже можно использовать tuple unpacking

for k, v in players.items():                    # в k - у нас запишется ключ, в v - значение
    print(f'{k} has rating {v}')                # Игрок {k} имеет рейтинг {v}

# Если мы хoтим пройтись просто по значениям, то можно использовать цикл for и функцию values

for v in players.values():
    print(v)

# использование вложенного цикла, н-р поиск всех комбинаций чисел из 3х списков, которые в сумме дают 0 (ноль). 
# создадим двойной вложенный цикл из 2х списков
#  find all pairs sum of whitch equals 0
list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]

# чтобы найти все пары нужно построить двойной вложенный цикл

# создадим пустой список
pairs = []
# нужно просуммировать каждый элемент из list1 с каждым элементом из list2

for x in list1:                 # сделаем внешний цикл для прохода по первому списку
    for y in list2:             # и внутренний цикл для прохода по второму списку

# действия сколько раз он будет вызван 1раз х=2 - затем вход во второй цикл 6 раз, х = 2, y = 2 / -6 / 8 / 3 / 5 / -2; 
                                                                        # затем х = 4, у = 2 / -6 / 8 / 3 / 5 / -2 и т.д. пока х = -2 и у = -2 
# и на этом оба цикла закончатся, сперва мы выйдем из внутреннего затем из внешнего циклов

        cur_sum = x + y
        if cur_sum ==0:                 # и если их сумма == 0 
            pairs.append((x, y))        # то мы добавляем текущую пару в виде tuple в наш лист pairs
print(pairs)                            # и выведем их [(2, -2), (-5, 5), (6, -6), (-2, 2)]















    