'''2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
'''
def num_translate_adv():
    translate_num = '' #Введите между '' число
    if translate_num == 'one':
        print('Один')
    elif translate_num == 'two':
        print('два')
    elif translate_num == 'three':
        print('три')
    elif translate_num == 'four':
        print('четыре')
    elif translate_num == 'five':
        print('пять')
    elif translate_num == 'six':
        print('шесть')
    elif translate_num == 'seven':
        print('семь')
    elif translate_num == 'eight':
        print('восемь')
    elif translate_num == 'nine':
        print('девять')
    elif translate_num == 'ten':
        print('десять')
    else:
        print('None')
    return
print(num_translate_adv())

