def calculatrice():
    print("--- Calculatrice Sup'Com ---")
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    
    print(f"Somme : {num1} + {num2} = {num1 + num2}")
    print(f"Produit : {num1} * {num2} = {num1 * num2}")
    
    # Nouvelle fonctionnalité ajoutée sur notre branche !
    if num2 != 0:
        print(f"Division : {num1} / {num2} = {num1 / num2}")
    else:
        print("Erreur : Division par zéro impossible !")

if __name__ == "__main__":
    calculatrice()