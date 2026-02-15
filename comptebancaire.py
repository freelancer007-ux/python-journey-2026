#comptebancaire.py
#compte bancaire jour 2

class Comptebancaire:
    def __init__(self,typec,plafond,titulaire,solde: float,devise):
        self.typec=typec
        self.plafond=plafond
        self.titulaire=titulaire
        self.solde=solde
        self.devise=devise

    def depot(self,somme: float):
        self.solde += somme
        print("depot effectuer avec succes !!")

    def retrait(self,somme: float):
        if self.solde <= 0:
            print("retait impossible compte vide ")
        elif somme > self.solde:
            print("votre solde est insiffusant")
        else:
            solde_restant=self.solde - somme
            print(f"felecitation vous venez de retirer {somme} {self.devise} de votre compte solde est {solde_restant}")

comptebancaire1 = Comptebancaire("epargne","1000000","client1",20000,"XOF")
comptebancaire1.depot(10000)
comptebancaire1.retrait(500000)
comptebancaire1.retrait(5000)
comptebancaire1.retrait(4000)