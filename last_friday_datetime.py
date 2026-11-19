#   Задание: Необходимо вывести дату последней пятницы указанного месяца
#   Пример входного значения: 05/2022
#   Пример выходного значения: 27.05.2022

#   Требования к скрипту:

#   1) Название скрипта last_friday_datetime.py
#   2) Название функции get_last_friday
#   3) На вход функции подается элемент типа String
#   4) Функция возвращает элемент типа String

import calendar
from datetime import date
from datetime import timedelta


def get_last_friday(date_str: str) -> str:
    month_str, year_str = date_str.split('/')
    month = int(month_str)
    year = int(year_str)

    last_day_of_month = calendar.monthrange(year, month)[1]
    current_date = date(year, month, last_day_of_month)

    while current_date.weekday() != 4:
        current_date -= timedelta(days=1)

    return current_date.strftime("%d.%m.%Y")


print(f"05/2022 -> {get_last_friday('05/2022')}")  # Ожидается 27.05.2022