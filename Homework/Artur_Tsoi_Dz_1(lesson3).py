'''f1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык'''
def num_translate():
    translate_num = '' #Введите между '' число
    if translate_num == 'one':
        print('Один')
    elif translate_num == 'two':
        print('Два')
    elif translate_num == 'three':
        print('Три')
    elif translate_num == 'four':
        print('Четыре')
    elif translate_num == 'five':
        print('Пять')
    elif translate_num == 'six':
        print('Шесть')
    elif translate_num == 'seven':
        print('Семь')
    elif translate_num == 'eight':
        print('Восемь')
    elif translate_num == 'nine':
        print('Девять')
    elif translate_num == 'ten':
        print('Десять')
    else:
        print('None')
    return
print(num_translate())




