#CompteSecurise.py
#compte securisé jour 3 aplication de private et property

class CompteSecurise:
    def __init__(self, titulaire,numero: int,solde: float,devise):
        self.__titulaire=titulaire
        self.__numero=numero
        self.__solde=solde
        self.devise=devise

    def get_solde(self):
        return self.__solde
    
    def set_solde(self, setsolde: float):
        if setsolde < 0:
            print("solde negatif")
        else:
            print(f"nouveau solde : {self.__solde} {self.devise}")
        
    def depot(self, montant):
        if montant < 0:
            print("impossible montant negatif !!")
        else :
            self.__solde += montant
            print(f"depot de {montant} {self.devise} effectuer avec succes !!")
            print(f"votre solde est {self.__solde}\n")


    def retrait(self, montant):
        if montant > self.__solde or montant < 0:
            print("action impossible ressayer ....")
        else:
            self.__solde -= montant
            print(f"Succes : retrait de {montant} {self.devise} du compte {self.__numero}")
            print(f"votre solde est {self.__solde}\n")

    
compte1 = CompteSecurise("arafat",9898,5000,"XOF")
compte1.get_solde()
compte1.retrait(3000)
compte1.depot(4000)