def calculatrice():
    print("--- Calculatrice Sup'Com ---")
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    
    print(f"Somme : {num1} + {num2} = {num1 + num2}")
    print(f"Produit : {num1} * {num2} = {num1 * num2}")

if __name__ == "__main__":
    calculatrice()