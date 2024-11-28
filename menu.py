from gestion_contacts.ajouter import ajouter_contact
from gestion_contacts.lire import lire_contacts
from gestion_contacts.trier import trier_contacts
from gestion_contacts.compter import compter_contacts
from gestion_contacts.rechercher import rechercher_contact
from gestion_contacts.modifier import modifier_contact
from gestion_contacts.supprimer import supprimer_contact

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


if __name__ == "__main__":
    menu()
