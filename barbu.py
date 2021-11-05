#!/usr/bin/env python3

# jezu's barbus :p

# Pas besoin d'expliquer les regles, ne pas les connaitre serait de tres
# mauvais gout ^^. Pour ce script, vous aurez besoin de python3 ( qui l'eut cru ) et
# de la librairie random. Vous lancez le script, et voilacht ^^ lol

# License:
# http://www.opensource.org/licenses/gpl-3.0.html

# Importation du tirage au hasard
from random import randrange

# Table des regles
u = [
    "1 gorgee a distribuer",
    "2 gorgees a distribuer",
    "3 gorgees a distribuer",
    "4 gorgees a distribuer",
    "5 gorgees a distribuer",
    "6 gorgees a distribuer",
    "J'ai deja fait",
    "Je n'ai jamais fait",
    "Dans ma valise",
    "Les marques",
    "Maitre des pouces",
    "Mot le plus long",
    "Nouvelle regle",
]

# Demarrage
print("C'est partis pour un ch'ti barbuch! Come on :p")
input()

while 1:
    t = [0] * 52

    for i in range(0, 52):
        k = 1
        while k:
            j = randrange(0, 52)

            # Verification que
            if not (j in t) or j == 0:
                t[i] = j
                k = 0
                print("Carte " + str(i + 1) + " = " + str(u[j % 13]))
                input()

    print("Vous etes tous bourres :D Et c'est repartis :p\n")
