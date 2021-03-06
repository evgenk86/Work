# ДЗ - 5. Card sum

# Дан список карт. 
#  current_hand = [2, 3, 4, 10, 'Q', 5]
#  В общем и целом, список может содержать следующие значения 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A'.
# у каждой карты есть свой "вес"
# 2, 3, 4, 5, 6 весят +1
# 7, 8, 9 весят 0
# 10, 'J', 'Q', 'K', 'A' весят -1

# Задача. Имея список карт (current_hand) посчитать их общий "вес"

current_hand = [2, 3, 4, 10, 'Q', 5]

# Создадим словарь, в качестве ключей будут значения этих карт, а в качестве значений будет их "вес" {2:1} т.e. у 2 вес 1 и т.д.
cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}

# чтобы посчитать вес карт на любой руке, нужно взять вес каждой карты на руке
# преобразовать один список в другой список
# список карт превратить в список "весов" этих карт
# и все полученные значения передать в функцию "sum" чтобы их просуммировать

cards_sum = sum([cards[x] for x in current_hand]) 

# заводим интератор х который идет по current_hand, т.е. в х содержится текущая карта. в левой части мы можем обратиться по словарю по ключу х
# саму карту использовать ввиде ключа - cards[x] будет возвращать вес текущей карты в переменную current_hand

print(cards_sum)









