# ДЗ - 4. Joined List

# На вход подаются два списка чисел длины N.
# Задача. Взять из первого списка все нечетные чсла, из второго четные и объединить их в новом спсике с названием joined_list.
# Примечание. Можно сделатьдвумя циклами for, можно одним, можно с помощью list comprehension

# import sys

# first_lst = sys.argv[1]
# second_lst = sys.argv[2]

# ваше решение ниже:

first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

joined_list = [] # завести пустой список, и добавлять в него значения

for x in first_list: # цикл для первого списка
    if x % 2 !=0: # проверка делимости без остатка, если не равно != 0 - значит нечетное
        joined_list.append(x) # добавлять в него х если условие выполняется не равно 0 - значения нечетные

for x in second_list: # цикл для второго списка
    if x % 2 ==0: # проверка делимости без остатка, если равно == 0 - значит четное
        joined_list.append(x) # добавлять в него х если условие выполняется - остаток равен 0 - значения четные

print(joined_list)

# или так через list comprehension:

first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

odds = [x for x in first_list if x % 2 !=0]
evens = [x for x in second_list if x % 2 ==0]

joined_list = odds + evens
print(f'Merged list: {joined_list}')






