import logging

def log_error(message):
    
    logging.basicConfig(
        filename='error.log', 
        level=logging.ERROR, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        log_error(f"Le fichier '{filename}' est introuvable.")
        print("Le fichier que vous tentez d'ouvrir n'existe pas")
    finally:
        print("Le fichier est terminé.")

read_file("fille.txt")
