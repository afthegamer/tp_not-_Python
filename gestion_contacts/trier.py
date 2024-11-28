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

