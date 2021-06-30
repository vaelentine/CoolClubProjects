from random import randint


def get_random_3d6_roll():
    value = 0
    for i in range(3):
        value += randint(1, 6)
    return value


def get_attribute_modifier(attribute):
    if not isinstance(attribute, int):
        raise TypeError('Invalid argument, must be int between 3 and 18')
    if attribute == 3:
        return -2
    elif 4 <= attribute <= 7:
        return -1
    elif 8 <= attribute <= 13:
        return 0
    elif 14 <= attribute <= 17:
        return 1
    elif attribute == 18:
        return 2
    else:
        raise ValueError('Invalid argument, int must be between 3 and 18')
