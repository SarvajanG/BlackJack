#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

#GLOBALS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True


# In[2]:


class Card:
    
    def __init__(self,rank,suit):
        # Create a Card
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()
        self.value = values[rank.capitalize()]
    
    def __str__(self):
        # Print a Card
        return self.rank + ' of ' + self.suit


# In[3]:


Five_of_Clubs = Card(ranks[3], suits[3])
Ace_of_Clubs = Card(ranks[-1],suits[-1])
King_of_Spades = Card(ranks[-2], suits[-2])


# In[4]:


class Deck:
    
    def __init__(self):
        # Create a Deck of Cards
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
                
                
    def show_cards(self):
        # Print out all of the cards currently in the deck
        x = 1
        for card in self.all_cards:
            print("{} {}".format(x, card))
            x += 1          
            
    def shuffle(self):
        # Shuffle Cards in the Deck
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        # Remove the first card in the Deck (top of the Deck)
        return self.all_cards.pop(0)
    
    


# In[5]:


class Hand(Deck):
    
    def __init__(self):
        # Create a Hand
        self.all_cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        # Add a card to the Hand and increase value of hand and increase count of Aces in hand
        self.all_cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        # Adjust value of hand when hand is over 21 and Aces are available to be adjusted, decrese count of Aces when adjusted
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
            


# In[6]:


class Chips:
        
        def __init__(self):
            #Create a set of chips
            self.total = 100 # Default
            self.bet = 0
            
        def win_bet(self):
            # Add winnings from bet to total
            self.total += self.bet
        
        def lose_bet(self):
            # Subtract bet losings from total
            self.total -= self.bet
        


# In[7]:


def take_bet():
    # Take a bet from the player and adjust player bet value
    
    while True:
        try:
            print('Your available funds are ${}'.format(player_chips.total))
            player_chips.bet = int(input("Enter the amount you would like to bet: "))
        except:
            print("\nEntry is not an valid numeric character, Please try again")
        else:
            if player_chips.bet <= player_chips.total:
                print("You have bet ${}".format(player_chips.bet))
                break
            print("\nYou cannot bet more than your available funds!")


# In[8]:


def hit(deck,hand):
    # Place a Card from the top of the deck into the players hand
    hand.add_card(deck.deal_one())
    if hand.value > 21:
        hand.adjust_for_ace()


# In[9]:


def hit_or_stand(deck,hand):
    # Ask the player whether they want to hit or stand
    global playing
    player_choice = "INVALID"
    
    while player_choice not in ['Hit','Stand']:
        player_choice = input("Would you like to Hit or Stand: ")
        if player_choice == 'Hit':
            hit(deck,hand)
            print("You chose Hit!")
        elif player_choice == 'Stand':
            playing = False
            print("You chose Stand!")
        else:
            print("\nInvalid entry, Please try again")


# In[10]:


def show_some(player,dealer):
    # Show some dealer cards and all player cards
    print("DEALER:")
    print("Hidden Card: Unknown")
    for card in dealer.all_cards[1:]:
        print('{}: {}'.format(card,card.value))
    print("Shown Value: {}".format(dealer.value-dealer.all_cards[0].value))
    
    print("\n"*3)
    
    print("PLAYER:")
    for card in player.all_cards:
        print('{}: {}'.format(card,card.value))
    print("Total Value: {}".format(player.value))
    


# In[11]:


def show_all(player,dealer):
    # Show all cards
    print("DEALER:")
    for card in dealer.all_cards:
        print('{}: {}'.format(card,card.value))
    print("Total Value: {}".format(dealer.value))
    
    print("\n"*3)
    
    print("PLAYER:")
    for card in player.all_cards:
        print('{}: {}'.format(card,card.value))
    print("Total Value: {}".format(player.value))


# In[12]:


def player_busts():
    player_chips.lose_bet()
    print("BUST!, Your cards exceeded 21!")
    print("You lost ${}".format(player_chips.bet))
    

def player_wins():
    player_chips.win_bet()
    print("You WIN!")
    print("You Won ${}!".format(player_chips.bet))
    

def dealer_busts():
    player_chips.win_bet()
    print("The Dealer BUSTED!, You WIN!")
    print("You Won ${}!".format(player_chips.bet))
    
    
def dealer_wins():
    player_chips.lose_bet()
    print("You lose, Dealer has a better hand!")
    print("You lost ${}".format(player_chips.bet))
    
    
def push():
    print("PUSH!, You tied the Dealer's Hand")
    print("Your chips remain the same: ${}".format(player_chips.total))


# In[ ]:





# In[ ]:





# In[ ]:


while True:
    # Opening Statement
    print("Welcome to BlackJack!")
    
    # Create and Shuffle Deck
    deck = Deck()
    deck.shuffle()
    
    # Create Player and Dealer Hands
    player = Hand()
    dealer = Hand()
    
    # Create Player's Chip Set and ask for Player's Bet
    player_chips = Chips()
    take_bet()
    print("\n")
    
    # Deal two cards each to player and dealer
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    
    # Show some cards
    show_some(player,dealer)
    
    while playing:
        
        # Ask player for hit or stand
        hit_or_stand(deck,player)
        
        print("-"*100)
        
        # Show some cards
        show_some(player,dealer)
        
        # If the player busts
        if player.value > 21:
            player_busts()
            break
        elif playing == False:
            # Dealer hits if needed
            while dealer.value < 17:
                hit(deck,dealer)
                print("The dealer has Hit!")
                print("-"*100)
                show_some(player,dealer)

            # Show all the cards
            print("-"*100)
            show_all(player,dealer)

            # Check who won
            if dealer.value > 21:
                dealer_busts()
            elif player.value > dealer.value:
                player_wins()
            elif player.value < dealer.value:
                dealer_wins()
            elif player.value == dealer.value:
                push()

            # Print out Chip total
            print("Your chip total is now ${}".format(player_chips.total))
        
    # Play Again?
    replay = "INVALID"
    while replay not in ['Y','N']:
        replay = input("Would you like to play again 'Y' or 'N': ")
        if replay == 'Y':
            continue
        elif replay == 'N':
            break
        else:
            print("Invalid entry, please try again")
    if replay == 'N':
        print ("Thanks for playing, come back soon!")
        break
    else:
        playing = True


# In[ ]:




