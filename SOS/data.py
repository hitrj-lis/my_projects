# -*- coding: utf-8 -*-

import os
import platform
import sys
import time
import shutil
from colorama import init, Fore

init()

cursor = ' >>: '

colors = {'red': Fore.RED, 'black': Fore.BLACK, 'blue': Fore.BLUE, 'cyan': Fore.CYAN, 'green': Fore.GREEN,
          'white': Fore.WHITE, 'magenta': Fore.MAGENTA, 'yellow': Fore.YELLOW, 'lred': Fore.LIGHTRED_EX,
          'lblack': Fore.LIGHTBLACK_EX, 'lblue': Fore.LIGHTBLUE_EX, 'lcyan': Fore.LIGHTCYAN_EX,
          'lgreen': Fore.LIGHTGREEN_EX, 'lwhite': Fore.LIGHTWHITE_EX, 'lmagenta': Fore.LIGHTMAGENTA_EX,
          'lyellow': Fore.LIGHTYELLOW_EX}


def reed_settings(settings_file):
    settings = {}
    with open(settings_file, 'r') as file:
        for setting in file:
            setting = setting[:-1]
            setting = setting.split(':')
            settings[setting[0]] = setting[1]
    return settings


def execute_settings(settings):
    print(settings['hello'])
    print(colors[settings['color']])


class Arrange:
    """ Copy files """
    def __call__(self,):
        copy_directory = input(f'copy directory{cursor}')
        if os.path.exists(copy_directory):
            new_directory = input(f'new directory{cursor}')
            if os.path.exists(new_directory):
                print('processing...')
                for dirpath, dirnames, filenames in os.walk(copy_directory):
                    for file in filenames:
                        full_file_path = os.path.join(dirpath, file)
                        secs = os.path.getmtime(full_file_path)
                        data = time.gmtime(secs)
                        year = str(data[0])
                        if data[1] <= 9:
                            month = f'0{data[1]}'
                        else:
                            month = str(data[1])
                        new_full_file_path = os.path.join(new_directory, year, month)
                        if not os.path.exists(new_full_file_path):
                            os.makedirs(new_full_file_path)
                        shutil.copy2(src=full_file_path, dst=new_full_file_path)
            else:
                print('new_directory is not true')
        else:
            print('copy_directory is not true')

    def __str__(self):
        return 'copy files'


class Print:
    """ print """
    def __call__(self):
        input_atr = input(f'print{cursor}')
        print(f'{input_atr}')

    def __str__(self):
        return 'print'


class Operators:
    """ list of all operators """
    def __call__(self):
        for operator in FUNC_ARRAY:
            print(f'{operator.__class__.__name__.lower():.<20}{operator}')

    def __str__(self):
        return 'list of all operators'


class Clear:
    """ clear screen """
    def __call__(self):
        clear = lambda: os.system('cls')
        clear()

    def __str__(self):
        return 'clear screen'


class Environ:
    """ get the value of the environment variable """
    def __call__(self):
        info = os.environ
        for arg, text in info.items():
            print(f'{arg:.<35}{text}')

    def __str__(self):
        return 'get the value of the environment variable'


class OS:
    """ OS platform """
    def __call__(self):
        print(platform.system())

    def __str__(self):
        return 'OS platform'


class Color:
    """ text color """
    def __call__(self):
        input_color = input(f'color{cursor}')
        if input_color == '?':
            for color in colors:
                print(color)
        else:
            print(colors[f'{input_color}'])

    def __str__(self):
        return 'text color'


class Exit:
    """ Exit of program """
    def __call__(self):
        exit = lambda: sys.exit()
        exit()

    def __str__(self):
        return 'exit'


FUNC_ARRAY = [Arrange(), Clear(), Color(),  Environ(), Exit(), Operators(), OS(), Print()]
