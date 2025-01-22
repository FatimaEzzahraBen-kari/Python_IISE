def get_positive_integer():
    try:
        nbr= int(input("Entrez un entier positif : "))
        while nbr < 0 :
            nbr= int(input("Entrez un entier positif : "))
    except ValueError:
        print("Erreur! veuillez entrer un nombre valide")
    else:
        print(nbr)
        print("Bravo! Vous avez entrer un nombre valide")
get_positive_integer()
       