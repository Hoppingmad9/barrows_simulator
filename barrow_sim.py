import random
random.seed()
from collections import Counter

def linzaRoll(linzaKilled):
    if (linzaKilled):
        dropRoll = random.randint(1,192)
        if (dropRoll == 1):
            linzaDrop = random.randint(33,37)
            return (linzaDrop)
    return 0

def brothersRoll(brothersKilled):
    dropRoll = random.randint(1,max(450-(58*len(brothersKilled)),73))
    if (dropRoll == 1):
        drops = [[1,2,3,4,5,6],
        [7,8,9,10],
        [11,12,13,14],
        [15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28],
        [29,30,31,32]]
        possibleDrops = []
        for key, val in enumerate(brothersKilled):
            if (val):
                possibleDrops += drops[key]
        brothersDrop = random.randint(1,len(possibleDrops))
        return possibleDrops[brothersDrop-1]
    return 0

def barrowsRoll(brothersKilled,linzaKilled):
    drops = []
    for i in range(min(sum(brothersKilled)+1,7)):
        drop = linzaRoll(linzaKilled)
        if (drop == 0):
            drop = brothersRoll(brothersKilled)
        if (drop != 0):
            drops.append(drop)
    return drops

def fullSetCheck(drops):
    indexes = [6,10,14,18,24,28,32]
    dropsSeperated = []
    prev = 0
    for index in indexes:
        dropsSeperated.append(drops[prev:index])
        prev = index
    dropsSeperated.append(drops[indexes[-1]:])
    #print(dropsSeperated)
    return sum([True if 0 not in i else False for i in dropsSeperated])

##drops = [0] * 37
##chests = 400
##for i in range(chests):
##    drop = barrowsRoll([1,1,1,1,1,1,1], False)
##    for i in drop:
##        drops[i-1] += 1
###print(drops)
##if (fullSetCheck(drops)):
##    print("Full set")
##else:
##    print("No set")
##print(chests/float(sum(drops)))

allChests = [None] * 6
##average number of runs for a set
if (True):
    runs = 10000
    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            drop = barrowsRoll([1,1,1,1,1,1,1], False)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        #print(j)
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[0] = chestsForSet
    print("killing all brothers: "+str(sum(chestsForSet)/runs))

    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            brothersKilledList = [0,0,1,0,0,0,0]
            mazeBrother = random.randint(0,6)
            brothersKilledList[mazeBrother] = 1
            drop = barrowsRoll(brothersKilledList, False)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[1] = chestsForSet
    print("killing dharok and maze: "+str(sum(chestsForSet)/runs))

    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            brothersKilledList = [0,0,0,0,0,0,0]
            brothersKillOrder = [2,3,5,6,1,0,4]
            mazeBrother = random.randint(1,7)
            for k in range(mazeBrother):
                brothersKilledList[brothersKillOrder[k]] = 1
            drop = barrowsRoll(brothersKilledList, False)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[2] = chestsForSet
    print("killing until tunnel; melee first: "+str(sum(chestsForSet)/runs))
            
    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            drop = barrowsRoll([1,1,1,1,1,1,1], True)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[3] = chestsForSet
    print("killing all brothers + linza: "+str(sum(chestsForSet)/runs))

    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            brothersKilledList = [0,0,1,0,0,0,0]
            mazeBrother = random.randint(0,6)
            brothersKilledList[mazeBrother] = 1
            drop = barrowsRoll(brothersKilledList, True)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[4] = chestsForSet
    print("killing dharok and maze + linza: "+str(sum(chestsForSet)/runs))

    chestsForSet = []
    for j in range(runs):
        drops = [0] * 37
        chests = 0
        while (fullSetCheck(drops) == 0):
            brothersKilledList = [0,0,0,0,0,0,0]
            brothersKillOrder = [2,3,5,6,1,0,4]
            mazeBrother = random.randint(1,7)
            for k in range(mazeBrother):
                brothersKilledList[brothersKillOrder[k]] = 1
            drop = barrowsRoll(brothersKilledList, True)
            chests += 1
            for i in drop:
                drops[i-1] += 1
        chestsForSet.append(chests)
    #print(chestsForSet)
    allChests[5] = chestsForSet
    print("killing until tunnel; melee first + linza: "+str(sum(chestsForSet)/runs))




counts = [None] * 6
for key, value in enumerate(allChests):
    counts[key] = dict(Counter(value))

print(counts)
    
