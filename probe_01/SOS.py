# Scripts_Of_System v. 1.0
# (c) 2019

import os
import sys
import platform
from colorama import init, Fore

init()


class ScriptData:

    def __init__(self):
        self.script_data = {'int': 0, 'string': '', 'object': None}
        self.script = ''

    def write(self, write):
        self.write = write

    def split(self, string):
        string_split = string.split(';')
        check_string = None
        if 'print' in string or 'string' in string:
            if len(string_split) > 1:
                print('Операторы "print" и "string" должны быть в отдельной строке')
            else:
                check_string = []
                for _ in string_split:
                    check_string.append(_)
        else:
            if string == '':
                pass
            else:
                check_string = []
                for _ in string_split:
                    check_string.append(_)
        return check_string


#---DATA_TEXT---#

info = '\n      ОПЕРАТОР                 ОПИСАНИЕ\n' \
       '\n' \
       '     info.....................Вывод списка информирующих операторов\n' \
       '     operator[Enter]..........Вывод информации по оператору\n' \
       '         name>>:[name]            [cancel] - отмена\n' \
       '     operators................Вывод списка всех операторов\n' \
       '     #info....................Вывод списка информаторов ошибки ввода\n' \
       '     #?.......................Вывод указанного информатора\n' \
       '         #>>:#№                  [cancel] - отмена\n' \
       '     \n'

operators_info = '\n     ОПЕРАТОР              ОПИСАНИЕ\n' \
                 '\n' \
                 '     color.................Изменить цвет текста\n' \
                 '         color>>:[color]       [cancel] - отмена\n' \
                 '     clear.................Очистить экран\n' \
                 '     close.................Выйти\n' \
                 '     dir n.................Создать новую папку\n' \
                 '         new>>:[name]          [cancel] - отмена\n' \
                 '     dir p[Enter]..........Перейти по пути в текущей директории\n' \
                 '         path>>:[path]         [cancel] - отмена\n' \
                 '     dir r.................Прочитать текущую директорию\n' \
                 '     path r[Enter].........Прочитать директорию указанного пути\n' \
                 '         path>>:[path]         [cancel] - отмена\n' \
                 '     open..................Открыть папку текущего пути\n' \
                 '     start p[Enter]........Запустить файл (открыть папку) указанного пути\n' \
                 '         path>>:[path]         [cancel] - отмена\n' \
                 '     \n' \
                 '     \n' \
                 '     \n' \
                 '     \n' \
                 '     \n'


#---FUNCTION---#

#-sistem-#

def sistem_script(input_script):
    script = ScriptData()
    string = script.split(string=input_script)
    return string

def sistem_cls():
    clear = lambda: os.system('cls')
    clear()

#-sos-#

def sos_print():
    print()


#---DATA---#


back_address = 'D:\MY_SCRIPTS'

address = back_address

blocked_path = '*<>?/+|:"'

colors = {'red': Fore.RED, 'black': Fore.BLACK, 'blue': Fore.BLUE, 'cyan': Fore.CYAN, 'green': Fore.GREEN,
          'white': Fore.WHITE, 'magenta': Fore.MAGENTA, 'yellow': Fore.YELLOW, 'lred': Fore.LIGHTRED_EX,
          'lblack': Fore.LIGHTBLACK_EX, 'lblue': Fore.LIGHTBLUE_EX, 'lcyan': Fore.LIGHTCYAN_EX,
          'lgreen': Fore.LIGHTGREEN_EX, 'lwhite': Fore.LIGHTWHITE_EX, 'lmagenta': Fore.LIGHTMAGENTA_EX,
          'lyellow': Fore.LIGHTYELLOW_EX}

informators = {'#1': 'Недопустимые символы директории', '#2': 'Неверный адрес директории', '#3': '', '#4': '', '#5': '',
               '#6': '', '#7': '', '#8': '', '#9': '', '#10': '', '#11': '', '#12': '', '#13': '', '#14': '', '#15': '',
               '#16': '', '#17': '', '#18': '', '#19': '', '#20': ''}

functions = {'print': sos_print()}


#---MAIN---#


