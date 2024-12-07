class Animal:

    def faire_du_bruit(self):
        return "Les animaux font des bruits"

class Chat(Animal):
    def faire_du_bruit(self):
        return "Le chat miaule"
class Chien(Animal):

    def faire_du_bruit(self):
        return "Le chien aboie"

chat1=Chat()
print(chat1.faire_du_bruit())

chien1=Chien()
print(chien1.faire_du_bruit())