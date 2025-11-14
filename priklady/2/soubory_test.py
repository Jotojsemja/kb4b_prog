import random
cesta_1 = "kb4b_prog/2. prace_se_soubory/data/citaty.txt"
cesta_2 = "kb4b_prog/2. prace_se_soubory/data/studenti.txt"
def citat():
    zacatek_emoji()
    with open(cesta_1, "r", encoding="utf-8") as soubor:
        text = soubor.readlines()
        radky = []
        for radek in text:
            radky.append(radek)
        pocet_radku = len(radky)
        vybrany_radek = random.randint(1, pocet_radku)
        citat = radky[vybrany_radek].strip()
        print(citat.split("-")[0],"###",citat.split("-")[1], "###")
    print(random.choice(["💥", "🔥", "❤️‍", "😎", "🤣"]))

def zacatek_emoji():
    pocet_e = random.randint(3,5)
    for i in range(pocet_e):
        print(random.choice(["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]), end="")
    print()


def vyber_studenta():
    with open(cesta_2, "r", encoding="utf-8") as soubor:
        return(random.choice(soubor.readlines()))
print(vyber_studenta())

        

