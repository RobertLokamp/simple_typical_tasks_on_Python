# Игра "Угадайка чисел"
# Программа генерирует случайное число в заданном пользователем диапазоне и просит пользователя угадать это число за
# определённое число попыток, которые рассчитываются с помощью бинарного поиска.

# Порядок работы:
# 1. Пользователь вводит диапазон, в котором должно быть загадываемое число
# 2. Программа загадывает число в заданном диапазоне и определяет количество попыток, за которое нужно угадать это число
# 3. Пользователь отгадывает (вводит числа), пока не угадает или не закончатся попытки. Если введённое число больше или
    # меньше загаданного, то программа сообщает об этом
# 4. Если пользователь угадал или закончились попытки, то пользователь может выбрать: хочет он сыграть ещё раз или нет


from random import randint

# Функции
def is_valid_l_border(l_border):
    """
    Функция, которая проверяет, что левая граница диапазона задана правильно (число больше нуля)
    :param l_border: значение левой границы
    :return: True or False
    """
    if l_border.isdigit() == True and int(l_border) >= 0:
        return True
    else:
        return False

def is_valid_r_border(l_border, r_border):
    """
    Функция, которая проверяет, что правая граница диапазона задана правильно (число, большее, чем левая граница)
    :param l_border: значение левой границы
    :param r_border: значение правой границы
    :return: True or False
    """
    if r_border.isdigit() == True and int(r_border) > int(l_border):
        return True
    else:
        return False

def quantity_of_attempts(l_border, r_border):
    """
    Функция, которая рассчитывает количество попыток в соответствии с заданным диапазоном (согласно принципу
    бинарного поиска)
    :param l_border: значение левой границы
    :param r_border: значение правой границы
    :return: количество попыток
    """
    counter = 0
    while int(l_border) != int(r_border):
        r_border = (int(r_border) + int(l_border)) // 2
        counter += 1
    return counter

def quantity_of_attempts_txt(counter):
    """
    Функция, которая возвращает количество попыток вместе с верным окончанием слова "попытка"
    :param counter: количество попыток
    :return: количество попыток с верным окончанием слова "попытка"
    """
    if (counter > 20 and counter % 10 == 1) or counter == 1:
        return str(counter) + ' попытка'
    if (counter > 20 and (counter % 10 == 2 or counter % 10 == 3 or counter % 10 == 4)) or (
            counter == 2 or counter == 3 or counter == 4):
        return str(counter) + ' попытки'
    else:
        return str(counter) + ' попыток'

def is_valid_your_num(l_border, r_border, your_num):
    """
    Функция, которая проверяет, что пользователь ввёл допустимое значение (число внутри заданных границ)
    :param l_border: значение левой границы
    :param r_border: значение правой границы
    :param your_num: число, которое ввёл пользователь
    :return: True or False
    """
    if int(l_border) <= int(your_num) <= int(r_border):
        return True
    else:
        return False

# Начало программы
print('Добро пожаловать в числовую угадайку')


# Начало основного цикла программы
while True:
    print('Задай мне диапазон чисел, в котором должно быть загадываемое число.\n'
          'Рекомендую задавать небольшую разницу между граничными числами (не более 100).\n'
          'Иначе отгадывать будем очень долго :) ')


    # Задание границ диапазона
    l_border = input('Задай левую границу (число). Это должно быть положительное целое число: ')
    while not is_valid_l_border(l_border):
        l_border = input('Неверно задана левая граница. Это должно быть положительное целое число: ')
    r_border = input(
        'Задай правую границу (число). Это должно быть положительное целое число, большее, чем левая граница: ')
    while not is_valid_r_border(l_border, r_border):
        r_border = input(
            'Неверно задана правая граница. Это должно быть положительное целое число, большее, чем левая граница: ')


    # Загадывание числа и расчёт количества попыток
    secret_num = randint(int(l_border), int(r_border))  # Загадывание случайного числа в заданном диапазоне
    print('Я загадала число от ' + str(l_border) + ' до ' + str(r_border) + ', попробуй его угадать! \n'
    'Что-то мне подсказывает, что, при данном диапазоне, заданное число можно угадать за ' +
          quantity_of_attempts_txt(quantity_of_attempts(l_border, r_border)) + '. \n'
    'Значит у тебя ' + quantity_of_attempts_txt(quantity_of_attempts(l_border, r_border)) + ' :)\n'
    'Ну, начнём!')

    attempts = quantity_of_attempts(l_border, r_border)  # Расчет количества попыток в соответствии с диапазоном

    # Начало цикла угадывания числа
    while True:
        if attempts == 0:  # Если попытки закончились, то выходим из цикла угадывания
            print('Извини, но твои попытки закончились. Ты проиграл.')
            break

        your_num = int(input('Введи число: '))  # Ввод пользователем числа

        if is_valid_your_num(l_border, r_border, your_num):  # Если пользователь ввёл валидное число
            if secret_num < your_num:  # Если введённое число больше загаданного, то сообщаем, отнимаем попытку и продолжаем
                attempts -= 1
                print('Моё число меньше, попробуй ещё раз. Осталось ' + quantity_of_attempts_txt(attempts))
                continue
            elif secret_num > your_num:  # Если введённое число меньше загаданного, то сообщаем, отнимаем попытку и продолжаем
                attempts -= 1
                print('Моё число больше, попробуй ещё раз. Осталось ' + quantity_of_attempts_txt(attempts))
                continue
            else:  # Если введённое число совпадает с загаданным (угадали), то говорим сколько попыток потратили и выходим
                taken_attempts = quantity_of_attempts(l_border, r_border) - attempts + 1
                print('Ты угадал(а), поздравляю! Тебе потребовалось ' + quantity_of_attempts_txt(taken_attempts))
                break
        else:  # Если пользователь ввёл невалидное число
            print('Нет-нет, тебе надо ввести ЧИСЛО, которое находится МЕЖДУ ' + str(l_border) + ' и ' + str(r_border))
            continue


    # Конец основного цикла, предложение сыграть ещё раз
    game_again = input('Спасибо, что играл в числовую угадайку. Сыграем ещё? (д(y)/н(n)): ')  # Предложение сыграть ещё
    answers_for_game_again = ['д', 'y', 'н', 'n']  # Список с валидными вариантами ответов на предложение сыграть ещё
    while game_again not in answers_for_game_again:  # Если вводим значения не из списка с валидными вариантами ответов
        game_again = input('Если хочешь играть ещё, введи: д или y. Если не хочешь, то н или n: ')
    if game_again.lower() == 'д' or game_again.lower() == 'y':  # Если согласились играть ещё, то возвращаемся в начало основного цикла
        print('ОК, играем!')
        continue
    elif game_again.lower() == 'н' or game_again.lower() == 'n':  # Если не согласились играть ещё, то выходим из основного цикла
        print('До новых встреч!')
        break
