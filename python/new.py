import os
tento_rok = 25
def cleaner():
    os.system('cls')
    
def vypsani_del():
    vysledky = []
    cislo = int(input("Zadej číslo a dostaneš jeho dělitele:"))
    for i in range(1, cislo+1):
        if cislo % i == 0:
            vysledky.append(i)
    print(vysledky)
    
def schody():
    pocet = int(input("Zadej delku schodů:"))
    znak = input("Zadej materiál schodů: ")
    
    for i in range(pocet):
        print(i * znak)
    
def validator_rod_cisla():
    rodne = input("Zadej svoje rodné číslo, ucčitě si to neuložím: \n >" ) 
    rok = int(rodne[0] + rodne[1])
    if rok > 00 and rok < tento_rok:
        print(rok)
cleaner()
#vypsani_del()
#schody()
validator_rod_cisla()


