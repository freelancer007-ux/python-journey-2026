class Espece:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")


class Humain(Espece):
    def __init__(self, nom, age, type):
        super().__init__(nom, age)
        self.type = type

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans. - {self.type}")
    
class Animal(Espece):
    def __init__(self, nom, age, type):
        super().__init__(nom, age)
        self.type = type

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans. - {self.type}")
    

homme1 = Humain("arafat",34,"Homme")
animal1 = Animal("miki",3, "Chat")
espece1 = Espece("Alien",500)

homme1.se_presenter()
animal1.se_presenter()
espece1.se_presenter()