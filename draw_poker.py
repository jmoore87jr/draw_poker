# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:24:19 2019

@author: john
"""

##fix histogram stuff
##create draw() with parameters for hand input, rank of discards, number of draws

#draw simulator (and equity calculator?) for 2-7 single draw

#import packages
import random
import matplotlib.pyplot as plt


#create new deck and shuffle
def newDeck():
    #create list of ranks (ignoring suits for 2-7 draw; J+ are 11-14)
    ranks = []
    for i in range(2,15):
        ranks.append(i)
        
    #create deck. loop through each rank 4x
    deck = []
    for j in range(4):
        for k in range(13):
            deck.append(ranks[k])
            
    #shuffle deck
    random.shuffle(deck)
    return deck


#deal hand, categorize it, and store the category
def deal5(runs = 1):
    #create list for each sim's hand
    allhands = []
    #make newDeck, then deal hand and rank it
    for i in range(runs):
        deck = newDeck()
        hand = []
        for j in range(5):
            hand.append(deck[j])
            deck.remove(hand[j])
        
        #sort hand
        hand.sort(reverse = True)
        ##print("hand: " + str(hand))
        
        #categorize hand
        handType = []
        if hand[0]-hand[1]==1 and hand[1]-hand[2]==1 and hand[2]-hand[3]==1 and hand[3]-hand[4]==1:
            handType = 15
        elif hand[0]==hand[1] or hand[0]==hand[2] or hand[0]==hand[3] or hand[0]==hand[4] or hand[1]==hand[2] or hand[1]==hand[3] or hand[1]==hand[4] or hand[2]==hand[3] or hand[2]==hand[4] or hand[3]==hand[4]:
            handType = 15
        else:
            handType = hand[0]
            
        #store handType in 'allhands'
        allhands.append(handType)
        
    #count frequency of hands and print results
    print("pair+: " + str((allhands.count(15))*100 / len(allhands)) + "%")
    print("A-hi: " + str((allhands.count(14))*100 / len(allhands)) + "%")
    print("K-hi: " + str((allhands.count(13))*100 / len(allhands)) + "%")
    print("Q-hi: " + str((allhands.count(12))*100 / len(allhands)) + "%")
    print("J-hi: " + str((allhands.count(11))*100 / len(allhands)) + "%")
    print("T-hi: " + str((allhands.count(10))*100 / len(allhands)) + "%")
    print("9-hi: " + str((allhands.count(9))*100 / len(allhands)) + "%")
    print("8-hi: " + str((allhands.count(8))*100 / len(allhands)) + "%")
    print("7-hi: " + str((allhands.count(7))*100 / len(allhands)) + "%")


#input hand and draw ranks, return hand dist post-draw
    ###change maxkeep to array length 3, and loop for each draw
def draw(ohand = [], draws = 1, runs = 1, maxKeep = [8,9,11]):
    #create list for each sim's hand
    allhands = []
    for i in range(runs):
        deck = newDeck() #get new shuffled deck
        hand = ohand.copy() #set hand back to inputted hand
        #remove hand cards from deck
        for j in range(len(hand)):
            deck.remove(hand[j])
        random.shuffle(deck) #reshuffle deck
        #loops for each draw
        for k in range(draws):
            hand.sort(reverse = True)
            ##print(hand)
            for l in range(len(hand)):
                #discard cards higher than maxKeep and replace
                if hand[l] > maxKeep[k]:
                    hand[l] = deck.pop(0)
                #discard pairs and replace
                for m in range(len(hand)-1):
                    if hand[m] == hand[m+1]:
                        hand[m] = deck.pop(0)
            ##print(hand)
        #sort hand
        hand.sort(reverse = True)
        #categorize hand
        handType = []
        if hand[0]-hand[1]==1 and hand[1]-hand[2]==1 and hand[2]-hand[3]==1 and hand[3]-hand[4]==1:
            handType = 15
        elif hand[0]==hand[1] or hand[0]==hand[2] or hand[0]==hand[3] or hand[0]==hand[4] or hand[1]==hand[2] or hand[1]==hand[3] or hand[1]==hand[4] or hand[2]==hand[3] or hand[2]==hand[4] or hand[3]==hand[4]:
            handType = 15
        else:
            handType = hand[0]
            
        #store handType in 'allhands'
        allhands.append(handType)
        
    #count frequency of hands and print results
    print("pair+: " + str((allhands.count(15))*100 / len(allhands)) + "%")
    print("A-hi: " + str((allhands.count(14))*100 / len(allhands)) + "%")
    print("K-hi: " + str((allhands.count(13))*100 / len(allhands)) + "%")
    print("Q-hi: " + str((allhands.count(12))*100 / len(allhands)) + "%")
    print("J-hi: " + str((allhands.count(11))*100 / len(allhands)) + "%")
    print("T-hi: " + str((allhands.count(10))*100 / len(allhands)) + "%")
    print("9-hi: " + str((allhands.count(9))*100 / len(allhands)) + "%")
    print("8-hi: " + str((allhands.count(8))*100 / len(allhands)) + "%")
    print("7-hi: " + str((allhands.count(7))*100 / len(allhands)) + "%")

    
    


    