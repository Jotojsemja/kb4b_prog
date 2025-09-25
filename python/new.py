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
    while (True):
        rodne = input("Zadej svoje rodné číslo, určitě si to neuložím: \n >" )
        
        mesic = int(rodne[2] + rodne[3])
        den = int(rodne[4] + rodne[5])
        if mesic < 63 and den < 32:
            break
        print("Chybička někde se vloudila")
    # rok 
    rok = rodne[0] + rodne[1]
    if int(rok) < tento_rok+1:
        rok_spravne = "20" + str(rok)
    else:
        rok_spravne = "19" + str(rok)
    # měsíc
    if mesic > 12:
        mesic -= 50
        pohlavi = "žena" 
    else:
        pohlavi = "muž"
    # den 
    

    print(f"{den}.{mesic}.{rok_spravne} {pohlavi}")

def validator_vstupu():
    while(True):
        zkontrolovat = input("Zadej vstup: ")
        if (int(zkontrolovat) % 2 !=0):
            print("tak ještě jednou")
        else:
            break

#def vymazani_duplicit(pole):
#    neduplikat = []
#    for i in pole:
#            if i == j:
#                neduplikat.append(i)
      
cleaner()
#vypsani_del()
#schody()
#validator_rod_cisla()
validator_vstupu()

