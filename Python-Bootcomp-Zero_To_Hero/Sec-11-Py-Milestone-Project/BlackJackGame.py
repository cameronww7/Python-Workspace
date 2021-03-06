from __future__ import print_function
import random

"""
 Prompt 82-BlackJack-Game
"""

print("82-BlackJack-Game")

"""
Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses, or busts, etc...

And most importantly:

You must use OOP and classes in some portion of your game. 
You can not just use functions in your game. 
Use classes to help you define the Deck and the Player's hand. 
There are many right ways to do this, so explore it well!

Feel free to expand this game. 
Try including multiple players. 
Try adding in Double-Down and card splits! 
Remember to you are free to use any resources you want and as always HAVE FUN!

Game Play
To play a hand of Blackjack the following steps must be followed:

- Create a deck of 52 cards
- Shuffle the deck
- Ask the Player for their bet
- Make sure that the Player's bet does not exceed their available chips
- Deal two cards to the Dealer and two cards to the Player
- Show only one of the Dealer's cards, the other remains hidden
- Show both of the Player's cards
- Ask the Player if they wish to Hit, and take another card
- If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
- If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
- Determine the winner and adjust the Player's chips accordingly
- Ask the Player if they'd like to play again

Playing Cards
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks 
(2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, 
Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without 
busting. As a starting point in your program, you may want to assign variables to store a list of suits, 
ranks, and then use a dictionary to map ranks to values.

The Game
Imports and Global Variables
Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare 
variables to store suits, ranks and values. You can develop your own system, or copy ours below. Finally, 
declare a Boolean value to be used to control while loops. This is a common practice used to control the 
flow of the game.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

"""

print("\n82-BlackJack-Game\n")
print("- - - - - - - - - - ")


"""
 Black Jack Game Classes
"""
class Card:
    """
    This class will function as a card.
    Meaning it will have a Rank and Suite.
    Will be apart of an array of some sort.
    Will output for example "Queen of Hearts" if printed.
    """
    def __init__(self, xSuite, xRank, xValue):
        self.suit = xSuite
        self.rank = xRank
        self.value = xValue

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

    def get_suite(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

    def get_Card(self):
        return "%s of %s" % (self.rank, self.suit)

    def get_Card_Value(self):
        return self.value

    def get_Card_Suite(self):
        return self.suit


class Deck(Card):
    """
    This Class will create an Entire Desk of Cards (Card Class).
    This wil be used to play the game.
    Should keep track of what is dealt to prevent duplicates.
    """
    def __init__(self, xSuite, xRank, xValue):
        suit = xSuite
        rank = xRank
        value = xValue
        self.counter = 0

        self.deck = []  # start with an empty list

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, xValue.get(rank))
                self.deck.append(card)
                self.counter += 1

    def get_counter(self):
        return self.counter

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one_card(self):
        return self.deck.pop()

    def __str__(self):
        counter = 1
        for index in self.deck:
            print("%s: %s" % (counter, index))
            counter += 1
        return ""

