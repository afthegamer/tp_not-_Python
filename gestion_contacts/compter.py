def compter_contacts():
    try:
        with open('contacts.txt', 'r') as fichier:
            contacts = fichier.readlines()
            print(f"Nombre de contacts : {len(contacts)}")
    except FileNotFoundError:
        print("Le fichier de contacts est introuvable.")

