class Compte:
    def __init__(self, id_compte, titulaire, solde, devise):
        self.__id_compte = id_compte
        self.__titulaire = titulaire
        self.__solde = solde
        self.__devise = devise

        if self.__solde < 0:
            raise ValueError("le solde doit etre positif")

    def depot(self, montant):
        if montant <= 100:
            raise ValueError("erreur minimum requis 100 !")
        
        self.__solde += montant
        print(f"vous venez de faire un depot de {montant} {self.devise} sur le compte {self.__id_compte}")
        return self.__solde

    def retrait(self, montant):
        if montant <= 100:
            raise ValueError("erreur minimum requis 100 !")
        
        if montant > self.__solde:
            raise ValueError("desolé solde insiffusant!")
        
        self.__solde -= montant
        print(f"vous venez de faire un retrait de {montant} {self.devise} sur le compte {self.__id_compte}")
        return self.__solde

    @property
    def id_compte(self):
        return self.__id_compte
    
    @property
    def titulaire(self):
        return self.__titulaire
    
    @property
    def solde(self):
        return self.__solde
    
    @property
    def devise(self):
        return self.__devise

    def __str__(self):
        return f"compte N°{self.__id_compte} / titulaire : {self.__titulaire} : solde {self.__solde}"
    
    def __repr__(self):
        return f"compte( {self.__id_compte}: {self.__titulaire} {self.__solde})"
    
class CompteEpargne(Compte):
    def __init__(self, id_compte, titulaire, solde, devise, taux_interets, total_epargne):
        super().__init__(id_compte, titulaire, solde, devise)
        self.__taux_interets = taux_interets
        self.__total_epargne = total_epargne

    @property
    def taux_interts(self):
        return self.__taux_interets
    @property
    def total_epargne(self):
        return self.__total_epargne
    
    def calculer_interets(self):
        return self.solde * (self.__taux_interets / 100)
    
    def interets(self):
        interets = self.calculer_interets()
        self.depot(interets)
        print(f"interets de {interets} {self.devise} apliqué")

    def __str__(self):
        base = super().__str__()
        return f"{base} Taux : {self.__taux_interets}% | interets : {self.calculer_interets()}"
    
    def __repr__(self):
        return f"CompteEpargne ({self.id_compte}: {self.titulaire} {self.solde} {self.taux_interts})"
    
    def epargner(self, montant):
        if montant < 0 and self.__solde > montant:
            raise ValueError("le montant ne doit pas depasser ni etre nul")
        self.__solde -= montant
        self.__total_epargne += montant
        print(f"vous venez d'epargner {montant} {self.devise} du compte N°{self.__id_compte}")
        return self.__solde
    

class CompteJeune(Compte):
    def __init__(self, id_compte, titulaire, age, solde, devise):
        if age >= 25:
            raise ValueError("Compte reservés aux moins de 25 ans")
        
        super().__init__(id_compte, titulaire, solde, devise)
        self.__age = age
        self.__plafond_de_retrait = 10000

    @property
    def age(self):
        return self.__age
    
    def retrait(self, montant):
        if montant > self.__plafond_de_retrait:
            raise ValueError ("Action non autorisé")
        return super().retrait(montant)
    def __str__(self):
        base = super().__str__()
        return f"{base} : {self.__plafond_de_retrait} le titulaire a {self.__age} ans !"

    def __repr__(self):
        return f"CompteJeune : {self.id_compte}: {self.titulaire} {self.solde} "
    

c1 = Compte("2345","Arafat",10000,"XOF")
c2 = CompteEpargne("2342","Fatima", 200000, "EU",5.5,0)
c3 = CompteJeune("5675","Ali", 20, 30000,"USD")
c4 = Compte("9034","Moussa", 150000,"NH")

print("-"*60)
print()
print([c1, c2, c3, c4])
print("-"*60)
    
c1.depot(50000)
c1.retrait(20000)
print("-"*60)
print()
c2.depot(100000)
c2.calculer_interets()
print("-"*60) 
print()
c3.depot(10000)
c3.retrait(5000)

print("-"*60)
print(c1)
print()
print(c2)
print()
print(c3)
print("-"*60)
print()
print([c1, c2, c3, c4])