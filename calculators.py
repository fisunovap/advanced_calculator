from math import sqrt


def solver_x4(a, b, c):
    """ Решает квадратное уравнение и возвращает результат в форматированной строке """
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        if x1>=0:
            x_1 = sqrt(x1)
            x_2 = (0-sqrt(x1))
        else:
            x_1 = "sqrt(t1)<0"
            x_2 = "sqrt(t1)<0"
        x2 = (-b - sqrt(D)) / (2 * a)
        if x2>=0:
            x_3 = sqrt(x2)
            x_4 = (0 - sqrt(x2))
        else:
            x_3 = "sqrt(t2)<0"
            x_4 = "sqrt(t2)<0"
        text = "Дискриминант = %s \nX1 = %s \nX2 = %s \nX3 = %s\nX4 = %s " % (D, x_1, x_2, x_3, x_4)
    else:
        text = "Дискриминант = %s \nНет корней в поле действительных чисел" % D
    return text