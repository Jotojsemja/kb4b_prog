import random
import os
import time

min_bet = 20
money = 200

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


def gamble_toss(money):
    while (money > 0):
        money = coin_toss(money)
        if money is None:
            break
    time.sleep(2)
    cleaner()
    print("Chcípneš na bídu bídníku.")


    
class Black_jack:
    def __init__(self, addressing, money):
        self.addressing = addressing # osovování
        self.cards = [] # karty
        self.money = money # peníze
        self.bet = 0
        self.value = 0 # kolik má ruka hodnutu
        self.aces = 0 # kolik má es protože eso je GG
        self.lost = False # jestli prohrál nebo ne
        
    def show_cards(self):
        print(f"Karty {self.addressing} jsou:")
        for card in self.cards:
            print(card)
            
    def draw_card(self):
        drawed = random.choice(deck)
        deck.remove(drawed)
        self.cards.append(drawed)
        self.values()
        
    def values(self):
        self.value = 0
        for card in self.cards:
            card = card[:-1]
            if card  == "A":
                self.value += 11 
                self.aces += 1
            elif not(card.isdigit()):
                self.value += 10
            else:
                self.value += int(card)
        
    def boom(self):
        while(1):
            if self.value > 21:
                if self.aces > 0:
                    self.value -= 10
                    self.aces -= 1
                    continue
                # udelal jsi boooooom
                self.lost = True
                break
            break
        
    def moves(self):
        while(not(self.lost)):
            move = input("Jaký je tvůj další krok? [stand][hit][double down]\n>")
            print()
            if (move == "stand"):
                break
            if (move == "hit"):
                self.draw_card()
                self.show_cards()
                self.boom()
            else:
                print("Špatný vstup! Zadejte buď: [stand] nebo [hit]")
        
    def results(self):
        if self.value == 21 and len(self.cards) == 2:
            print(f"Karty {self.addressing} obsahují Blackjack!")
            return -1  # jen jako rozlišení 
        else:
            return self.value
        
def dealer_ai():
    while(dealer.value < 17 or dealer.aces == 1):
        dealer.draw_card()
    dealer.show_cards()
    dealer.values()


def game_of_blackjack():
    print("Tvůj zůstatek: ", player.money)
    while(player.bet < min_bet or player.bet > player.money):
        player.bet = input("Zadej svou sázku: \nmin sázka je 20. \n>")
        if player.bet.isnumeric():
            player.bet = int(player.bet)
        else:
            player.bet = 0 # špatný input
    print("Tvá sázka je ", player.bet)
    time.sleep(1)
    cleaner()
    
    dealer.draw_card()
    dealer.show_cards()
    dealer.draw_card()
     
    player.draw_card()
    player.draw_card()
    player.show_cards()
    player.moves()
    time.sleep(2) 
    
    dealer_ai()
    dealer.boom()
    time.sleep(2)
    
    # vyhodnocení hry
    dealer_points = dealer.results()
    player_points = player.results()
    print()
    print(f"{player_points} pro {player.addressing}")
    print(f"{dealer_points} pro {dealer.addressing}")
    
    if player.lost:
        print("Dům vyhrává")
        print("Štěstina se někdy neusmívá")
        # dům bere
        player.money -= player.bet
        
    elif (dealer_points == player_points):
        print("Nikdo nevyhrává", player_points,"vs", dealer_points)
        # prosím vrať sázky!!
        print("Tvůj zůstatek je: ", player.money)
        
    elif player_points == -1:
        print("Právě si vyhrál")
        print("Kámo máš Blackjack co bys čekal?")
        # hráč bere + 250%
        player.money += player.bet * 1.5
        print("Tvůj zůstatek je: ", player.money)
        
    elif dealer_points == -1:
        print("Dům vyhrává")
        print("Dům má Blackjack")
        # Dům bere
        player.money -= player.bet

    elif dealer.lost:
        print("Právě si vyhrál")
        print("Očividně jsi v této hře lepší")
        # hráč bere + 100%
        player.money += player.bet
        print("Tvůj zůstatek je: ", player.money)
                
    elif dealer_points > player_points:
        print("Dům vyhrává")
        print("Někdy štěstina nepřeje")
        # dům bere
        player.money -= player.bet
    else:
        print("Právě si vyhrál")
        # hráč bere + 100%
        player.money += player.bet
        print("Tvůj zůstatek je: ", player.money)
        
    return 
#-----------------------------------------------------      
# Katy!!!!!!!!!!!!! ai
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♠', '♣']
deck = [f"{value}{suit}" for suit in suits for value in values]
# konec ai
def_deck = deck.copy()
player = Black_jack("hráče", money)
dealer = Black_jack("dealera", 0)
# -------------------------------------------------------------------------------------------------------------------------------
cleaner()
game_of_blackjack()

cleaner()
gamble_toss(money) 

