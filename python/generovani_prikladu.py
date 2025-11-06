import random

def generuj_priklad():
    cislo_1 = random.randint(0,10)
    cislo_2 = random.randint(0,10)
    znak = random.choice(["+", "-"])
    if znak == "+":
        vysledek = cislo_1 + cislo_2
    elif znak == "-":
        vysledek = cislo_1 - cislo_2
    else:
        vysledek = cislo_1 * cislo_2
    print("Příklad: ", cislo_1, znak, cislo_2, "= ", end="")
    odpoved = int(input())
    return odpoved == vysledek


pocet_prikladu = 3
body = 0

for i in range( pocet_prikladu):
    if generuj_priklad():
        body += 1
print("Spravně ", body,"/", pocet_prikladu)
