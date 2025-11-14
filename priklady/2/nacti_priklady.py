import random

def nacti_priklad(line):
    cislo_1 = int(line.split()[0])
    znak = line.split()[1]
    cislo_2 = int(line.split()[2])
    
    if znak == "+":
        vysledek = cislo_1 + cislo_2
    elif znak == "-":
        vysledek = cislo_1 - cislo_2
    else:
        vysledek = cislo_1 * cislo_2
    print("Příklad: ", cislo_1, znak, cislo_2, "= ", end="")
    odpoved = int(input())
    return odpoved == vysledek


cesta = "kb4b_prog/2. prace_se_soubory/data/priklady.txt"
with open(cesta, "r", encoding="utf-8") as file:
    # for line in file.readlines():
    #     print(line)
    lines = file.readlines()
    pocet_prikladu = 3
    body = 0

    for i in range(pocet_prikladu):
        if nacti_priklad(lines[i].strip()):
            body += 1
    print("Spravně ", body,"/", pocet_prikladu)