for i in range(1, 11):  # внешний цикл по строкам
    for j in range(1, 11):  # вложенный цикл по столбцам
        mul = i * j  # TODO выровнять по ширине 3 по правому краю
        print(mul, end="")  # печатаем все столбцы в одну строку
    print()  # после обработки всех столбцов переходим на новую строку
