import os
import datetime as dt
import math

# Afficher le repertoire courant
courant = os.getcwd()
print(f"Le repertoire courant est : {courant}")
# Afficher la date et l'heure actuelle
date_actuelle =dt.datetime.now()
print(f"La date actuelle est {date_actuelle}")
# Afficher la racine carré d'un nombre
nbr = int(input("Entrer un nombre : "))
racine = math.sqrt(nbr)
print(f"La racine de {nbr} est {racine}")