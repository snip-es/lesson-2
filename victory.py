while True:
    try:
        user_input_year1 = int(input('Введите год рождения Ленина: '))
        if user_input_year == 1799:
            user_input_day = input('Введите день рожденья Пушкина: ')
            while user_input_day != ('26 мая' or '26 Мая' or '26.05'):
                user_input_day = input('Введите день рожденья Пушкина: ')
                print('Верно')
            break
        elif user_input_year != 1799:
            print('Неверный год рождения')
        else:
            raise ValueError
    except ValueError:
        print("Введите год цифрами пожалуйста")