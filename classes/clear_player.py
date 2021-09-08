import pickle
import sys
from Player import Bot

sys.path.append(".\classes")

bot_names = 'riri', 'fifi', 'lili', 'pipi'
bot_values = [
    [1, 1, 1],
    [10, 10, 0.5],
    [100, 100, 0.2],
    [1000, 1000, 0.1]
]
bot_prices = [[100, 1000], [5000, 50000], [100000, 500000], [10000000, 8000000]]

sauvegarde = {
    'argent': 0,
    'uranium': 0,
    'bots': [Bot(bot_names[i], bot_values[i], bot_prices[i]) for i in range(len(bot_names))],
    'val_argent': 1,
    'val_uranium': 1,
    'mult': 0
}

with open('../resources/save/player', 'wb') as fichier:
    a = pickle.Pickler(fichier)
    a.dump(sauvegarde)

contenus = ""
with open('../resources/save/lock.txt', 'w') as fichier:
    for p in range(0, 24):
        contenus += str(int(True)) + "\n"
    fichier.write(contenus)

contenus = ""
with open('../resources/save/init.txt', 'w') as fichier:
    for p in range(0, 2):
        contenus += "on\n"
    fichier.write(contenus)
