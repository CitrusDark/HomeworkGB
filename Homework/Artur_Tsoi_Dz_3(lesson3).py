'''Написать
функцию
thesaurus(), принимающую в качестве аргументов имена сотрудников
и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие
имена, начинающиесяс
соответствующей
буквы f'''
def thesaurus(*names):
    set_names = {name.title() for name in names}
    first_letter = [name[0].upper() for name in set_names]
    result_dict = {k: list() for k in first_letter}

    for name in set_names:
        result_dict[name[0]].append(name)

    return result_dict

print(thesaurus("Райя", "Марси", 'Ракс', 'Макс'))

