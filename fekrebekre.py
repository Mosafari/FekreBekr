import random

lockpass = {'a': '', 'b': '', 'c': '', 'd': ''}
playerguss = {'a': '', 'b': '', 'c': '', 'd': ''}
PG = ''


def Passmaker():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for key in lockpass:
        lockpass[key] = random.choice(num)


def Playergussdecleaer(PG):
    PG = list(PG.strip())
    # fixing error with 'reversed()'->Index Out of Range (for revoming item)
    for item in reversed(range(len(PG))):
        if not PG[item].isnumeric():
            PG.remove(PG[item])
    if len(PG) < 4:
        print('your guss is to short')
    elif len(PG) > 4:
        print('your guss is to long')
    else:
        return PG


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
PG = input()
Playergussdecleaer(PG)
