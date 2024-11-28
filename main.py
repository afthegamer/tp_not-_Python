def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    prenom = input("Entrez le prénom du contact : ")
    email = input("Entrez l'adresse mail du contact : ")

    with open('contacts.txt', 'a') as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

def lire_contacts():
    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, prenom, email = contact.strip().split(', ')
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

def trier_contacts():
    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            contacts.sort(key=lambda x: x.split(', ')[0])  # Trie par nom

        with open('contacts.txt', 'w') as fichier:
            fichier.writelines(contacts)

        print("Les contacts ont été triés par ordre alphabétique.")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

def compter_contacts():
    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            print(f"Nombre de contacts : {len(contacts)}")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

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

def modifier_contact():
    nom_recherche = input("Entrez le nom ou une partie du nom du contact à modifier : ")
    contacts_modifies = []
    contacts_a_modifier = []

    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, prenom, email = contact.strip().split(', ')
                if nom_recherche.lower() in nom.lower():
                    contacts_a_modifier.append(contact)
                else:
                    contacts_modifies.append(contact)

        if contacts_a_modifier:
            print("Contacts trouvés :")
            for index, contact in enumerate(contacts_a_modifier):
                nom, prenom, email = contact.strip().split(', ')
                print(f"{index + 1}. Nom : {nom}, Prénom : {prenom}, Email : {email}")

            choix = int(input("Entrez le numéro du contact à modifier : "))
            if 1 <= choix <= len(contacts_a_modifier):
                contact = contacts_a_modifier[choix - 1]
                nom, prenom, email = contact.strip().split(', ')
                print("Tapez 1 pour modifier le nom, 2 pour modifier le prénom, 3 pour modifier l'email")
                choix_modification = int(input("Entrez le numéro de l'information à modifier : "))
                if choix_modification == 1:
                    nouveau_nom = input("Entrez le nouveau nom : ")
                    contacts_a_modifier[choix - 1] = f"{nouveau_nom}, {prenom}, {email}\n"
                    print("Nom modifié avec succès.")
                elif choix_modification == 2:
                    nouveau_prenom = input("Entrez le nouveau prénom : ")
                    contacts_a_modifier[choix - 1] = f"{nom}, {nouveau_prenom}, {email}\n"
                    print("Prénom modifié avec succès.")
                elif choix_modification == 3:
                    nouveau_email = input("Entrez le nouvel email : ")
                    contacts_a_modifier[choix - 1] = f"{nom}, {prenom}, {nouveau_email}\n"
                    print("Email modifié avec succès.")
                else:
                    print("Choix invalide.")
            else:
                print("Choix invalide.")
        else:
            print("Aucun contact trouvé avec ce nom.")

        with open('contacts.txt', 'w') as fichier:
            fichier.writelines(contacts_modifies + contacts_a_modifier)
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

def supprimer_contact():
    nom_recherche = input("Entrez le nom ou une partie du nom du contact à supprimer : ")
    contacts_modifies = []
    contacts_a_supprimer = []

    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, prenom, email = contact.strip().split(', ')
                if nom_recherche.lower() in nom.lower():
                    contacts_a_supprimer.append(contact)
                else:
                    contacts_modifies.append(contact)

        if contacts_a_supprimer:
            print("Contacts trouvés :")
            for index, contact in enumerate(contacts_a_supprimer):
                nom, prenom, email = contact.strip().split(', ')
                print(f"{index + 1}. Nom : {nom}, Prénom : {prenom}, Email : {email}")

            choix = int(input("Entrez le numéro du contact à supprimer : "))
            if 1 <= choix <= len(contacts_a_supprimer):
                contacts_a_supprimer.pop(choix - 1)
                print("Contact supprimé avec succès.")
            else:
                print("Choix invalide.")
        else:
            print("Aucun contact trouvé avec ce nom.")

        with open('contacts.txt', 'w') as fichier:
            fichier.writelines(contacts_modifies + contacts_a_supprimer)
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

def menu():
    while True:
        print("\nMenu de gestion des contacts :")
        print("1. Ajouter un contact")
        print("2. Lire les contacts")
        print("3. Trier les contacts")
        print("4. Compter les contacts")
        print("5. Rechercher un contact")
        print("6. Modifier un contact")
        print("7. Supprimer un contact")
        print("8. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            lire_contacts()
        elif choix == '3':
            trier_contacts()
        elif choix == '4':
            compter_contacts()
        elif choix == '5':
            rechercher_contact()
        elif choix == '6':
            modifier_contact()
        elif choix == '7':
            supprimer_contact()
        elif choix == '8':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


menu()
