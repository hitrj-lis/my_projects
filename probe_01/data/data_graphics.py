# Список данных для графика программы graphics

from simple_draw import get_point

x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
y = [20, 25, 27, 30, 28, 26, 29, 33, 40, 37, 41, 47, 55, 70, 75, 78]

data_graphic = []
data_point_list = []

if len(x) == len(y):
    for accounting in range(len(x)):
        data_point_list.append(get_point(x[accounting] + 50, (y[accounting] + 50)))
        data_graphic.append(str(x[accounting]) + ',' + str(y[accounting]))
else:
    x_1 = 50
    y_1 = 50
    data_point_list.append(get_point(x_1, y_1))
    data_graphic.append(str(x_1) + ',' + str(y_1))
    x_1 = 100
    y_1 = 100
    data_point_list.append(get_point(x_1, y_1))
    data_graphic.append(str(x_1) + ',' + str(y_1))