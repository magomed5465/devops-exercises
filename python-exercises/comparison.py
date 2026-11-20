#   Задание: Написать функцию проверки неравенства для целых чисел. Возможные неравенства: "<" и ">"
#   Пример входного значения: 2>5
#   Пример выходного значения: False
#   Требования к скрипту:

#   1) Название скрипта comparison.py
#   2) Название функции compare
#   3) На вход функции подается элемент типа String
#   4) Функция возвращает элемент типа Boolean
#   Примечание: цифры могут состоять из нескольких символов и иметь отрицательные значения

def compare(expression: str) -> bool:
    if '<' in expression:
        operator = '<'
        left_str, right_str = expression.split('<')
    else:
        operator = '>'
        left_str, right_str = expression.split('>')

    left_num = int(left_str)
    right_num = int(right_str)

    if operator == '<':
        return left_num < right_num
    else:
        return left_num > right_num

print(compare('3<5'))
print(compare('3<-5'))
print(compare('-3<-5'))
print(compare('-3<5'))