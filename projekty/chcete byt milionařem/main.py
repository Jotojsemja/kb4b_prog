import matplotlib.pyplot as plt
from collections import Counter
import csv
import random as r
import os 
import time

path = "kb4b_prog\projekty\chcete byt milionařem/"
skull_art = r"""
                   .-.
                  (0.0)
                '=.|m|.='
                .='`"``=. 
    """
    
def cleaner():
    os.system('cls')
      
# účty    
# -------------------------------------------------------- 
def register(path):
    path += "uziv_databaze.csv"
    cleaner()
    print("Tak pojďmě si založit účet.")
    user_name = input("Zadej username: \n>")
    user_password = input("Zadej své heslo \n>")
    user_name.strip()
    user_password.strip()
    with open(path, "r",encoding="utf-8") as file:
        lines = file.read()
        if user_name in lines:
            return None, False
    with open(path, "a",encoding="utf-8") as file:
        file.write(f"\n{user_name},{user_password}")
        return user_name, True
 
        
def login(path):
    path += "uziv_databaze.csv"
    cleaner()
    with open(path, "r", encoding="utf-8") as file:
        print("Přihlasení do účtu")
        lines = csv.DictReader(file)
        login_successful = False
        user_name = input("Zadej jméno: \n>")
        user_password = input("Zadej heslo: \n>") 
    
        for line in lines:
            if not(login_successful):
                if line["login"] == user_name and line["password"] == user_password:
                    login_successful = True
                else:
                    login_successful = False
            
    return user_name, login_successful

                
def first_menu(path):
    print("Vítejte v Čicha chce být miliónářem.")
    login_successful = False 

    while(not(login_successful)):
        login_or_register = input("Pro pokračování musíme vědět jestli máte u nás účet[login] nebo nemáte[register]: \n>")
        
        if login_or_register.lower() == "login" or login_or_register.lower() =="ano" or login_or_register.lower() =="yes":
            user_name, login_successful = login(path)
            
        elif login_or_register.lower() == "register" or login_or_register.lower() == "ne"or login_or_register.lower() =="no":
            user_name, login_successful = register(path)
            
        else:
            print("[register, ne, no] / [login, ano, yes]")
            user_name = "idiot"
            time.sleep(4)
            
        if not(login_successful):
            cleaner()
            if user_name is None:
                print("Uživatelskké jméno už se používá zvolte jiné.")
            print("Něco se pokazilo! Nejspíš mezi židlí a pc")
            print(skull_art)
            time.sleep(4)
            
    print(f"Úspěšně přihlášen jako {user_name}")
    time.sleep(2)
    lobby(path, user_name)


# ----------------------    
def lobby(path, user_name):
    question_diff_counts, question_category_count, questions = content_of_questions(path)
    cleaner()
    while(1):
        while(1):
            print(f"Co chceš dělat {user_name}?")
            print("1. Hrát hru. [h]")
            print("2. Zobrazil statistiky otázek. [s]")
            print("3. Vypsat minulé výtěze. [v]")
            print("4. Pravidla a průběh hry. [p]")
            print("5. Odejít / Odhlásit se.[o]")
            choice = str(input("\n>"))
            if choice in ("h", "s", "v", "p", "o"):
                break
            
        match(choice):
            case("h"):
                path += "winners.txt"
                winning = game(questions)
                if winning:
                    print("Výhrál jsi gratulace!")
                    with open(path,"a", encoding="utf-8") as file:
                        file.write(f"user_name\n")
                else:
                    print("Dnes se to nějak nepovedlo. Děkuji za účast!")
                    
            case("s"):
                graph_menu(question_diff_counts, question_category_count)
                
            case("v"):
                path += "winners.txt"
                with open(path,"r", encoding="utf-8") as file:
                    lines = file.read()
                    print("Seznam výtězů:\n")
                    for line in lines:
                        print(line)
            case("p"):
                print("Pravidla hry")
                print("-----------------------------------------")
                print("Hra má vždy 15 úrovní (otázek). Obtížnosti jsou pevně dané:")
                print("• úroveň 1-5: easy,")
                print("• úroveň 6-10: medium,")
                print("• úroveň 11-15: hard.")
                print("Pro každou úroveň:")
                print("1. je náhodně vybrána otázka z příslušné obtížnosti,")
                print("2. hráč odpovídá True nebo False.")
                print("Hra končí:")
                print("• pokud hráč odpoví špatně,")
                print("• nebo pokud správně zodpoví všechny 15 otázek. V tomto případě je uživatelům")
                print("login (s možnou zprávou) uložen do souboru všech vítězů.")
                print("-----------------------------------------")
                time.sleep(10)
            
            case("o"):
                break
