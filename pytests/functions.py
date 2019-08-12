def divide_by_two(a):
    return a / 2


def divide_by(a, b):
    return a / b


def sum_all(list_el):
    if type(list_el) != list:
        raise ValueError('It suppose to be a list')
    if len(list_el) == 0:
        raise ValueError('The list have to has at least 1 element')
    acc = 0
    for el in list_el:
        acc += el
    return acc