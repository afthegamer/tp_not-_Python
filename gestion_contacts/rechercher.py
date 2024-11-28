def rechercher_contact():
    nom_recherche = input("Entrez le nom ou une partie du nom du contact à rechercher : ")
    trouve = False

    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, prenom, email = contact.strip().split(', ')
                if nom_recherche.lower() in nom.lower():
                    print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
                    trouve = True

        if not trouve:
            print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

