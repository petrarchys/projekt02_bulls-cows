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

def zkontroluj_cislo(cislo: int)->bool:
    """
    Zkontroluje celé číslo, zda se v něm neopakují číslovky.

    Příklad:
    >>> zkontroluj_cislo(1234) -> true
    >>> zkontroluj_cislo(1122) -> false
    """
    return len(str(cislo)) == len(set(str(cislo)))

def vrat_tajne_cislo()-> int:
    """
    Vrátí 4místné celé číslo bez opakování číslovek 
    """
    while True:
        tajne_cislo = vygeneruj_nahodne_cislo()
        print(f"{tajne_cislo=}")
        if zkontroluj_cislo(tajne_cislo):
            return tajne_cislo

def main():
    vypis_pozdrav()
    print(vrat_tajne_cislo())

if __name__ == "__main__":
    main()