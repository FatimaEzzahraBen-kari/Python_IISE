try:
        with open("texte.txt","r") as fichier:
                lignes = fichier.readlines()
                nb_lignes = len(lignes)
                nb_mots = sum(len(ligne.split()) for ligne in lignes)
                nb_caracteres = sum(len(ligne) for ligne in lignes)
        
                print(f"Statistiques pour le fichier texte.txt :")
                print(f"- Nombre total de lignes : {nb_lignes}")
                print(f"- Nombre total de mots : {nb_mots}")
                print(f"- Nombre total de caractères : {nb_caracteres}")

except FileNotFoundError:
        print(f"Erreur : Le fichier texte.txt n'existe pas.")
except Exception as e:
        print(f"Erreur : {e}")