        # Операторы сравнения

#   2 > 1

# Результатом сравнения может быть True или False

    # узнать какой тип
result = 2 > 1
print (type (result)) # <class 'bool'>

print (2 > 2)  # False
print (2 >= 2) # True
print (3 >= 2) # True
print (3 >= 4) # False

print (2 < 3)  # True
print (3 < 2)  # False
print (3 <= 3) # True
print (3 <= 2) # False
print (3 <= 4) # True

print (1 == 1)      # True - Сравнение - Равно!

print (1 != 1)      # False - Не Равно!

print (2 != 1)      # True - 2 - Не Равно - 1

    # Можно сравнивать строки

print ("string" == "string")            # True
print ("string" == "another string")    # False
print ("String" == "string")            # False

# можно сравнивать приводя к нижнему или верхнему регистрам / корректность проверки

x = "String"
y = "string"
print (x.lower() == y.lower()) # привели обе строки к нижнему регистру

# Построение цепочек
1 < 2 < 3 # True

print(1 < 2 < 3)
# или
print (1 < 2 and 2 < 3) # Это выражение более читабельно
# Оно будет True если оба выражения выполняются
print (1 > 2 and 2 < 3) # False т.к. 1ое значение не выполняется

print (1 > 2 or 2 < 3) # True / Проверка на истинноcть лишь одного выражения
# одно значение True другое False, для него достаточно лишь одного значения True

print (1 > 2 and 2 > 3) # False 

# Пример 1
is_admin = True
file_exists = False

should_open_file = is_admin and file_exists
should_open_file

# Пример 2
is_admin = False
if not is_admin:
    print('not an admin')

if is_admin == False:
    print('not an admin')



