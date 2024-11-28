def lire_contacts():
    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, prenom, email = contact.strip().split(', ')
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

