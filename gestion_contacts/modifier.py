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

