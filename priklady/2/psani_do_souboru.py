import random
import os 
import time

cesta = "kb4b_prog/2. prace_se_soubory/data/"
def cleaner():
    os.system('cls')
    
def gen_ran_numbers(cesta):
    cesta += "gen_cislo.txt"
    number_min = int(input("Zadej číslo min \n>"))
    number_max = int(input("Zadej číslo max \n>"))
    number_count = int(input("Zadej kolik  \n>"))
    generated = []
    
    for i in range(number_count):
        generated.append(random.randint(number_min, number_max))
    with open(cesta, "w", encoding="utf-8") as file:
        for number in generated:
            writed = str(number) + "\n"
            file.write(writed)
# gen_ran_numbers(cesta)  

def chatlog(cesta):
    cesta += "chat_log.txt"
    open(cesta, "w", encoding="utf-8").close()
    print("Pro ukončení zadej: KONEC")
    while(1):
        username = input("Zadej za koho píšeš: \n>")
        if "KONEC" in username:
            break
        massage = input("zadej zprávu:\n> ")
        if "KONEC" in massage:
            break
        with open(cesta, "a", encoding="utf-8") as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {username}: {massage}\n")
        print("Úspěšně zapsáno!\n")
# chatlog(cesta)

def create_account(cesta):
    user_name = input("Zadej username: \n>")
    user_password = input("Zadej své heslo \n>")
    currency = 1000
    with open(cesta, "a",encoding="utf-8") as file:
        file.write(f"{user_name};{user_password};{currency}")
        
def log_in(cesta):
    with open(cesta, "r", encoding="utf-8") as file:
        print("Přihlasení do účtu")
        lines = file.readlines()
        for line in lines:
            user_name_try = input("Zadej jméno: \n>")
            user_password_try = input("Zadej heslo: \n>")
            if user_name_try in line or user_password_try in line:
                print("uspesne prihlasen!")
            else:
                print("neco se pokazilo")
        
                
            
def game_room(cesta):
    cesta += "uziv_databaze.txt"
    log_in(cesta)
    create_account(cesta)
    
game_room(cesta)