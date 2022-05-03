import random

l = list()
l.append('images/green.png')
l.append('images/red.png')
l.append('images/purple.png')
l.append('images/blue.png')
l.append('images/brown.png')
l.append('images/bomb.png')
l.append('images/wall.png')

def getRndImg():
    #print(l)
    r = random.randint(0, 1000)
    if(r <= 950):
        return r % 5
    else:
        r = random.randint(0, 100)
        if(r <= 60):
            return 5
        else:
            return 6

def getImg(i):
    return l[i]