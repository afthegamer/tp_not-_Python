def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    prenom = input("Entrez le prénom du contact : ")
    email = input("Entrez l'adresse mail du contact : ")

    with open('contacts.txt', 'a') as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

