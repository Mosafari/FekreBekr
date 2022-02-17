import random

lockpass = {'a': '', 'b': '', 'c': '', 'd': ''}
playerguss = {'a': '', 'b': '', 'c': '', 'd': ''}
PG = ''


def Passmaker():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for key in lockpass:
        lockpass[key] = str(random.choice(num))
    return lockpass


def Playergussdecleaer():
    PG = input('Enter Your Guss : ')
    PG = list(PG.strip())
    # fixing error with 'reversed()'->Index Out of Range (for revoming item)
    for item in reversed(range(len(PG))):
        if not PG[item].isnumeric():
            PG.remove(PG[item])
    if len(PG) < 4:
        print('your guss is to short , try another')
        return Playergussdecleaer()
    elif len(PG) > 4:
        print('your guss is to long , try another')
        return Playergussdecleaer()

    else:
        i = 0
        for key in playerguss:
            playerguss[key] = PG[i]
            i += 1
        return playerguss


def Comparator(playerguss, lockpass):
    RNRP = 0  # right num in right place
    RNWP = 0  # right num in wrong place
    for key in playerguss:
        if playerguss[key] == lockpass[key]:
            RNRP += 1

        elif playerguss[key] in lockpass.values():
            RNWP += 1

    if RNRP > 0 and RNRP < 4:
        print('{} right num in right place'.format(RNRP))
    if RNRP > 0 and RNWP > 0:
        print('and')
    if RNWP > 0 and RNWP < 4:
        print('{} right num in wrong place'.format(RNWP))
    if RNRP == 4:
        lock = False
        print('You Win')
        return lock


going = True
lock = True
while going:
    lockpass = Passmaker()
    print(lockpass)
    while lock:
        playerguss = Playergussdecleaer()
        action = Comparator(playerguss, lockpass)
        if action == False:
            lock = False
    going = False
