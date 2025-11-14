import random
import turtle
cesta = "kb4b_prog/2. prace_se_soubory/data/slova.txt"
#zacatek kreslicích funkcí -----------------------------------------
def kresleni(pokus):
    t.hideturtle()
    match(pokus):
        case 1:
            nakresli_trouhelnik(75,-130,"green",200)
        case 2:
            nakresli_obdelnik(-25,25,"brown", 20,100)
            nakresli_obdelnik(0,125,"brown", 50,10)
        case 3:
            nakresli_obdelnik(20,110,"grey", 10,20)
        case 4:
            nakresli_kouli(20,90,"red",10)
        case 5:
            nakresli_obdelnik(20, 50,"red", 10,40)
        case 6:
            nakresli_obdelnik(17, 30,"red",4, 20)
            nakresli_obdelnik(17+6, 30,"red",4, 20)
        case 7:
            nakresli_obdelnik(20,70,"red",30,5)


def nakresli_trouhelnik(x,y,barva, velikost):
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.fillcolor(barva)
    t.begin_fill()
    for i in range (3):
        t.left(120)
        t.forward(velikost)
    t.end_fill()
 
    
def nakresli_obdelnik(x, y, barva,strana_a,strana_b):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(barva)
    t.begin_fill()
    
    t.forward(strana_a/2)
    t.left(90)
    t.forward(strana_b)
    t.left(90)
    t.forward(strana_a)
    t.left(90)
    t.forward(strana_b)
    t.left(90)
    t.forward(strana_a/2)
    t.end_fill()


def nakresli_kouli(x, y, barva, velikost):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(barva)
    t.begin_fill()    
    t.circle(velikost)
    t.end_fill()   
#konec kreslicích funkcí ------------------------------------------ 
   
   
def vyber_slovo(cesta): #ai napsal tuhle funkci
    with open(cesta,"r", encoding="utf-8") as soubor:
        slovnik = []
        for line in soubor.readlines():
            slovnik.append(line)
    
    return random.choice(slovnik)


def je_tam(pokus):
    if pismenko in skryte_slovo:
        for i in range(len(skryte_slovo)):
            if pismenko == skryte_slovo[i]:
                hadane_slovo[i] = pismenko 
    else: 
        return pokus+1
    return pokus


def vypis():
    for i in range(len(skryte_slovo)):
        print(hadane_slovo[i], end =" ")
    print("počet pokusů:",pokus )


print("Vítej, tady tě čeká jen oprátka!")
skryte_slovo = vyber_slovo(cesta)
hadane_slovo = ["_"]*len(skryte_slovo)
pokus = 0
max_pokusu = 7
t = turtle.Turtle()        
t.speed(100000000000)

while("".join(hadane_slovo) != skryte_slovo):
    pismenko = input("Zadej písmenko, co si myslíš, že tam je. \n>")
    pokus = je_tam(pokus)
    vypis()
    kresleni(pokus)
    if pokus == max_pokusu:
        break
    
if pokus == max_pokusu:
    for i in range (max_pokusu*50): # trest
            print(skryte_slovo, end =" ")   
    print("byl jsi zabit")
else:
    print("takže to skončilo...dobrá práce!")
    print("nezemřel jsi")    
    print(skryte_slovo)

if input() == "e":
    t.done()