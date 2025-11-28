import matplotlib.pyplot as plt
import csv
import random
import os 
import time

cesta = "kb4b_prog/2. prace_se_soubory/data/"
def cleaner():
    os.system('cls')

def people(cesta):
    cesta +="vira_v_cesku.csv"
    with open(cesta, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        max = 0
        belivers = 0
        religion_vyskyt = []
        religion = [
    "Apoštolská církev",
    "Bratrská jednota baptistů",
    "Církev adventistů sedmého dne",
    "Církev bratrská",
    "Církev československá husitská",
    "Církev Ježíše Krista Svatých posledních dnů v České republice",
    "Církev řeckokatolická",
    "Církev římskokatolická",
    "Českobratrská církev evangelická",
    "Evangelická církev augsburského vyznání v České republice",
    "Evangelická církev metodistická",
    "Federace židovských obcí v České republice",
    "Jednota bratrská",
    "Křesťanské sbory",
    "Luterská evangelická církev a. v. v České republice",
    "Náboženská společnost českých unitářů",
    "Náboženská společnost Svědkové Jehovovi",
    "Novoapoštolská církev v ČR",
    "Pravoslavná církev v českých zemích",
    "Slezská církev evangelická augsburského vyznání",
    "Starokatolická církev v ČR",
    "Církev sjednocení (moonisté)",
    "Scientologická církev",
    "Církev Křesťanská společenství",
    "Anglikánská církev",
    "islám",
    "buddhismus",
    "hinduismus",
    "Mezinárodní společnost pro vědomí Krišny, Hnutí Hare Krišna",
    "Jiné",
    "Buddhismus Diamantové cesty linie Karma Kagjü",
    "Církev živého Boha",
    "Česká hinduistická náboženská společnost",
    "Obec křesťanů v České republice",
    "Ruská pravoslavná církev, podvorje patriarchy moskevského a celé Rusi v České republice",
    "Ústředí muslimských obcí",
    "Višva Nirmala Dharma",
    "Hnutí Grálu",
    "Hnutí Nového věku (New Age)",
    "katolická víra (katolík)",
    "protestantská/evangelická víra (protestant, evangelík)",
    "křesťanství",
    "judaismus",
    "esoterismus",
    "Církev Nová naděje",
    "Církev Slovo života",
    "Církev víry",
    "Církev Svatého Řehoře Osvětitele",
    "Armáda spásy - církev",
    "Církev Nový Život",
    "Církev Oáza",
    "Společenství Josefa Zezulky",
    "Kněžské bratrstvo svatého Pia X.",
    "Théravádový buddhismus",
    "Společenství baptistických sborů",
    "Společenství buddhismu v České republice",
    "Křesťanská církev essejská",
    "pastafariánství",
    "satanismus",
    "agnosticismus",
    "animismus",
    "Bahá'í víra",
    "deismus",
    "konfucianismus",
    "sikhismus",
    "šintoismus",
    "taoismus",
    "zoroastrismus",
    "druidismus",
    "rastafariánství",
    "věřící - hlásící se k církvi - název neuveden"
]
        for line in reader:
            if line["uzemi_txt"] == "Brno":
                # if line["vira_txt"] in religion:
                    belivers += int(line["hodnota"])
                    religion_vyskyt.append(line["vira_txt"])
                    hodnota = line["hodnota"]
                    vira_txt = line["vira_txt"]
                    # print(line["hodnota"])
                    print(f"{hodnota} a {vira_txt}")
        
# a)        
                    if int(line["hodnota"]) > max:
                        max = int(line["hodnota"])
                        max_line = line
                    
        print(belivers)
        print(max, max_line["vira_txt"])                   
        print(f"prumerne {belivers/(len(religion_vyskyt)/2)}")
                    
                
                
            
people(cesta)