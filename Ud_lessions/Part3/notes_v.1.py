import time
import os
 
 
print('Заметки')
time.sleep(1)
 
def x():
    global data
    global zametka
    global opisanie
    
    data = (input("На какую дату поставить заметку?\n"))
    print('Дата заметки:', data)
    time.sleep(1)
    
    zametka = (input("Какое будет название: \n"))
    print('Дата заметки: ', data, '\nНазвание заметки: ', zametka)
    time.sleep(1)
 
    opisanie = (input("Напишите описание заметки: \n"))
    print('Дата заметки: ', data, '\nНазвание заметки: ', zametka, '\nОписание заметки: ', opisanie)
    time.sleep(2)
 
def m():
    with open('Заметка.txt', 'w+') as f:
        f.write('Дата заметки: ' + data + '\nНазвание заметки: '+ zametka + '\nОписание заметки: '+ opisanie)
 
def y():
    return input('Напишите sos, что бы посмотреть все комманды: ')
x()
 
time.sleep(2)
m()
print('Заметка создана!')
 
a = y()
 
while True:
    if  a == 'sos':
        sos = (input('Delete - удаление заметки\nExit - выход с программы\nCreate - создание новой заметки\nEdit - редактирование заметки\n'))
        if sos == 'Delete':
            data = 'Пусто'
            zametka = 'Пусто'
            opisanie = 'Пусто'
            time.sleep(1)
            (os.remove("Заметка.txt"))
            print('Заметка удалена')
            time.sleep(1)
            y()
            
        elif sos == 'Exit':
            time.sleep(1)
            break
        elif sos == 'Edit':
            x()
            time.sleep(1)
            print('Редактирование завершено')
            m()
            y()
        elif sos == 'Create':
            print('В разработке')
            time.sleep(1)
            y()
 