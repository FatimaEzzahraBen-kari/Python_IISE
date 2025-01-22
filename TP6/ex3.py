def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("Le fichier que vous tentez d'ouvrir n'existe pas")
    finally:
        print("le fichier est terminé ")
read_file("file.txt")
