        # Операции над файлами (чтение, изменение, удаление)

# Узнать в какой текущей директории находишься
# import os
# dirpath = os.getcwd()

# Создание файла и запись текста в него

my_file = open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt', 'w')
my_file.write('Name|Phone\nBob;12345\nJohn;56789\nAlice;95123\n')
my_file.close()

# Просмотр файла его атрибутов и кодировки / <_io.TextIOWrapper name='sample.txt' mode='r' encoding='cp1251'>
file = open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt')
print (file)

# Чтение файла
data = file.read() # курсор достиг конца
print (type(data)) # <class 'str'> - класс String - строковый
print (data) 

#     # курсор достиг конца и если снова вызвать @read@ то мы ничего не увидим. т.к. курсор в конце строки
#     # print(file.read())

#     # чтобы переместить курсор в начал файла можно вызвать функцию @seek@ и прочитать файл снова с самого начала
file.seek(0)
#     # print(file.read())

#     # <class 'str'> - тип String - строковый, но если мы хотим прочитать построчно и получить список строк

lines = file.readlines()
print(type(lines)) # вывод типа 
print(lines) # вывод содержимого
print(len(lines)) # вывод количества строк в файле

#     # открытие файла из другой директории

#     # sample_file = open(r'D:\Udemy\sample.txt') # экранирование через 'r'
#     # sample_file = open('D:\\Udemy\\sample.txt') # запись через "//"
sample_file = open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt') # для Linux

#     # по окончании работы с файлами нужно их закрывать, 
#     # чтобы избегать ошибок с утечками памяти и конкурентным доступом к одному и тому же файлу одновременно

file.close()
sample_file.close()
print (file.closed) # можно узнать их статус - закрылись они или нет True или False
print (sample_file.closed)

# Пример
# Использование специального синтаксиса с "with" чтобы не забывать закрывать файл после работы с ним
with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt') as sample_file:
    sample_data = sample_file.read()
print(sample_data) # по завершению данного блока кода, файл будет закрыт автоматически

print (sample_file.closed) # проверка статуса - закрылся он или нет True или False

# Режимы открытия файлов

#  'r' - чтение / поумолчанию если неуказывать параметр, то он открывается в режиме чтения
#  'w' - только запись / прочитать не получится / 
# если уже есть такой файл, который мы открываем в режиме "w", то все содержимое в нём будет затёрто /
# если файл на момент открытия не существовал, то он будет создан автоматически
#  'a' - добавление в конец 
# 'r+' - чтение и запись / файл уже должен существовать
# 'w+' - чтение и запись / если уже есть такой файл, который мы открываем в режиме "w+", то все содержимое в нём будет затёрто /
# если файл на момент открытия не существовал, то он будет создан автоматически

        
        # выведет ошибку т.к. в режиме "w" нельзя читать файл
    # with open('sample.txt', mode = 'w' ) as sample_file: 
    #     data = sample_file.read() # пытаемся прочитать файл
 

with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt', mode = 'a' ) as sample_file: 
    sample_file.write('Eric;62345')

with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt', mode = 'r' ) as sample_file: 
    data = sample_file.read()
print(data)

# если нужно читать и сразу запысывать в файл то
# некоторые открывают отдельно на запись и отдельно на чтение , делать 2 операции with open

with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/sample.txt', mode = 'r+' ) as sample_file: # допустим мы хотим допистаь в конец некоторые данные
# курсор находится в начале строки и его нужно переместить в конец файла
    sample_file.seek(0, 2) # указывает конец байта, конец файла (с [-1] тут не сработает)
    sample_file.write('\nToub;56478') # допишем в конец файла
    sample_file.seek(0)  # переместим курсор вновь в начало файла для последующего прочтения его
    print(sample_file.read()) # прочтем его

# Режим 'w+'

with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/Part2/abracadabra.txt', mode = 'w+') as spell_file: # создается файл если он не существует 
    # и открывается в режиме записи
    spell_file.write('abra-abra-abra-cadabra') # записывается текст
    spell_file.seek(0) # перемещается курсор в начало файла
    print(spell_file.read()) # прочитали содержимое файла и вывели его не экран





