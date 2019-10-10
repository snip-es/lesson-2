user_input_year = int(input('Введите год рождения Пушника: '))

if user_input_year == 1799:
    print('Верно')
    user_input_day = input('Введите день рождения Пушника: ')
    if user_input_day == ('26 мая' or '26 Мая' or '26.05'):
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')