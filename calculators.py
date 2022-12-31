from math import sqrt


def solver_x4(a, b, c):
    """ Решает квадратное уравнение и возвращает результат в форматированной строке """
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        if x1 >= 0:
            x_1 = sqrt(x1)
            x_2 = (0 - sqrt(x1))
        else:
            x_1 = "sqrt(t1)<0"
            x_2 = "sqrt(t1)<0"
        x2 = (-b - sqrt(D)) / (2 * a)
        if x2 >= 0:
            x_3 = sqrt(x2)
            x_4 = (0 - sqrt(x2))
        else:
            x_3 = "sqrt(t2)<0"
            x_4 = "sqrt(t2)<0"
        text = "Дискриминант = %s \nX1 = %s \nX2 = %s \nX3 = %s\nX4 = %s " % (D, x_1, x_2, x_3, x_4)
    else:
        text = "Дискриминант = %s \nНет корней в поле действительных чисел" % D
    return text


def solver_x2(a, b, c):
    """ Решает квадратное уравнение и возвращает результат в форматированной строке """
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = "Дискриминант = %s \nX1 = %s \nX2 = %s \n" % (D, x1, x2)
    else:
        text = "Дискриминант = %s \nНет корней в поле действительных чисел" % D
    return text


def to_new_system(n: str, old_system: int, new_system: int) -> str or bool:
    """
    Перевод в систему счисления с основанием от 2 до 35
    :param n: Число для перевода
    :param old_system: Старая система счисления
    :param new_system: Новая система счисления
    :return: Число в новой системе счисления
    """
    if new_system >= 36:
        raise ValueError
    n_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    int_10 = int(n, old_system)
    result = ""
    while int_10 > 0:
        result = n_dict[int_10 % new_system] + result
        int_10 //= new_system

    return result
