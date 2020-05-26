# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import packages
import random
import itertools


#create new deck and shuffle
def newDeck():
    #create list of ranks (ignoring suits for 2-7 draw; J+ are 11-14)
    ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    suits = ["s","h","d","c"]
        
    #create deck. loop through each rank 4x
    deck = []
    for i in range(len(suits)):
        for j in ranks:
            card = []
            card.append(j)
            card.append(suits[i])
            deck.append(card)
            
    #shuffle deck
    random.shuffle(deck)
    return deck


#draw 4 card badugi hand
def newHand():
    deck = newDeck()
    hand = []
    for i in range(0,4):
        hand.append(deck.pop(0))
    return hand


#new classification method
def badugiHand(hand):
    perms = list(itertools.permutations(hand))
    finalHand = []
    store3 = []
    store2 = []
    for i in range(len(perms)):
        suitcheck4 = [perms[i][0][1], perms[i][1][1], perms[i][2][1], perms[i][3][1]]
        suitcheck3 = [perms[i][0][1], perms[i][1][1], perms[i][2][1]]
        if perms[i][0][0] > perms[i][1][0] > perms[i][2][0] > perms[i][3][0] and len(set(suitcheck4)) == 4:
            finalHand = list(perms[i])
        elif perms[i][0][0] > perms[i][1][0] > perms[i][2][0] and len(set(suitcheck3)) == 3:
            j = list(perms[i])
            j.remove(j[3])
            store3.append(j)
        elif perms[i][0][0] > perms[i][1][0] and perms[i][0][1] != perms[i][1][1]:
            j = list(perms[i])
            j.remove(j[3])
            j.remove(j[2])
            store2.append(j)
    if len(finalHand) == 0 and len(store3) == 0 and len(store2) == 0:
        hand.sort()
        finalHand = hand[0]
    elif len(finalHand) == 0 and len(store3) == 0:
        store2.sort(reverse = True)
        finalHand = store2[-1]
    elif len(finalHand) == 0:
        store3.sort(reverse = True)
        finalHand = store3[-1]
    list(finalHand)
    finalHand.sort()
    return(finalHand)
      
    
#rank hand
def rank(hand):
    handRank = []
    if len(hand) == 4:
        handRank = str(hand[3][0]) + " Badugi"
    if len(hand) == 3:
        handRank = "3 card " + str(hand[2][0])
    if len(hand) == 2:
        handRank = "2 card"
    if len(hand) == 1:
        handRank = "1 card"
    return(handRank)
    
    
#draw sim for badugi
def draw(ohand = [], draws = 1, runs = 1):
    #list to store all hands
    allhands = []
    for i in range(runs):
        deck = newDeck()
        hand = ohand.copy()
        #remove hand cards from deck
        for j in range(len(hand)):
            deck.remove(hand[j])
        random.shuffle(deck) #reshuffle deck
        #loops for each draw
        for k in range(draws):
            sortedHand = []
            sortedHand = badugiHand(hand) #get the badugi hand minus discards
            while len(sortedHand) < 4: #draw new cards
                sortedHand.append(deck.pop(0))
            hand = sortedHand.copy()
            #print(hand)
        hand = badugiHand(sortedHand)
        hand.sort()
        handRank = rank(hand)
        allhands.append(handRank)
    print("K Badugi: " + str((allhands.count('13 Badugi'))*100 / len(allhands)) + "%")
    print("Q Badugi: " + str((allhands.count('12 Badugi'))*100 / len(allhands)) + "%")
    print("J Badugi: " + str((allhands.count('11 Badugi'))*100 / len(allhands)) + "%")
    print("T Badugi: " + str((allhands.count('10 Badugi'))*100 / len(allhands)) + "%")
    print("9 Badugi: " + str((allhands.count('9 Badugi'))*100 / len(allhands)) + "%")
    print("8 Badugi: " + str((allhands.count('8 Badugi'))*100 / len(allhands)) + "%")
    print("7 Badugi: " + str((allhands.count('7 Badugi'))*100 / len(allhands)) + "%")
    print("6 Badugi: " + str((allhands.count('6 Badugi'))*100 / len(allhands)) + "%")
    print("5 Badugi: " + str((allhands.count('5 Badugi'))*100 / len(allhands)) + "%")
    print("4 Badugi: " + str((allhands.count('4 Badugi'))*100 / len(allhands)) + "%")
    print("K 3card: " + str((allhands.count('3 card 13'))*100 / len(allhands)) + "%")
    print("Q 3card: " + str((allhands.count('3 card 12'))*100 / len(allhands)) + "%")
    print("J 3card: " + str((allhands.count('3 card 11'))*100 / len(allhands)) + "%")
    print("T 3card: " + str((allhands.count('3 card 10'))*100 / len(allhands)) + "%")
    print("9 3card: " + str((allhands.count('3 card 9'))*100 / len(allhands)) + "%")
    print("8 3card: " + str((allhands.count('3 card 8'))*100 / len(allhands)) + "%")
    print("7 3card: " + str((allhands.count('3 card 7'))*100 / len(allhands)) + "%")
    print("6 3card: " + str((allhands.count('3 card 6'))*100 / len(allhands)) + "%")
    print("5 3card: " + str((allhands.count('3 card 5'))*100 / len(allhands)) + "%")
    print("4 3card: " + str((allhands.count('3 card 4'))*100 / len(allhands)) + "%")
    print("3 3card: " + str((allhands.count('3 card 3'))*100 / len(allhands)) + "%")
    print("2 card: " + str((allhands.count('2 card'))*100 / len(allhands)) + "%")
        
    
            
    