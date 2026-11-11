expenses = []


def add_expense():
    description = input("Description : ")
    amount = float(input("Montant : "))
    expenses.append({"description": description, "amount": amount})
    print("Depense ajoutee !")


def show_expense():
    pass


def show_total():
    pass


def main():
    while True:
        print("\n,==== SUIVI DES DEPENSES ====")
        print("1. Ajoute une depense")
        print("2. Afficher les depense")
        print("3. Afficher le totale")
        print("4. Quitter")
        choice = input("votre choix :")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expense()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
    if __name__ == "  __main__  ":
        main()