while True:
    input_user = input(f'{address}>>: ')

    if input_user == 'script':
        program = [{'title': 'TITLE'}]
        while True:
            print(program)
            print(program[0]['title'])
            integer = '0123456789'
            for string in program:
                for check1 in integer:
                    for check2 in integer:
                        check = check1 + check2
                        for arg, kwarg in string.items():
                            if arg in check:
                                print(f'arg-{arg} check-{check}')
                                index = program.index(string)
                                print(f'{arg} {kwarg}')
            input_script = input('SCRIPT>>: ')
            if input_script[0:1] in integer and input_script[1:2] in integer:
                append = {input_script[0:2]:input_script[2:]}
                program.append(append)
            else:
                print('int NOK')
            sistem_cls()

    elif input_user == 'info':
        print(info)

    elif input_user == 'operators':
        print(operators_info)

    elif input_user == '#info':
        for arg, kwarg in informators.items():
            print(arg + '.....' + kwarg)

    elif input_user == '#?':
        input_user_2 = input('\t#>>: ')
        if input_user_2 == 'cancel':
            break
        elif input_user_2 in informators:
            print(informators[input_user_2])

    elif input_user == 'operator':
        while True:
            input_user_2 = input(f'\tname>>: ')
            if input_user_2 == 'cancel':
                break
            elif input_user_2 == 'color':
                for arg in colors:
                    print(f'\t\t{arg}')
                break

    elif input_user == 'os':
        print(platform.system())

    elif input_user == 'color':
        control = True
        while control:
            input_user_2 = input('\tcolor>>: ')
            for arg, kwarg in colors.items():
                if input_user_2 == arg:
                    print(colors[f'{input_user_2}'])
                    control = False
                    break
            if control:
                print('not corrected color\n')

    elif input_user == 'dir p':
        while True:
            input_user_2 = input(f'\tpath>>: ')
            if input_user_2 == 'cancel':
                break
            check_address = address + input_user_2
            if os.access(check_address, os.F_OK):
                back_address = address
                address = check_address
                print()
                break
            else:
                print('not corrected directory\n')

    elif input_user == 'dir r':
        len_dir = 0
        len_files = 0
        for dirpath, dirnames, filenames in os.walk(address):
            for dir_reed in dirnames:
                print(f'\t(DIR)....{dir_reed}')
                len_dir += 1
            for file in filenames:
                print(f'\t(FILE)...{file}')
                len_files += 1
            print(f'DIR({len_dir})FILES({len_files})\n')
            break

    elif input_user == 'dir n':
        input_user_2 = input(f'\tnew>>: ')
        while True:
            if input_user_2 == 'cancel':
                break
            address += '\\' + input_user_2
            os.mkdir(address, 777)
            print()
            break
        else:
            print('not corrected path\n')

    elif input_user == 'path r':
        input_user_2 = input(f'\tpath>>: ')
        while True:
            if input_user_2 == 'cancel':
                break
            if os.access(input_user_2, os.F_OK):
                back_address = address
                address = input_user_2
                len_dir = 0
                len_files = 0
                for dirpath, dirnames, filenames in os.walk(address):
                    for dir_reed in dirnames:
                        print(f'\t(DIR)....{dir_reed}')
                        len_dir += 1
                    for file in filenames:
                        print(f'\t(FILE)...{file}')
                        len_files += 1
                    print(f'DIR({len_dir})FILES({len_files})\n')
                    break
            else:
                print('not corrected path\n')

    elif input_user == 'open':
        if os.access(address, os.F_OK):
            os.startfile(address)
            print()
        else:
            print('not corrected path\n')

    elif input_user == 'start p':
        input_user_2 = input(f'\tpath>>: ')
        while True:
            if input_user_2 == 'cancel':
                break
            if os.path.isdir():
                back_address = address
                address = input_user_2
                os.startfile(address)
                print()
            else:
                print('not corrected path\n')

    elif input_user == 'back':
        address = back_address

    elif input_user == 'clear':
        sistem_cls()

    elif input_user == 'close':
        break



    elif input_user == 'test':
        aa = dict(os.environ)
        for bb in aa.items():
            print(f'{bb[0]}_____{bb[1]}')
        print()



    else:
        if len(input_user) >= 3:
            if input_user[1] == ':':
                if input_user[2] == '\\':
                    control_blocked_path = True
                    for check in input_user[3:]:
                        if check in blocked_path:
                            control_blocked_path = False
                            print('unknown path or operator #1}\n')
                            break
                    if control_blocked_path:
                        address_split = input_user.split('\\')
                        check_address = input_user[:3]
                        for check in address_split[1:]:
                            if check != '':
                                check_address += check + '\\'
                        if os.path.isdir(check_address):
                            back_address = address
                            address = check_address.upper()
                        else:
                            print('unknown path or operator #2\n')
                else:
                    print('unknown path or operator #3\n')
            else:
                print('unknown path or operator #4\n')
        else:
            print('unknown path or operator #5\n')
