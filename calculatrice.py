# calculatrice.py
# Ma première calculatrice Python - Jour 1

def addition(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraction(a, b):
    """Soustrait b de a"""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b

def division(a, b):
    """Divise a par b"""
    if b == 0:
        return "Erreur : Division par zéro impossible"
    return a / b

def calculatrice():
    """Programme principal de la calculatrice"""
    print("=== CALCULATRICE PYTHON ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
    while True:
        choix = input("\nChoisissez une opération (1-5) : ")
        
        if choix == '5':
            print("Au revoir !")
            break
            
        if choix in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Premier nombre : "))
                num2 = float(input("Deuxième nombre : "))
                
                if choix == '1':
                    print(f"Résultat : {num1} + {num2} = {addition(num1, num2)}")
                elif choix == '2':
                    print(f"Résultat : {num1} - {num2} = {soustraction(num1, num2)}")
                elif choix == '3':
                    print(f"Résultat : {num1} × {num2} = {multiplication(num1, num2)}")
                elif choix == '4':
                    resultat = division(num1, num2)
                    print(f"Résultat : {num1} ÷ {num2} = {resultat}")
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides")
        else:
            print("Choix invalide !")

# Lancer le programme
if __name__ == "__main__":
    calculatrice()