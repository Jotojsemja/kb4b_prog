import random
cesta = "2. prace_se_soubory\data\citaty.txt"

def citat():
    zacatek_emoji()
    
    with open(cesta, "r", encoding="utf-8") as soubor:
        text = soubor.read()
        radky = []
        for line in text:
            radky.append(line)
        delka = 0
        pocet_radku = text.count('\n')
        print(radky[random.randint(1, pocet_radku)])

    
def zacatek_emoji():
    pocet_e = random.randint(3,5)
    for i in range(pocet_e):
        print(random.choice(["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]), end="")
    print()
    
        
citat()


