def get_znak(x):
    if x[0] in '+-':
        return x[0]

list_time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list_time):
    znak = get_znak(list_time[i])
    if list_time[i].isdigit() or (znak and list_time[i][1:].isdigit()):
        if znak:
            list_time[i] = znak + list_time[i][1:].zfill(2)
        else:
            list_time[i] = list_time[i].zfill(2)

        list_time.insert(i, '"')
        list_time.insert(i + 2, '"')
        i += 2

    i += 1

print(list_time)

'''2. Дан список:
 ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']'''