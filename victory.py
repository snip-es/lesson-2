# Джон Д. Кармак II 1970
# Джон Роме́ро 1967
# Ньюэлл Гейб 1962
# Клифф Блезински 1975
# Питер Молиньё 1959
y = True
while y == True:
    cout_true = 0
    cout_false = 0
    cout_true1 = 0
    cout_true2 = 0
    cout_true3 = 0
    cout_true4 = 0
    cout_true5 = 0
    cout_false1 = 0
    cout_false2 = 0
    cout_false3 = 0
    cout_false4 = 0
    cout_false5 = 0
    x = True
    try:
        user_input_year1 = int(input('Введите год рождения Джона Кармака II: '))
        user_input_year2 = int(input('Введите год рождения Джона Роме́ро: '))
        user_input_year3 = int(input('Введите год рождения Гейба Ньюэлла: '))
        user_input_year4 = int(input('Введите год рождения Клиффа Блезински: '))
        user_input_year5 = int(input('Введите год рождения Питера Молиньё: '))
        if (user_input_year1 == 1970) and (user_input_year2 == 1967) and (user_input_year3 == 1962) and (
                user_input_year4 == 1975) and (user_input_year5 == 1959):
            print('Все верно')
        elif (user_input_year1 != 1970) or (user_input_year2 != 1967) or (user_input_year3 != 1962) or (
                user_input_year4 != 1975) or (user_input_year5 != 1959):
            print('Вы где-то ошиблись...')
            print('')
            if user_input_year1 == 1970:
                cout_true1 = 1
            else:
                cout_false1 = 1
                print('Год родженья Джона Кармака II не верный')
            if user_input_year2 == 1967:
                cout_true2 = 1
            else:
                cout_false2 = 1
                print('Год родженья Джона Роме́ро не верный')
            if user_input_year3 == 1962:
                cout_true3 = 1
            else:
                cout_false3 = 1
                print('Год родженья Гейба Ньюэлла не верный')
            if user_input_year4 == 1975:
                cout_true4 = 1
            else:
                cout_false4 = 1
                print('Год родженья Клиффа Блезински не верный')
            if user_input_year5 == 1959:
                cout_true5 = 1
            else:
                cout_false5 = 1
                print('Год родженья Питера Молиньё не верный')
        else:
            raise ValueError
    except ValueError:
        print("Сбой. Вводите год цифрами пожалуйста!")
    cout_true = cout_true1 + cout_true2 + cout_true3 + cout_true4 + cout_true5
    cout_false = cout_false1 + cout_false2 + cout_false3 + cout_false4 + cout_false5
    pros_true = ((cout_true) * 100) / (5)
    pros_false = ((cout_false) * 100) / (5)
    print('')
    print('Кол-во правильных ответов', cout_true)
    print('Кол-во неправильных ответов', cout_false)
    print('Процент правильных ответов', pros_true)
    print('Процент неправильных ответов', pros_false)
    print('')
    while x == True:
        try:
            user_input_answer = str(input('Вы хотите попробовать снова? Введите да или нет: '))
            if user_input_answer == 'нет':
                print('выхожу...')
                y = False
                break
            elif user_input_answer == 'да':
                print('играем снова!')
                x = False
            else:
                raise ValueError
        except ValueError:
            print("Введите да или нет буквами")
