# Internal_programming_01 - Внутреннее программирование
# 2018

# Имеет встроиный функционал с подробным описанием операторов

# Счётчики данных

number_block = 1
number_string = 1
activ_blok = 1
activ_string = 1

# Имена

name_program = 'Новая программа' # Название программы
name_blok = 'Новый блок' # Название блока

#

blok = 'Блок ' + str(number_block) + '. ' + name_blok
string = 'Строка ' + str(number_string) + '. '

# Списки данных

blocks = [] # Список блоков
strings = [] # Список строк
variables = {} # Словарь переменных

#

blocks.append(str(blok))
strings.append(str(string))

# Функции

def print_program():
    print(name_program)
    for _ in blocks:
        print(' ' + _)
        for _ in strings:
            print('  ' + _)

info = '\ninfo' \
       '\n     ЗАДАЧА               ОПИСАНИЕ\n' \
       '\n' \
       '     инфо            Вывод информации\n' \
       '     выход           Выход из программы\n' \
       '     печать          Вывод на экран\n' \
       '     \n' \
       '     \n' \
       '     \n' \
       '     \n' \

while 1 == 1:
    cursor = 'Блок ' + str(activ_blok) + '.Строка ' + str(activ_string)
    print('Internal_programming_01 (2018)\n'
          '\n'
          'Для  вывода  информации введите (инфо)\n'
          'Для выхода из программы введите (выход)\n')
    print_program()
    print('')
    text_input = str(input(str(cursor + '>>')))
    if text_input == 'выход':
        print('\x1b[31m \nвыход из программы\x1b[0m')
        break
    elif text_input == 'инфо':
        print(info)
    elif text_input == 'новый блок':
        number_block += 1
        blok = 'Блок ' + str(number_block) + '. ' + name_blok
        blocks.append(str(blok))
        activ_blok = number_block
    elif text_input == 'редактировать блок':
        number = input('Ведите номер блока>>')
        activ_block = int(number)
        print('activ_blok = ', activ_blok)