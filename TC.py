#hlavni_menu()
#pridat_ukol()
#zobrazit_ukoly()
#odstranit_ukol()

ukoly = []

#definovat hlavní menu, krok 1 - zda se zobrazí hlavné menu a u volby "1" se spustí funkce pridat_ukol 
#krok 2 - když se zadá volab např. "11", tak jestli to dá chybnou hlášku
def hlavni_menu():
    while True:
        print("1 - Přidat úkol")
        print("2 - Zobrazit úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec")
        volba = input("Zadej volbu: ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba.")

#definovat pridat_ukol, krok 1 - pokus se zvolí volba "1", tak zda se úkol přidá + přidá se nový název úkolu,
#krok 2- pokud uživatel zadá přidat_ukol, ale nevyplní nic do návzu úkolu, tak program odmítne prázdný vstup (zobrazí se chyba), program čeká na vyplnění.
def pridat_ukol():
    nazev = input("Zadej název úkolu: ").strip()
    if nazev:
        ukoly.append(nazev)
        print(f"Úkol '{nazev}' byl přidán.")
    else:
        print("Chyba: název úkolu nemůže být prázdný.")

#definovat zobrazit_ukol, krok 1 - po volbě "2" se zobrazí prázdný seznam a informuje, že nejsou žádné úkoly
#krok 2 - zobrazí se existující úkol a vypíše je.
def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
    else:
        print("\n Seznam úkolů: ")
        i = 1
        for ukol in ukoly:
            print(f"{i}. {ukol}")
            i += 1

#definovat odstranit_ukol, krok 1 - odtsranění úkolu, zda se úspěšné odstranil
#krok 2- objeví se hlavnáí menu 
def odstranit_ukol():
    zobrazit_ukoly()
    if len(ukoly) == 0:
        return
    
    try:
        cislo = int(input("Zadejte číslo ůkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstranit = ukoly.pop(cislo - 1)
            print(f"Úkol {odstranit} byl odstraněn.")
        else:
            print("chyba: Neplatné číslo.")
    except ValueError:
        print("Chyba: Zadej platné číslo.")




#spuštění
if __name__ == "__main__":
    hlavni_menu()


exit()
            


    
    


