# Форматирование строк

print ('my name is {}'.format('John')) # plaseholder {}


my_name = 'John'
print ('my name is {}'.format(my_name)) # my name is John


print ("my name is {} and I'm {}".format('John', 30)) # my name is John and I'm 30

print ("my name is {0} and I'm {1}".format('John', 30)) # аргументы индексируются как 0, 1, 2, и т.д.

print ("my name is {1} and I'm {0}".format('John', 30)) # если поменять местами, то получим - my name is 30 and I'm John

# В нормальных случаях всегда индекс начинается с 0, очень редко меняют местами- это усложняет понимание кода

# более краткая форма вывода форматирования срок - f - формат / ИНТЕРПОЛЯЦИЯ СТРОК
name = "John"
age = 30
print(f'My name is {name} and I\'m {age}')

# Пример

pi= 3.1415
print("Pi equals {pi:1.2f}".format(pi=pi))

# или через ИНТЕРПОЛЯЦИЮ СТРОК - более краткая форма 

print(f"Pi equals {pi:1.2f}")

# {pi:1.2f}, где f - означает что мы форматируем float - число с плавающей точкой
# .2 - означает что мы хотим вывести только 2 символа после "."
# 1 - означает - не добавлять пробелы в перед этим числом









