import random
cesta = "kb4b_prog/2. prace_se_soubory/data/"

def citat(cesta):
    zacatek_emoji()
    cesta += "citaty.txt"
    with open(cesta, "r", encoding="utf-8") as soubor:
        radky = soubor.readlines()
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
# citat(cesta)

def nahodny_student(cesta):
    with open(cesta, "r", encoding="utf-8") as soubor:
        return(random.choice(soubor.readlines()))
    
def vyber_studenta(cesta, n):
    cesta += "studenti.txt"
    studenti = []
    with open(cesta, "r", encoding="utf-8") as soubor:
        while(n>0):
            student = nahodny_student(cesta)
            if student in studenti:
                continue
            studenti.append(student)
            n-=1
    studenti.sort()
    return(studenti)
    
studenti = vyber_studenta(cesta, 5)
print(*[student for student in studenti], sep="")

vystupni_soubor = "kb4b_prog/2. prace_se_soubory/data/vystupni.txt"

with open(vystupni_soubor, "w", encoding="utf-8") as file :
    for s in studenti:
        file.write(s)