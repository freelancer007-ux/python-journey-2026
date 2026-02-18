#Creation des comptes
class Compte():
    def __init__(self, titulaire, numero, devise, solde, etat=None):
        self.__titulaire = titulaire
        self.__numero = numero
        self.devise = devise
        self.__solde = solde
        self.etat = etat if etat else Actif()

    @property
    def solde(self):
        return self.__solde
    @solde.setter
    def solde(self, valeur):
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le solde doit être un nombre")
        if valeur < 0:
            raise MontantInvalide(valeur, "le solde doit être positif !")
        self.__solde = valeur

    
    @property
    def titulaire(self):
        return self.__titulaire

    @property
    def numero(self):
        return self.__numero
 
    def verifier_actif(self): 
        if isinstance(self.etat, Inactif): 
            raise Exception("Opération impossible : compte inactif")
    
    def depot(self, montant):

        self.verifier_actif()
        
        if not isinstance (montant,(int, float)):
            raise TypeError("veuillez entrer un nombre !")
        
        if montant < 0:
            raise MontantInvalide(montant,"le montant doit etre positif !")
        
        self.solde += montant
        print(f"Depot de {montant} {self.devise} effectuer avec succes !")

    def retrait(self, montant):

        self.verifier_actif()

        if montant < 0:
            raise MontantInvalide(montant,"le montant doit etre positif !")
        
        if not isinstance (montant,(int, float)):
            raise TypeError("veuillez entrer un nombre !")
        if montant > self.solde:
            raise SoldeInsiffusant(self.solde, montant)
        
        self.solde -= montant
        print(f"Retrait de {montant} {self.devise} effectuer avec succes !")

    def __str__(self):
        return f"Compte de : {self.__titulaire} | compte N°{self.__numero} | solde : {self.__solde}"
    
    def __repr__(self):
        return f"compte N°{self.__numero}, {self.__titulaire}, {self.devise},  {self.__solde}"
class CompteEpargne(Compte):
    def __init__(self, titulaire, numero, devise, solde, taux_interet, etat=None):
        super().__init__(titulaire, numero, devise, solde, etat)
        self.__taux_interet = taux_interet   # en pourcentage, ex: 5 pour 5%

    @property
    def taux_interet(self):
        return self.__taux_interet

    def ajouter_interet(self):
        self.verifier_actif()
        """Ajoute les intérêts au solde"""
        interet = self.solde * (self.__taux_interet / 100)
        self.solde += interet
        print(f"Intérêt de {interet} {self.devise} ajouté au compte.")

    def retrait(self, montant):
        self.verifier_actif()
        """On impose un solde minimum de 100 pour un compte épargne"""
        if not isinstance(montant, (int, float)):
            raise TypeError("veuillez entrer un nombre !")
        if montant > self.solde:
            raise SoldeInsiffusant(self.solde, montant)
        if self.solde - montant < 100:
            raise Exception("Retrait refusé : solde minimum de 100 requis sur un compte épargne.")
        super().retrait(montant)

    def __str__(self):
        return (f"Compte épargne de : {self.titulaire} | "
                f"compte N°{self.numero} | solde : {self.solde} | taux d'intérêt : {self.__taux_interet}%")

class CompteJeune(Compte):
    def __init__(self, titulaire, age, numero, devise, solde, plafond, etat=None):
        if age >= 25:
            raise AgeInvalide(age)
        
        super().__init__(titulaire, numero, devise, solde, etat)
        self.__age = age
        self.__plafond = plafond

    def depot(self, montant):
        self.verifier_actif()
        if not isinstance(montant, (int, float)):
            raise TypeError("le solde doit un nombre !")
        if montant > self.__plafond:
            raise PlafonDepasse(self.__plafond,montant)
        super().depot(montant)

    def retrait(self, montant):
        self.verifier_actif()
        if not isinstance(montant, (int, float)):
            raise TypeError("le solde doit un nombre !")
        if montant > self.__plafond:
            raise PlafonDepasse(self.__plafond,montant)
        super().retrait(montant)
    

    @property
    def plafond(self):
        return self.__plafond
    def __str__(self):
        return f"Compte jeune de  : {self.titulaire} | compte N°{self.numero} | solde : {self.solde} | plafond : {self.plafond}"
    
    def __repr__(self):
        return f"compte Jeune N°{self.__numero}, {self.__titulaire}, {self.devise},  {self.__solde}"




#Gestion des Erreur
class Erreur(Exception):
    pass

class MontantInvalide(Erreur):
    def __init__(self, montant, raison):
        self.montant = montant
        self.raison = raison
        message = f"Montant invalide : {montant} | raison : {raison}"
        super().__init__(message)
class SoldeInsiffusant(Erreur):
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        
        message = (f"solde insiffusant : "
                f"votre solde est : {solde} "
                f"montant demande : {montant}")
        super().__init__(message)
class PlafonDepasse(Erreur):
    def __init__(self, plafond, montant):
        self.plafond = plafond
        self.montant = montant
        message = f"plafond depasser | plafond fixé a : {plafond} | montant demander {montant}"
        super().__init__(message)
class AgeInvalide(Erreur):
    def __init__(self, age):
        self.age = age
        message = f"votre age est : {age} | limite fixé a 25 ans !"
        super().__init__(message)
    

# Verifier Etat
class Etat():
    def __init__(self):
        pass
class Actif(Etat):
    def __init__(self):
        pass
class Inactif(Etat):
    def __init__(self):
        pass

c1 = Compte("Arafat", "9008", "XOF", 0)
c1.etat=Inactif()
try:
    c1.depot(-5)
except Exception as e:
    print(f"Erreur : {e}")
    
try:       # OK
    c1.retrait(50)
except Exception as e :
    print(f"Erreur : {e}")      # OK
print(c1)           # Affiche le solde mis à jour

c2 = CompteJeune("Toto",23,"2345","EU",500,5000)
print(c2)
print([c1])
c2.etat = Inactif()
try:
    c2.depot("j")
except Exception as e :
    print(f"Erreur : {e}")
print(c2)
try:
    c2.retrait(500)
except Exception as e:
    print(f"Erreur {e}")
# print(c2)