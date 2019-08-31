# -*- coding: utf-8 -*-

# Scripts_Of_System v. 1.0
# (c) 2019

from data import *

settings_file = 'C:\\Users\\Пчеловек\\PycharmProjects\\my_projects\\SOS\\settings.sos'
default_settings = {'color': 'red', 'hello': 'hello'}

settings = reed_settings(settings_file)
execute_settings(settings)

while True:
    input_array = input(f'{cursor}')
    print()
    for function in FUNC_ARRAY:
        if input_array == function.__class__.__name__.lower():
            function.__call__()
            print()
