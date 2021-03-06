# Цикл WHILE / CONTINUE / BREAK

# цикл "while" похож на цикл "for" и может быть заменен циклом "for", но в некоторых случаях цикл "while" - "проще" и "короче"

# цикл "while" - переводится как "пока нечто" и вычисляется в "True"
# т.е. после "while" - должно стоять некое выражение вычисляемое в boolean

x = 0
while x < 3:                            # до тех пор пока x меньше 3 повторять следующее
    print(f'x equals {x}')              # выводить строчку "х равняется х"
    x+=1                                # и прибавляем каждый раз к "х" 1(единицу)
    
    # этот код выполняется до тех пор пока x меньше 3х

        # x equals 0 - х сперва равнялся 0 (по условию)
        # x equals 1 - затем к 0 мы прибавили 1, получили 1
        # x equals 2 - затем к 1 мы прибавили еще 1, получили 2
        #            - затем к 2 мы прибавили 1, получили 3
        #            - цикл проверил условие, где 3 не меньше 3х и следовательно в "print(f'x equals {x}')" он не зашел, вышел из цикла и тем самым завершил свою работу

x = 0
while x < 3:                            # до тех пор пока x меньше 3 повторять следующее
    print(f'x equals {x}')              # выводить строчку "х равняется х"
    x+=1                                # и прибавляем каждый раз к "х" 1(единицу)
else:
    print('Condition is not met')       # условие не выполнено, т.к. мы зашли в ветку "else"


# break используется для преждевременного выхода из цикла

# continue - для перехода к следующей итерации и не доходить до окончания кода блока исполняемого в цикле

# pass - как заполнитель чтобы ничего не делать

vals = [1,2,3,4,5,6,7,8,9]          # создадим список значений

sum = 0                             # создадим переменную в которой будем накапливать сумму
for v in vals:                      # и пройдемся циклом for по нашим значениям
    if v % 2 ==0:                   # и если наше значение делиться на 2 без остатка, является чётным числом, 
        continue                    # то мы ничего не делаем, а переходим к след. итерации
    else:                           # а вот если нечетное
        sum += v                    # прибавляем к сумме текущее значение
    if sum > 10:                    # а когда сумма становится больше 10
        break                       # то хотим выйти из цикла

print(sum)                          # 16

# когда мы только вошли в цикл, то переменной v была присвоена 1, и в данном случае мы попадаем в "else" 
# - проверяем sum > 10 не выполняется и в break мы тоже не попадаем
# в v записывается 2 - это четное число - попадаем в contunue и нижний блок "else" не срабатывает
# в v записывается 3 - это нечетное число и в данном случае мы попадаем в "else" т.д.
# и когда в sum записывается 16 выполняется "sum > 10" срабатывает break - выход из цикла
# и выводится результат


# 1.
#     sum = 0
#     v = 1 / else
#     0 + 1 = 1
# 2.
#     sum = 1
#     v = 2 
#     2 % 2 = 0 / без остатка / continue
# 3.
#     sum = 1
#     v = 3 / else
#     sum = 1 + 2 = 4
# 4.
#     sum = 4
#     v= 4
#     4 % 2 = 0 / без остатка / continue
# 5.
#     sum = 4
#     v = 5 / else
#     sum = 4 + 5 = 9
# 6.
#     sum = 9
#     v = 6
#     6 % 2 = 0 / без остатка / continue
# 7.
#     sum = 9
#     v = 7 
#     sum = 9 + 7 = 16
    
#     sum > 10 - break

# ни 8 ни 9 в v не будет записана
# 9ка уже добавлена в sum не будет

# использование "pass"

for v in vals:
    pass

# если мы создали цикл, не знаем пока что в него писать, но не хотим удалять его можно "закрыть" его командой "pass", т.о. он просто пропустится







