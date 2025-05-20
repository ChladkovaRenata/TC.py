#prázdný seznam pro ukládání jednitlivých úkolů
ukoly = []

#definovat pridat_ukol
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if nazev and popis:
            ukoly.append({"nazev": nazev, "popis": popis})
            print("Úkol byl přidán.")
            break
        else:
            print("Chyba: Název i popis musí být vyplněny.")

#definovat zobrazit_ukol
def zobrazit_ukoly():
    print("\n Seznam úkolů: ")
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        for i, u in enumerate(ukoly, 1):
            print(f"{i}. {u['nazev']} - {u['popis']}")

#definovat odstranit_ukol
def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo ůkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstranit = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstranit['nazev']}' byl odstraněn.")
        else:
            print("Chyba: Neplatné číslo.")
    except:
        print("Chyba: Zadejte platné číslo.")

#definování hlavní_menu
def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Chyba: Neplatná volba. Zkuste to znovu.")

#spuštění
hlavni_menu()


    
    


