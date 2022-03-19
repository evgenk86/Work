        # Строки и байты str, bytes, bytesarray

import sys
from unittest import result
print(sys.getdefaultencoding()) # узнать какую кодировку использует данный компьютер

# Функция 'ord' возвращает код введенного символа в таблице юникод

print(ord('a')) # 97

# Функция 'chr' преобразует код символа по таблице юникод в букву

print(chr(97)) # a

# Кодировочные таблицы

s = 'hello' # переведём его в байты используя функцию encode
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8') # передаем кодировочную таблицу
enc_utf16 = s.encode('utf16')

print(type(enc_ascii)) # выведем тип переменных / метод encode возвращает тип <class 'bytes'>
print(enc_ascii) # b'hello' - префикс - b, означает что представление байтовое
print(enc_utf8) # b'hello'
print(enc_utf16) #b'\xff\xfeh\x00e\x00l\x00o\x00'


# узнать какое кол-во байтов используется для представления этих строк
print(len(enc_ascii)) # результат - 5 , т.о. выделяет 1 байт на каждый символ
print(len(enc_utf8))  # результат - 5 , т.о. выделяет 1 байт на каждый символ
print(len(enc_utf16)) # результат - 12 , т.о. выделяет 2 байта на каждый символ


str_in_bytes = b'hello' # либо можно сразу использовать 
str_in_bytes1 = s.encode('utf8') # либо можно передать кодировочную таблицу

str_in_text = 'hello'
print(type(str_in_bytes))  # тип <class 'bytes'>
print(type(str_in_bytes1)) # тип <class 'bytes'>
print(type(str_in_text))   # тип <class 'str'>

# можно вызвать напрямую

print('bytes'.encode('utf8')) # b'bytes'
print('байты'.encode('utf8')) # b'\xd0\xb1\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'

# можно вывести один символ из слова / строки
print(str_in_bytes[0]) # например 1ый символ 'h' - получим 104
print(str_in_text[0])  # например 1ый символ 'h' - получим h

# str_in_bytes[0] = 10 # получим ошибку т.к. тип не изменяемый

# если нужно поменять то используется bytearray

ba = bytearray(b'hello')
ba[0] = 87
print(ba) # bytearray(b'Wello') - заменил h на заглавную W

#  нельзя так делать он будет считать все символы
result = str(str_in_bytes)
print(result)                   # b'hello'
print(len(result))              # 8 - символов

result = str(str_in_bytes, 'utf8') # нужно передавать кодировку 
print(result)             

# перевод строк в байты

result = str_in_bytes.decode('utf8')
print(result)

# запись в файл каких либо значений

jpeg = [120, 3, 255, 0, 100]
with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/btest.bin', mode = 'w+b' ) as file: # если забудете 'b' то прочтете байты как текст
        file.write(bytes(jpeg))

with open('/media/evgen/2E29-A776/Documentz/Work/Udemy/btest.bin', mode = 'rb' ) as file:
     data = file.read()
     for b in data:
             print(int(b))

