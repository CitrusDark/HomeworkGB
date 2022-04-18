
def thesaurus_adv(*namesandfamily):
    set_names = {name.title() for name in namesandfamily}
    set_family = {family.title() for family in namesandfamily}
    first_letter = [name[0].upper() for name in set_names]
    second_letter = [family[0].upper() for family in set_family]
    result_dict = {key: list() for key in first_letter}
    result_dict2 = {key: list() for key in second_letter}

    for name in set_names:
        result_dict[name[0]].append(name)
    for family in set_family:
        result_dict2[family[0]].append(family)
    return first_letter , second_letter


print(thesaurus_adv("Райя Петров", "Марси Калиновский", "Макс Рокосовский", "Марк Машининиснвоый"))
'''Так как почти срок сдачи ДЗ,прошу объяснить как сделать доп задание это с фамиилиями hz
'''
