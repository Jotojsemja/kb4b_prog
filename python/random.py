import random
import os
import time

def cleaner():
    os.system('cls')
   
    
def two_choices():
    return random.randint(0,1)
    

def coin_toss(money):
    print("Zůstatek: ",money)
    bet = input("Tvá sázka?\n>")
    if not(bet.isdigit()) or int(bet) > money:
        print("Něco se pokazilo!")
        return money
    bet = int(bet)
    
    your_choice = input("Tvoje volba ""panna"" nebo ""orel""? \n>")
    if not(your_choice == "panna" or your_choice == "orel"):
        print("Něco se pokazilo!")
        return money
    
    if two_choices():
        toss = "orel"
    else:
        toss = "panna"
    time.sleep(0.2)
    print()
    
    print("Tvá volba:", your_choice)
    print("Mince dopadla:", toss)
    if toss == your_choice:
        money += bet *2
        print("Vyhrál jsi!!!!", bet * 2)
    else:
        print("Prohrál jsi. Zkus to znovu.")
        money -= bet
    return money


def gamble_toss():
    money = 100
    while (money > 0):
        money = coin_toss(money)
        if money is None:
            break
    time.sleep(4)
    cleaner()
    print("Chcípneš na bídu bídníku.")


def draw_card():
    drawed = random.choice(deck)
    deck.remove(drawed)
    return drawed

def black_jack():
    player_cards = []
    player_cards.append(draw_card())
    player_cards.append(draw_card())
    print(player_cards)
#-----------------------------------------------------      
# Katy!!!!!!!!!!!!! ai
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♠', '♣']
deck = [f"{value}{suit}" for suit in suits for value in values]
def_deck = deck.copy()
   
# cleaner()
# gamble_toss()

black_jack()
# while(len(deck)):
#     print(draw_card())
# print(def_deck)