class Hand:
    """
    Hand Class is what each player has in this hand
    So at least two objects, First a Player Hand and second the Dealer Hand
    """
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.value2 = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def set_Value(self):
        # I need to loop through the dictionary and add up the value of each card
        # and assign it a total value so
        # add up, Ace + 10 = Blackjack, 10 + 7 = 17
        self.value = 0
        self.value2 = 0

        for index in self.cards:
            # Tracks the Number of Aces

            if index.get_Card_Value() == 11:
                self.value2 += 1
                self.aces -= 1
            elif self.value2 != 0:
                self.value2 += index.get_Card_Value()
                self.aces -= 1
            elif self.aces >= 1:
                self.value2 += index.get_Card_Value()

            self.value += index.get_Card_Value()

        #print(self.value)

    def get_value(self):
        return self.value

    def get_value_2(self):
        return self.value2

    def get_cards(self):
        return self.cards

    def aces_exist(self):
        if self.aces >= 1:
            return True
        else:
            return False

    def add_card(self, xCard):
        # adds 1 card
        self.cards.append(xCard)

        if xCard.get_Card_Value() == 11:
            self.aces += 1

        return True

    def add_cards(self, xCards):
        # adds as many cards are sent in, proply useless
        for card in xCards:
            self.cards.append(card)
        return True

    def adjust_for_ace(self):
        # Provides two values to account for an Ace
        pass

    def show_first_card(self):
        return "{}".format(self.cards[0])

    def show_first_card_value(self):
        return "{}".format(self.cards[0])

    def get_first_card(self):
        return self.cards[0]

    def clear_hand(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.value2 = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def __str__(self):
        counter = 1
        for index in self.cards:
            print("%s: %s" % (counter, index))
            counter += 1
        return ""


class Chips:
    """
    Chips Class is to hold each players chips
    Needs to Make bets and hold each player total
    """
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def get_bet(self):
        return self.bet

    def balance(self):
        return self.total

    def place_bet(self, xPlacedBet):
        if xPlacedBet <= self.total:
            print("Bet Placed")
            self.bet = xPlacedBet
            self.total -= xPlacedBet
            return True
        else:
            print("You do not have that Chip amount")
            return False

    def win_bet(self):
        self.total = self.total + self.bet * 2
        self.bet = 0
        return self.total

    def lose_bet(self):
        self.bet = 0
        return self.total

    def clear_bet(self):
        self.total += self.bet
        return True

    def __str__(self):
        #print("Stack Total : {}".format(self.total))
        return "Stack Total : {}".format(self.total)


"""
 Black Jack Game Functions
"""

def Show_Player_Hand(xPlayer_hand):
    print("\nShowing Player Hand")
    xPlayer_hand.set_Value()
    print("Players Total Hand Value is {}".format(xPlayer_hand.get_value()))
    print(xPlayer_hand)
    return True

def Show_Dealer_Hand_OneUp(xDealer_hand):
    print("\nDealer is showing")
    xDealer_hand.set_Value()
    print("{}, face up face is : {}".format(xDealer_hand.get_first_card().get_value()+10, xDealer_hand.get_first_card()))
    return True

def Show_Dealer_Hand(xDealer_hand):
    print("\nShowing Dealer Hand")
    print("Dealers Total Hand Value is {}".format(xDealer_hand.get_value()))
    print(xDealer_hand)
    return True

def Show_Both_Hands(xPlayer_hand, xDealer_hand):
    Show_Dealer_Hand(xDealer_hand)
    Show_Player_Hand(xPlayer_hand)
    return True

def Prompt_User_For_Bet(xPlayer_chips):
    print("\nYour Current Balance is {}".format(xPlayer_chips.balance()))
    while True:
        try:
            # First Attempt - will be successful if an Int comes in
            players_Bet = int(input("Please enter Your Bet: "))

        except:
            # If an error pops it will display an Error and re-prompted the user for an Int
            print("Looks like you did not enter an integer!")
            continue

        else:
            # Breaks the infinite while loop if a int is entered
            print("Player Bet {}".format(players_Bet))
            break

    if not xPlayer_chips.place_bet(players_Bet):
        while True:
            try:
                # First Attempt - will be successful if an Int comes in
                players_Bet = int(input("Please enter Your Bet: "))

            except:
                # If an error pops it will display an Error and re-prompted the user for an Int
                print("Looks like you did not enter an integer!")
                continue

            else:
                # Breaks the infinite while loop if a int is entered
                print("Player Bet {}".format(players_Bet))
                break

        print("Player Balance {} after Betting".format(xPlayer_chips.balance()))
    return True

def Prompt_User_To_Contiune():
    exitVar = True
    while exitVar:
        userInput = input("Would you like to play blackjack (Enter y for yes, n for No) : ")
        userInput = userInput.lower()

        if userInput == "n":
            return False
        elif userInput == "y":
            return True
        else:
            print("\nLooks like you entered in the wrong input, please try again!\n")

def Setup_Hands(xPlayer_hand, xDealer_hand, xNewDeck):
    for index in range(0, 2):
        xPlayer_hand.add_card(xNewDeck.deal_one_card())
        xDealer_hand.add_card(xNewDeck.deal_one_card())

def Prompt_User_To_Hit_Or_Stay(xPlayer_hand, xPlayer_chips, xNewDeck):
    userInput = "H"

    while xPlayer_hand.get_value() < 22 and userInput == "H":
        try:
            # First Attempt - will be successful if an Int comes in
            userInput = input("\nPlease Enter if you want to Stay, Hit"
                        "\nEnter S to Stay"
                        "\nEnter H to Hit"
                        "\nEnter your Choice: ")

            userInput = userInput.upper()

            if userInput == "S" or userInput == "H":
                valid = True
            else:
                valid = False

        except:
            # If an error pops it will display an Error and re-prompted the user for an Int
            print("Looks like you didn't enter a correct character")
            continue

        if valid:
            if userInput == "S" and xPlayer_hand.get_value() < 22:
                print("Player Stays")
                print(xPlayer_chips.clear_bet())

            elif userInput == "H" and xPlayer_hand.get_value() < 22:
                print("\nPlayer Hits")
                xPlayer_hand.add_card(xNewDeck.deal_one_card())
                Show_Player_Hand(xPlayer_hand)
        else:
            print("\nError!"
                  "\nLooks like you didnt enter a correct character"
                  "\nPlease Try again!\n")

    if xPlayer_hand.get_value() < 22:
        return False

    return True

def Check_If_Bust(xPlayer_hand):
    if xPlayer_hand.get_value() > 21:
        return True
    else:
        return False

def Check_Win_Or_Lose(xPlayer_hand, xDealer_hand, xPlayer_chips):
    if Check_If_Bust(xPlayer_hand):
        print("Player Loses")
        xPlayer_chips.lose_bet()
        return False
    elif xPlayer_hand.get_value() > xDealer_hand.get_value():
        print("Player Wins!")
        xPlayer_chips.win_bet()
        return True
    elif xPlayer_hand.get_value() == xDealer_hand.get_value():
        print("Draw")
        xPlayer_chips.clear_bet()
        return True
    elif Check_If_Bust(xDealer_hand) or xPlayer_hand.get_value() < xDealer_hand.get_value():
        print("Player Loses")
        xPlayer_chips.lose_bet()
        return False



def Play_Dealers_Hand(xDealer_hand, xNewDeck):
    while xDealer_hand.get_value() < 16:
        xDealer_hand.add_card(xNewDeck.deal_one_card())
        xDealer_hand.set_Value()

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

newDeck = Deck(suits, ranks, values)
newDeck.shuffle()
#print(newDeck)


player_1 = "Player 1"
dealer   = "Dealer"

print("Lets Play Black Jack")


while Prompt_User_To_Contiune():
    print("lets Play blackjack!")

    # Setup Player Hand & Chips
    player_hand = Hand()
    player_chips = Chips()

    # Setup Dealer Hand & Chips
    dealer_hand = Hand()

    Prompt_User_For_Bet(player_chips)

    print("Dealing Hands")
    Setup_Hands(player_hand, dealer_hand, newDeck)

    Show_Dealer_Hand_OneUp(dealer_hand)
    Show_Player_Hand(player_hand)

    Prompt_User_To_Hit_Or_Stay(player_hand, player_chips, newDeck)

    Play_Dealers_Hand(dealer_hand, newDeck)

    Show_Both_Hands(player_hand, dealer_hand)
    Check_Win_Or_Lose(player_hand, dealer_hand, player_chips)

    print("\nYour Current Balance is {}\n".format(player_chips.balance()))


