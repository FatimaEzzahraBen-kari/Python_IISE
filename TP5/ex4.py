import csv
with open("contacts.csv","r") as fichier:
    lecteur = csv.DictReader(fichier) # DictReader lit le fichier CSV et retourne chaque ligne sous forme de dictionnnaire
    for ligne in lecteur:
        print(f"Nom : {ligne['Nom']}, Age : {ligne['Age']}, Ville : {ligne['Ville']}")
    # lecteur = csv.reader(fichier)
    # for ligne in lecteur:
    #     print(ligne)