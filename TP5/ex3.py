#Demander les phrases à l'utilisateur
phrase1 = input("Veuillez entrer la première phrase:")
phrase2 = input("Veuillez entrer la deuxième phrase:")
phrase3 = input("Veuillez entrer la troisième phrase:")

#Ecrire les phrases dans le fichier 
with open("phrase.txt","w") as fichier:
    fichier.write(phrase1 + "\n")
    fichier.write(phrase2 + "\n")
    fichier.write(phrase3 + "\n")

#Demander si l'utilisateur veut ajouter d'autres phrases supplimentaires 
reponse = input("Voulez-vous ajouter d'autres phrases ? (oui/non) : ")

#Ajouter des phrases supplimentaires 
while reponse.lower() == "oui":
    phrase_sup = input("Entrez une phrase supplimentaire :")
    with open("phrases.txt","a") as fichier:
        fichier.write(phrase_sup + "\n")
        reponse = input("Voulez-vous ajouter d'autres phrases ? (oui/non) : ")

print("Les phrases son enregietrer avec succes dans phrase.txt")