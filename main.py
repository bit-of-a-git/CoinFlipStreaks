import random

experiments = 10000
flips = 100
total = experiments * flips
streak = 0
numofstreaks = 0

HorT = ["H", "T"]

for i in range(experiments):
    coins = []
    for j in range(flips):
        coins.append(random.choice(HorT))
        if j == 0:
            pass
        else:
            if coins[j] == coins[j - 1]:
                streak += 1
            else:
                streak = 0
        # If two coins in a row are the same then streak = 1, therefore for six streak will equal 5
        if streak == 5:
            numofstreaks += 1

print('Chance of streak: %s%%' % (numofstreaks * 100 / total))
