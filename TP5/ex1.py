with open("exemple.txt","r") as fichier:
    #contenue = fichier.read()
    lignes = fichier.readlines()
    l=1
    for ligne in lignes:
        print(l,ligne)
        l+=1
