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

