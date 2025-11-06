# import random

# dice = [1, 2, 3, 4, 5, 6]
# hod = 0
# def dice_roll():
#     return random.choice(dice)

# def two_die(): 
#     global hod
#     dice_1 = 1
#     dice_2 = 2
#     print("Hody")
#     while(dice_1 != dice_2):
#         dice_1 = dice_roll()
#         dice_2 = dice_roll() 
#         print(dice_1, dice_2)
#         hod +=1
#     return(dice_1, dice_2)

# dice_1, dice_2 = two_die()
# print("Padla dvojce: ", dice_1, dice_2)
# print("Počet hodů: ", hod)

# import random
# teploty = []
# def temps():
#     global teploty
#     for i in range (24):
#         teploty.append(random.randint(-10,20))
    
# def statistic():
#     global teploty
#     pocet = 0
#     temps()
#     print("Naměřené teploty:", end="")
#     for i in range(23):
#         print(" ",teploty[i], end="")
#     print()
#     print("Průměrná teplota je: ", round(sum(teploty)/24, 1))
#     for i in range(23):
#         if teploty[i] < 0:
#             pocet +=1
#     print("Tolik teplot je pod bodem mrazu: ", pocet)
# statistic()

import random 

def novy_priklad():
    vysledek = random.randint(0, 100)
    return vysledek

def reseni_prikladu():
    vysledek_1 = novy_priklad()
    print("sqrt(",vysledek_1*vysledek_1,  end="")
    odpoved_1 = int(input( ") = "))
    
    
def test():
    vysledek_1 = novy_priklad()
    vysledek_2 = novy_priklad()
    vysledek_3 = novy_priklad()
    print("sqrt(",vysledek_1*vysledek_1,  end="")
    odpoved_1 = int(input( ") = "))
    print("sqrt(",vysledek_2*vysledek_2,  end="")
    odpoved_2 = int(input( ") = "))
    print("sqrt(",vysledek_3*vysledek_3,  end="")
    odpoved_3 = int(input( ") = "))
    print("Vaše odpovědi: ", vysledek_1 == odpoved_1, vysledek_2 == odpoved_2, vysledek_3 == odpoved_3)
    
test()