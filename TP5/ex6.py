import os
# Rennomage du fichier
try:
    os.rename("phrases.txt","ancienne_phrases.txt")
    print("Le fichier a été renommer avec succes")

except FileNotFoundError:
    print("Le fichier à renommer est introuvable!")
except IOError:
    print("Erreur lors du renommage du fichier!")   
# Suppression du fichier renommé
nom_fichier = "ancienne_phrases.txt"
try:
    os.remove(nom_fichier)
    print(f"Fichier {nom_fichier} supprimé")  
except FileNotFoundError:
    print("Le fichier à supprimer est introuvable!")
except IOError:
    print("Erreur lors du suppression du fichier!") 
