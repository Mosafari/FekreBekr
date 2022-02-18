import random

lockpass = {'a': '', 'b': '', 'c': '', 'd': ''}
playerguess = {'a': '', 'b': '', 'c': '', 'd': ''}
PG = ''


def Passmaker():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for key in lockpass:
        lockpass[key] = str(random.choice(num))
    return lockpass


def Playerguessdecleaer():
    PG = input('Enter Your Guess : ')
    PG = list(PG.strip())
    # fixing error with 'reversed()'->Index Out of Range (for revoming item)
    for item in reversed(range(len(PG))):
        if not PG[item].isnumeric():
            PG.remove(PG[item])
    if len(PG) < 4:
        print('your guess is to short , try another')
        return Playerguessdecleaer()
    elif len(PG) > 4:
        print('your guess is to long , try another')
        return Playerguessdecleaer()

    else:
        i = 0
        for key in playerguess:
            playerguess[key] = PG[i]
            i += 1
        return playerguess


def Comparator(playerguess, lockpass):
    RNRP = 0  # right num in right place
    RNWP = 0  # right num in wrong place
    for key in playerguess:
        if playerguess[key] == lockpass[key]:
            RNRP += 1

        elif playerguess[key] in lockpass.values():
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
    while lock:
        playerguess = Playerguessdecleaer()
        action = Comparator(playerguess, lockpass)
        if action == False:
            lock = False
    going = input('"You Win"\nPress Enter for Exit')
