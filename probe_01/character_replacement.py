# character_replacement_01 - Программа для замены символов языкавых раскладок клавиатуры(pec./eng.)
# 2018

from data.data_cr import *

while 1 == 1:
    convert_text = ''
    print('character_replacement_01 (2018)')
    print('\nДля  вывода  информации  введите (info==info)\n'
          'Для выхода из программы введите (exit==exit)\n\n', leng, '\n')
    text = str(input('Введите текст:\n'))
    if text == 'exit==exit':
        break
    elif text == 'info==info':
        print(info)
    elif text == 'rus>>eng':
        leng = 'rus>>eng'
    elif text == 'eng>>rus':
        leng = 'eng>>rus'
    else:
        if leng == 'eng>>rus':
            for i in text:
                if i in eng_rus:
                    convert_text += eng_rus[i]
                else:
                    convert_text += i
        elif leng == 'rus>>eng':
            for i in text:
                if i in rus_eng:
                    convert_text += rus_eng[i]
                else:
                    convert_text += i
        print(convert_text)