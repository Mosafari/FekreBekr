import random

lockpass = {'a': '', 'b': '', 'c': '', 'd': ''}
playerguss = {'a': '', 'b': '', 'c': '', 'd': ''}


def Passmaker():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for key in lockpass:
        lockpass[key] = random.choice(num)


def Comparator():
    RNRP = 0  # right num in right place
    RNWP = 0  # right num in wrong place
    for key in playerguss:
        if playerguss[key] == lockpass[key]:
            RNRP += 1
            continue

        elif playerguss[key] in lockpass:
            RNWP += 1
            continue

        else:
            pass
    if RNRP > 0:
        print('{} right num in right place'.format(RNRP), end=" ")
    elif RNRP > 0 and RNWP > 0:
        print('and', end=" ")
    elif RNWP > 0:
        print('{} right num in wrong place'.format(RNWP))


Passmaker()