# grafy
# ----------------------
def graph_menu(question_diff_counts, question_category_count):
    graff_type = input("Jaký graf chcete? (stačí první písmenko)\nGraf obtížnosti [difficulty] \nGraf kategorií [category]\n>")
    match(graff_type[0]):
        case("d"): # difficulty
            graph(question_diff_counts)
        case("c"): # category
            graph(question_category_count)

      
def content_of_questions(path):
    path += "quiz_questions.csv"
    question_diff_raw = Counter() #vím, že už to můžu počítat přes pole s otázkama, jen se mi tento způsob líbí, tak ho tady nechávám :D
    question_category_raw = Counter()
    questions = [[], [], []] # první easy, druhá medium, třetí hard
    
    with open(path, "r", encoding="utf-8") as file:
        lines = csv.DictReader(file)
        
        for line in lines:
            if line["difficulty"] == "easy":
                questions[0].append((line["question"], line["correct_answer"]))
            elif line["difficulty"] == "medium":
                questions[1].append((line["question"], line["correct_answer"]))
            elif line["difficulty"] == "hard":
                questions[2].append((line["question"], line["correct_answer"]))
                
            question_diff_raw[line["difficulty"]] += 1
            question_category_raw[line["category"]] += 1
        
    question_diff_counts = list(question_diff_raw.items()) 
    question_category_count = list(question_category_raw.items())

    return question_diff_counts, question_category_count, questions
           
       
def graph(question_counts):     
    x_axis, y_asix = zip(*question_counts)     
    plt.bar(x_axis, y_asix, color="red")

    plt.title("Otázky")
    plt.ylabel("Počet otázek")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# hra
# ------------------------
def game(questions):
    level = 0
    level_names = ["lehká","základní","náročná"]
    winning = True
    
    cleaner()
    for i in range(0, 2):
        if i % 5 == 0 and i != 0: # každých  lvl se mění obtížnost
            level += 1
            print("Úroveň se zvyšuje!")
            loading(15)
        question_number = r.randint(0,len(questions[level]))
    
    #forntend
        print(f"{i+1}. otázka.")
        print(f"Úroveň složitosti: {level_names[level]}")
        
        while(True): # cyklus jestli uživatel zadává správné vstupy
            print(questions[level][question_number][0], questions[level][question_number][1])
            answer = input("[True / False] [Pravda / Nepravda]\n>")
            # kontroluji jen první písmenka kvůli upsání
            if answer:
                if answer[0].lower() in ("t", "p"):
                    answer = True
                    break
                elif answer[0].lower() in ("f", "n"):
                    answer = False
                    break
                else:
                    continue
    
        if answer is not questions[level][question_number][1]: 
            print("Někde se někdo asi uklikl protože ty chyby neděláš!")
            loading(5)
            print("Ještě to zkontroluji.")
            loading(9)
            print("Nebyl to omyl reálně jsi odpověděl špatně.")
            print(skull_art)
            loading(20)
            winning = False
            break
        
        cleaner()
        loading(1)
        cleaner()
        
    return winning
        
    

def loading(wait):
    for i in range(wait):
        print(".", end="")
        time.sleep(0.2 * wait/9)
        print("..", end=".")
    print()
    
    
      
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
cleaner()
#+++++++++++++++
# first_menu(path)    
lobby(path, "teo")
#+++++++++++++


#+++++++++++++++++
# graph_menu(path)

# test, test1, test2 = content_of_questions(path)

# print(test)
# print(test1)
# print(test2[0][0][0])

# game(test2)

# answer = ""
# valid_answers = {"f", "F", "t", "T", "p", "P", "n", "N"}
# while(not(answer in valid_answers)): # cyklus jestli uživatel zadává správné vstupy
#         print(valid_answers)
#         answer = input("[True / False] [Pravda / Nepravda]\n>")
#         # kontroluji jen první písmenka kvůli upsání
#         if answer[0].lower() in ("t", "p"):
#             answer = True
#         elif answer[0].lower() in ("f", "n"):
#             answer = False