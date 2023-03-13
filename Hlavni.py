from Pojisteni import Pojisteni
from PojisteniManager import PojisteniManager

def main():
    pojisteni_manager = PojisteniManager()

    while True:
        print("\nCo chcete udělat?")
        print("1 - Vytvořit nového pojištěného")
        print("2 - Zobrazit seznam pojištěných")
        print("3 - Vyhledat pojištěného podle jména a příjmení")
        print("4 - Konec programu")
        volba = input("Zadejte číslo volby: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            while True:
                vek = input("Zadejte věk: ")
                if not vek.isdigit():
                    print("Chybný vstup, zadejte prosím číslo.")
                    continue
                break
            telefon = input("Zadejte telefonní číslo: ")
            pojisteni = Pojisteni(jmeno, prijmeni, vek, telefon)
            pojisteni_manager.pridej_pojisteneho(pojisteni)
            print("Pojištěný byl úspěšně přidán.")

        elif volba == "2":
            print(pojisteni_manager)

        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            pojisteni = pojisteni_manager.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteni:
                print(pojisteni)
            else:
                print("Pojištěný s tímto jménem a příjmením nebyl nalezen.")

        elif volba == "4":
            print("Děkujeme, pěkný den")
            break

main()