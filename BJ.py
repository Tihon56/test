import random as r

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

#def for making starting hand
def make_a_hand (deck):
    hand = []
    for i in range(2):
        r.shuffle(deck)
        card = deck.pop
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

# def for counting points
def at_all (hand):
    at_all = 0
    for card in hand:
        if card=="J" or card=="Q" or card=="K": #for pictures
            at_all+=10
        #condition for ace
        if card=="A":
            if at_all>=11:at_all+=1
            else: at_all+= 11
        else: at_all+=card
    return at_all

# def for adding card in hand
def one_more(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand


#game

def game():
    print ("Welcome to BJ!/n")
    dealer_hand = make_a_hand(deck)
    player_hand = make_a_hand(deck)


