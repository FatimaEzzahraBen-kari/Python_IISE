import shutil

# copie le fichier
source1 = "journal.txt"
destination1 = "journal_copie.txt"

try: 
    shutil.copy(source1,destination1)
    print(f"Fichier copiée de {source1} vers {destination1}")
except FileNotFoundError:
    print("Le fichier source est introuvable!")
except IOError:
    print("Erreur lors de la copie du fichier!") 

# Deplacer le fichier
source2 = "journal_copie.txt"
destination2 = "archives"
try: 
    shutil.move(source2,destination2)
    print(f"Fichier déplacée de {source2} vers {destination2}")
except FileNotFoundError:
    print("Le fichier source est introuvable!")
except IOError:
    print("Erreur lors du déplacement du fichier!") 