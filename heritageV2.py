#code pour heritage avancé
#jour 4 encapsulation + property + heritage

class Compte:
    def __init__(self,numero, solde: float, titulaire, plafond: float):
        self.numero = numero
        self._solde = solde
        self.titulaire = titulaire
        self.plafond = plafond

    @property
    def get_solde(self):
        return self._solde
        
    @get_solde.setter
    def set_solde(self, n_solde):
        if n_solde < 0:
            print("impossible solde negatif !")
        else:
            self._solde = n_solde
            print(f"votre nouveau solde est {self._solde} ")

    def limite(self):
        print(f"la limite du compte N°{self.numero} est {self.plafond}")

    def retrait(self, montant):
        if self._solde > montant:
            self._solde -= montant
            print(f"retrait effectuer avec succes de la somme de {montant}")
            print(f"votre nouveau solde est {self._solde}")
        else:
            print("Desolé : votre solde est insifusant !")

    def depot(self, montant):
        if montant > 0 and self.plafond < montant:
            print(f"Depot de {montant} est effectuer avec succes sur le compte N°{self.numero}")

    def get_info(self):
        print(f"le compte est le N° {self.numero} , titulaire : {self.titulaire} solde : {self._solde}")


class CompteEpargne(Compte):
    def __init__(self, numero, solde, titulaire, plafond, type_compte):
        super().__init__(numero, solde, titulaire, plafond)
        self.type_compte = type_compte
        self.__epargne_totale = 0

    def epargne(self, montant):
        if self._solde > montant:
            self._solde -= montant
            self.__epargne_totale += montant
            print(f"vous venez d'epargner la somme de {montant} de votre compte : N°{self.numero}")

    def mon_epargne(self):
        print(f"Mon epargne total est de {self.__epargne_totale}")

C1 = Compte("8907",12000,"Arafat",10000000)
C2 = CompteEpargne("8934",23000,"Toto",2000000,"Epargne")

C1.get_info()
C1.limite()
C1.retrait(8000)
C1.get_solde


C2.get_info()
C2.get_solde
C2.set_solde = 20000
C2.get_info()
C2.epargne(10000)
C2.mon_epargne()
C2.limite()
C2.retrait(8000)
C2.get_solde