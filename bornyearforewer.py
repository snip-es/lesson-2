#Работает до тех пор пока не будет введен правильный год

while True:
    try:
        user_input_year = int(input('Введите год рождения Пушника: '))
        if user_input_year == 1799:
            print('Верно')
            break
        elif user_input_year != 1799:
            print('Неверный год рождения')
        else:
            raise ValueError
    except ValueError:
        print("Введите год цифрами пожалуйста")