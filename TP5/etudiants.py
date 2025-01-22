import json
info = {
    "Nom": "Kawtar",
    "Age": 15,
    "Note": 16
}
with open('etudiants.json','w') as fichier:
    json.dump(info, fichier, indent=4)

with open('etudiants.json','r') as fichier:
    info =json.load(fichier)
    print(info)