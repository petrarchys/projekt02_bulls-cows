"""
projekt_2.py: druhý projekt do Engeto Online Datový analytik s Pythonem

author: Petr Sychra
email: psychra@seznam.cz
discord: petrsychra
"""

import random

def vypis_pozdrav()-> None:
    """
    Vypíše pozdrav uživateli a úvodní text
    """
    print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")

def vygeneruj_nahodne_cislo()->int:
    """
    Vygeneruje náhodné 4místné číslo od 1000 do 9999.
    """
    return random.randint(1000, 9999)

def zkontroluj_unikatnost_cisla(cislo: int)->bool:
    """
    Zkontroluje celé číslo, zda se v něm neopakují číslovky.

    Příklad:
    >>> zkontroluj_unikatnost_cisla(1234) -> true
    >>> zkontroluj_unikatnost_cisla(1122) -> false
    """
    return len(str(cislo)) == len(set(str(cislo)))

def vrat_tajne_cislo()-> int:
    """
    Vrátí 4místné celé číslo bez opakování číslovek. 
    """
    while True:
        tajne_cislo = vygeneruj_nahodne_cislo()
        if zkontroluj_unikatnost_cisla(tajne_cislo):
            return tajne_cislo

def over_vstup_uzivatele(vstup: str)-> bool:
    """
    Ověří vstup uživatele. Délka 4 čísla, nezačínat nulou.  
    """
    if len(vstup) != 4 or not vstup.isdigit() or vstup[0] == "0" or not zkontroluj_unikatnost_cisla(int(vstup)):
        print(f"Chyba, zadejte 4 číslovky bez duplicit a nesmí začínat 0.")
        return False
    else:
        return True

def vrat_cislo_uzivatele()-> int:
    """
    Vrátí celé 4místné číslo zadané uživatelem.
    """
    while True:
        vstup_uzivatele = input(">>>")
        if over_vstup_uzivatele(vstup_uzivatele):
            return int(vstup_uzivatele)

def main():
    vypis_pozdrav()
    print(vrat_cislo_uzivatele())


if __name__ == "__main__":
    main()