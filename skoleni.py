# Importování potřebných knihoven
import csv
import datetime

# Nastavení názvu souboru pro ukládání dat
file_name = "pojistne_udalosti.csv"

# Definování funkce pro přidání nové události
def add_event():
    # Získání informací od uživatele
    datum = input("Zadejte datum události (formát DD.MM.RRRR): ")
    popis = input("Zadejte popis události: ")
    # Vytvoření záznamu
    zaznam = [datum, popis]
    # Otevření souboru pro přidání nového záznamu
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(zaznam)
    print("Událost byla úspěšně přidána.")

# Definování funkce pro zobrazení všech událostí
def show_events():
    # Otevření souboru a načtení dat
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # Vypsání každého záznamu
        for row in reader:
            print(f"{row[0]}: {row[1]}")

# Hlavní smyčka programu
while True:
    # Zobrazení nabídky možností
    print("\nCo chcete udělat?")
    print("1 - Přidat novou událost")
    print("2 - Zobrazit všechny události")
    print("3 - Konec programu")
    volba = input("Zadejte číslo volby: ")
    # Zpracování volby uživatele
    if volba == "1":
        add_event()
    elif volba == "2":
        show_events()
    elif volba == "3":
        break
    else:
        print("Neplatná volba.")