# from cmath import sqrt


# a = 10
# b = 5
# c = 7
# p = (a+b+c)/2

# import math
# area = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print (area)

            # Bool и None

# a = True
# print(a)
# b = False
# # type (a)

            # Экранирование кавычек
 
# a = 'John is a "strong" programmer'
# print(a)

# a = "I'm John and I'm a \"strong\" programmer"
# print(a)

# a = 'C:\\Users\\Documents'
# print(a)

# a = r'C:\Users\Documents'
# print(a)

            #  Перенос строк использование Escape последовательностей

# a = "I'm John and \nI'm a programmer"
# print(a)

# \r перевод каретки
# print("I'm John and \r\nI'm a programmer") 

# \t - табуляция
# print("I'm John and \nI'm a \tprogrammer") 

# hello = str('Hello')
# print(hello)

# greating = str('Hello, my name is John') # можно обратиться к отдельному символу по его индексу
# print (greating)
# print(greating[0]) # выведет "Н", индекс 1го символа является 0, отсчет с 0, а не с 1
# print(greating[3]) # выведет "l"
# print(greating[18]) # выведет "J"
# print(greating[-1]) # выведет "n", [-1] - отсчёт с конца
# print(greating[-4]) # выведет "J"

# new_greating='hello' # изменять строку после её создания НЕЛЬЗЯ
# print(new_greating)

        #Срезы

# greating = str('Hello, my name is John') # можно обратиться к отдельному символу по его индексу
# print (greating[2:]) # вывести построку начиная с индекса 2 включительно
# print (greating[0:3]) # указать диапазон , выведет "Hel"
# print (greating[::2]) # шаг с которым мы забираем срез, получим каждый 2ой символ строки
# print (greating[3:25:2]) # начиная с 3 по 25 символ нашей строки, забираем каждый 2ой символ

        # Конкотенация или склеивание строк

# print("My name is" + " " + "John") 

# a = "hello"
# b = "world"
# print (a + " " + b) # склеивать большое кол-во строк через + не рекомендуется, расходуется много памяти
# расходует мало памяти
# print ("%s %s" % (a, b)) # способ заполнения строк
# print ("{} {}".format(a, b)) # способ заполнения строк




