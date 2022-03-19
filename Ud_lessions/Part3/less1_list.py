# Коллекции, типы данных list - список

int_list = [1,2,3]                      # создание списка в квадратных скобках [1,2,3]

mixed_list = [1, 2.0, 'string']         # список может содержать различные типы данных - целые int - 1, вещественные float - 2.0, текст 'string'

# в большинстве случаев список содержит однородные данные (одного и того же типа)

# чтобы узнать длину списка - функция - len()

print(len(int_list))                    # результат выведет 3, т.к. список int_list содержит 3 элемента
print(len(mixed_list))

# можно обращаться к отдельным элементам по индексу

print(int_list[0])                      # выведет 1 элемент в списке
print(mixed_list[-1])                   # выведет последний элемент в списке

# можно делать срезы

# int_list[1:] # вывести все элементы начиная со второго элемента

print(int_list[1:]) 

# Конкотенация  - объединение списков (слияние)

names1 = ['John', 'Bob', 'Alice']
names2 = ['Tracy', 'Elijah', 'Mason']
names_combined = names1 + names2
print (names_combined)                  # ['John', 'Bob', 'Alice', 'Tracy', 'Elijah', 'Mason']

# list - является изменяемым списком, можно менять в них данные

names1[0] = 'Liam'
print(names1)                           # ['Liam', 'Bob', 'Alice']

# для добавления данных в список используется функция - 'append'

names1.append('William')
names1.append('James')
print(names1)                           # ['Liam', 'Bob', 'Alice', 'William', 'James']

# для удаления последнего элемента в списке используется функция - рор

popped = names1.pop()                   # возвращает удаленный элемент
print(popped)
print(names1)

# удаление по индексу

names1.pop(0)                           # удаление 1го элемента 
print(names1)                           # ['Bob', 'Alice', 'William']

# при использовании рор() - без индекса, по умолчанию он будет [-1] и будет удаляться последний элемент в списке

names1.append('James')                  # добавим обратно 'James'
names1.sort()                           # отсортируем его с помощью функции - sort по возрастанию
print(names1)

# Пример сортировки

letters = ['ac', 'ab', 'aa']
letters.sort()
print(letters)                          # ['aa', 'ab', 'ac']

# Пример сортировки по ключу

letters1 = ['abc', 'a', 'ab']
letters1.sort(key=len)                  # сортировка по длине 
print(letters1)                         # ['a', 'ab', 'abc']

# Пример сортировки чисел по возрастанию

numbers = [3,2,8,5,0,3,4,1,1]
print(numbers)                          # [3, 2, 8, 5, 0, 3, 4, 1, 1]
numbers.sort()                          
print(numbers)                          # [0, 1, 1, 2, 3, 3, 4, 5, 8]

# Пример реверсирования списка / задом наперёд (это не сортировка по убыванию!!!)

numbers = [3,2,8,5,0,3,4,1,1]           # [3, 2, 8, 5, 0, 3, 4, 1, 1]
numbers.reverse()
print(numbers)                          # [1, 1, 4, 3, 0, 5, 8, 2, 3]

# Пример сортировки чисел по убыванию

numbers = [3,2,8,5,0,3,4,1,1]           # [3, 2, 8, 5, 0, 3, 4, 1, 1] 
numbers.sort(reverse=True)
print(numbers)                          # [8, 5, 4, 3, 3, 2, 1, 1, 0]

# Пример добавления в список по индексу

numbers = [3,2,8,5,0,3,4,1,1]           # [3, 2, 8, 5, 0, 3, 4, 1, 1] 
numbers.insert(1, 22)                   # вставить между 1 и 2 значение 22
print (numbers)                         # [3, 22, 2, 8, 5, 0, 3, 4, 1, 1]

# Пример поиска к-либо элемета функция - index

numbers = [3,2,8,5,0,3,4,1,1]           # [3, 2, 8, 5, 0, 3, 4, 1, 1] 
print(numbers.index(5))                 # возвращает значение индекса по которому находится тот или иной элемент (первое совпадение)
                                        # в нашем случае вернет индекс "3", т.к. "5" находится по этому значению индекса 

print(numbers.index(3, 1, 8))           # можно указать интервал - с какого индекса начать поиск и по какой производить поиск 

# если индекс не находит элемента то он выдает ошибку Value Error

# print(numbers.index(42))              # ValueError: 42 is not in list


# для поиска кол-ва вхождений того или иного элемента используется функция 'count'

print(numbers.count(3))                 # результат 2, т.к. 3(троек) в нашем списке [3, 2, 8, 5, 0, 3, 4, 1, 1] - 2шт.

# для создания копии списка функция - copy

copy = numbers.copy()
print(copy)

# Функция copy - возвращает поверхностную копию списка, 
# т.е. если список содержит изменяемые типы данных, то изменив внутр.состояние к-либо элемента в исходном списке
# эти изменения отразятся и в нашей копии


# Функция clear - очистка списка

numbers.clear()
print(numbers) # на выходе мы получим пустой список

