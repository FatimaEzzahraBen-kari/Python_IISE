try:
    with open("inexistant.txt","r") as fichier:
        contenue = fichier.read()
except FileNotFoundError :
    print("Le fichier que vous tentez d'ouvrir n'existe pas") 