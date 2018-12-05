# graphics_01 (2018)   Программа прстроения графиков

import simple_draw as sd

# Параметры по умолчанию:

check = 'truth'
name_line_x = 'x'
name_line_y = 'y'

point_list = []
resolution = {}
data = []

# Внесение в список параметров по умолчанию:

def in_data():
    x_1 = 50
    y_1 = 50
    point_list.append(sd.get_point(x_1, y_1))
    data.append(str(x_1) + ',' + str(y_1))
    x_1 = 100
    y_1 = 100
    point_list.append(sd.get_point(x_1, y_1))
    data.append(str(x_1) + ',' + str(y_1))

resolution['x'] = 1200
resolution['y'] = 600

sd.resolution = (resolution['x'], resolution['y'])
in_data()

# Информационные данные:

info = '\ninfo' \
       '\n     ЗАДАЧА            ОПИСАНИЕ\n' \
       '\n' \
       '     инфо.............Вывод информации\n' \
       '     выход............Выход из программы\n' \
       '     данные...........Вывод списка данных точек графика\n' \
       '     новые............Ввод новых данных(удаляет старые данные)\n' \
       '     добавить.........Добавляет новые данные в конец списка данных\n' \
       '     вставить.........Добавляет новые данные в определённое место списка\n' \
       '     удалить..........Удаляет весь список данных(Заменяя его списком по умолчанию)\n' \
       '     импорт...........Импортировать список данных из модуля: data_graphics\n' \
       '     старт............Запуск графика\n' \

# Функции:

def graphics(point_list):

    sd.line(start_point=sd.get_point(50, 50), end_point=sd.get_point(50, 500))
    sd.line(start_point=sd.get_point(50, 50), end_point=sd.get_point(1100, 50))
    sd.lines(point_list=point_list)
    sd.sleep(10)

# Программа:

while check == 'truth':
    print('\ngraphics_01 (2018)\n'
          '\n'
          'Для  вывода  информации введите (инфо)\n'
          'Для выхода из программы введите (выход)\n')
    print()
    text = input('>>: ')
    if text == 'инфо':
        print(info)
    elif text == 'выход':
        check = 'false'
        break
    elif text == 'данные':
        print(data)
    elif text == 'новые':
        point_list.clear()
        data.clear()
        for _ in range(2):
            x = input('x=')
            y = input('y=')
            point_list.append(sd.get_point(int(x)+50, int(y)+50))
            data.append(str(x) + ',' + str(y))
    elif text == 'добавить':
        x = input('x=')
        y = input('y=')
        point_list.append(sd.get_point(int(x)+50, int(y)+50))
        data.append(str(x) + ',' + str(y))
    elif text == 'вставить':
        x = input('x=')
        y = input('y=')
        insert = input('положение в списке: ')
        point_list.insert(int(insert)-1, (sd.get_point(int(x)+50, int(y)+50)))
        data.insert(int(insert)-1, (str(x) + ',' + str(y)))
    elif text == 'удалить':
        delete = input('всё / номер в списке')
        if delete == 'всё':
            in_data()
        elif len(point_list) < 3:
            print('Минимальное колличество данных!')
        else:
            int_delete = int(delete)
            point_list.pop(int_delete - 1)
            data.pop(int_delete - 1)
    elif text == 'импорт':
        from data_graphics import data_graphic, data_point_list
        point_list.clear()
        data.clear()
        point_list = data_point_list
        data = data_graphic
    elif text == 'старт':
        graphics(point_list)
    else:
        print('некоректный ввод')
