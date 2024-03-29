# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

reform = 1582
big_leap_year = 400
small_leap_year = 4
not_leap_year = 100

year = int(input("Введите год: "))

if year < reform:
    if not year % small_leap_year:
        result = "Год является високосным (по Юлианскому календарю)."
    else:
        result = "Год не является високосным (по Юлианскому календарю)."
elif year % not_leap_year and not year % small_leap_year \
    or year % big_leap_year == 0:
    result = "Год является високосным (по Григорианскому календарю)."
else:
    result = "Год не является високосным (по Григорианскому календарю)."
print(result)