# draw_poker
Monte Carlo simulator for 2-7 draw poker games

draw_poker.py currently has 2 functions: 

1. deal5() only takes an argument for the # of simulations. It deals 5 cards and categorizes the hand into 7-hi thru pair+. 
  *e.g. deal5(100000) for the distribution of starting 5 card hands*
2. draw() takes arguments for starting hand, # of draws, # of simulations, and maximum rank to keep for each draw. It outputs the frequency of hands 7-hi thru pair+ after drawing.
  *e.g. draw([14,12,8,7,2],1,100000,[11,11,11]) to draw once, with AQ872, for 100,000 trials, with keep of J or better.
        draw(13,11,8,7,3),3,100000) to draw 3 times, with KJ873, for 100,000 trials, with default keeps of 8,9,J on respective draws.*

Future plans:

1. input 2 hands
2. range vs. range equity graph after draw



Badugi.py:

1. newHand() will show you the format of a hand
2. draw() takes starting hand, # of draws, # of simulations

