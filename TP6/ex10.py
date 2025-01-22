try:
    file = input("veuilez entrer un fichier : ")
    with open(file,"r") as fichier:
        contenu = fichier.read()
    print("Le contenu du fichier est : ")
    print(contenu)
    nbr= int(input("Veuillez entrer un entier : "))
    while nbr % 1 != 0:
            nbr= int(input("Veuillez entrer un entier : "))
    print("Bravo! vous avez saisi un entier valide") 
except FileNotFoundError:
     print(f"Le fichier {file} n'existe pas")
except PermissionError:
     print(f"Vous n'avez pas les droits pour lire le fichier {file}. Veuillez réessayer")
except ValueError:
    print("Erreur! veuillez entrer un nombre valide")
finally:
     print("Fin du traitement.")
    

    
