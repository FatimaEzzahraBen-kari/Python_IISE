phrase1 = input("Veuillez entrer la première phrase:")
phrase2 = input("Veuillez entrer la deuxième phrase:")
phrase3 = input("Veuillez entrer la troisième phrase:")

with open("phrases.txt","w") as fichier:
    fichier.write(phrase1 + "\n")
    fichier.write(phrase2 + "\n")
    fichier.write(phrase3 + "\n")

print("Les phrases son enregietrer avec succes dans phrase.txt")