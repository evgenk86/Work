# # ДЗ - 3. Division by 3 or 5

# Вы получаете ввод читсла от пользователя.
# Постороить цикл от 0 до введенного числа (включительно) 
# и посчитать сумму всех чисел, делимых без отатка на 3 и 5. 
# Вывести на консоль это число
# Примечание: задача решается как прямым for, так и с помощью list comprehension
# (просуммировать числа "профильтрованного" списка можно, передав список в функцию sum(agr_list)).


# Решение 1:

limit = int(input('Введите число: ')) # получили ввод числа от пользователя, например 10

arglist = 0
for v in range(limit + 1):                      
    if v % 3 ==0 or v % 5 ==0:
        arglist += v

print(arglist)

# или так через list comprehension:

arglist = [ i for i in range(limit + 1) if i % 3 == 0 or i % 5 ==0]
print(sum(arglist))

# Решение 2:

limit = int(input('Введите число: ')) # Ввод значений

total_sum = 0 # введем переменную в которую будем накапливать значения
for v in range(limit + 1):
    if v % 3 == 0 or v % 5 == 0:
        total_sum +=v

print(total_sum)

# или так через list comprehension:

arglist = sum([i for i in range(limit + 1) if i % 3 == 0 or i % 5 ==0])
print(f'Total sum = {arglist}')










