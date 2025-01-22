import csv

# Ajouter des contacts
def ajouter_contacts(fichier_csv):
    nom = input("Nom :").strip()
    prenom = input("Prenom :").strip()
    telephone = input("Telephone : ").strip()

    try:
        with open(fichier_csv, mode='a', newline='', encoding='utf-8') as fichier:
            ecrivain = csv.writer(fichier)
            ecrivain.writerow([nom, prenom, telephone])
        print("Contact ajouté avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'ajout du contact : {e}")

# Afficher des contacts
def afficher_contacts(fichier_csv):
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as fichier:
            lecteur = csv.reader(fichier)
            contacts = list(lecteur)
            if not contacts:
                print("Aucun contact à afficher.")
            else:
                print("\nListe des contacts :")
                for ligne in contacts:
                    print(f"Nom : {ligne[0]}, Prenom : {ligne[1]}, Telephone : {ligne[2]}")
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
    except IOError:
        print("Erreur lors de l'affichage du fichier.")

# Rechercher un contact par nom
def rechercher_contact(fichier_csv):
    nom = input("Entrez le nom du contact à rechercher : ").strip()
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as fichier:
            lecteur = csv.reader(fichier)
            trouve = False
            for ligne in lecteur:
                if ligne[0].lower() == nom.lower():
                    print(f"Nom : {ligne[0]}, Prenom : {ligne[1]}, Telephone : {ligne[2]}")
                    trouve = True
            if not trouve:
                print("Contact non trouvé.")
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
    except IOError:
        print("Erreur lors de la recherche dans le fichier.")

# Supprimer un contact
def supprimer_contact(fichier_csv):
    nom = input("Entrez le nom du contact à supprimer : ").strip()
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as fichier:
            contacts = [ligne for ligne in csv.reader(fichier) if len(ligne) == 3]  # Ignorer les lignes mal formées

        contacts_modifies = [contact for contact in contacts if contact[0].lower() != nom.lower()]

        if len(contacts) == len(contacts_modifies):
            print("Contact non trouvé.")
        else:
            with open(fichier_csv, mode='w', newline='', encoding='utf-8') as fichier:
                writer = csv.writer(fichier)
                writer.writerows(contacts_modifies)
            print("Contact supprimé avec succès !")
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
    except IOError:
        print("Erreur lors de la suppression du contact.")


# Fonction principale
def main():
    fichier_csv = "file.csv"
    while True:
        print("\nMenu :\n1. Ajouter un contact\n2. Afficher tous les contacts\n3. Rechercher un contact\n4. Supprimer un contact\n5. Quitter")
        choix = input("Entrez votre choix : ").strip()

        if choix == "1":
            ajouter_contacts(fichier_csv)
        elif choix == "2":
            afficher_contacts(fichier_csv)
        elif choix == "3":
            rechercher_contact(fichier_csv)
        elif choix == "4":
            supprimer_contact(fichier_csv)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide ! Veuillez réessayer.")

if __name__ == "__main__":
    main()
