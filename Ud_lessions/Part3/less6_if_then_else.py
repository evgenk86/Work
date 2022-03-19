#  Логические операторы
#  ветвление программ
# Операторы if - else / elif

if True:    # если выражение стоящее после if истонно - вычисляется в True
    print('Indeed, true.') # то программная логика поёдет по пути написанному после ':' в блоке if / True вычисляется в True

# Пример

if 3 > 2:
    print('3 is greater than 2') # выполнится


if 3 < 2:
    print('2 is less than 2') # не выполнится т.к. выражение вычисляется в False и следовательно в этот блок после ":" программа не зайдёт


is_admin = True
if is_admin:
    print("It's admin, look him!")


# Пример

selected_character = input()

if selected_character == 'Protos':                                      # если введенное значение пользователем равно = 'Protos'
    print('Protos is the most powerful race')                           # то вывести данное выражение
elif selected_character == 'Zerg':                                      # а если оно равно = 'Zerg'
    print('Zerg is the most weak race but it spreads like a plague')    # то вывести данное выражение
elif selected_character == 'Terrain':                                   # elif - можно ставить столько сколько есть выражений / случаев
    print('Terrain is a race balanced between Zerg and Protos')
else:                                                                   # ИНАЧЕ - во всех остальных случаях
    print('Hmm... it seems we have a new race.')                        # выполняется следующее выражение


# с помощью "if elif и else" мы можем строить любое логическое ветвление в программе проверяя все случаи которые нам известны 
# и спользовать блок "else" для обработки всех тех случаев кторые не подпадают под случаи обрабатываемые в ветках "if и elif"  





