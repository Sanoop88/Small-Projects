'''Aim:- To create a blackjack game. 
So a deck of cards has 52 cards(without jokers). 

13 cards of each suit, i.e. diamonds, hearts, spade, clubs. 
Each suite has an Ace, cards from 2-10, a king, a queen and jack.
For blackjack an ace could have a value of 1 or 11, number cards have their own face value 
and a king, queen, jack each have a value of 10.

We'll first need to create 4 decks. wondering should I create a deck class and then a seperate card class, hmmm.


logic is a bit tricky for this, hmmm. 

so i was thinking i'd have a list for player and a list for dealer. and keep appending that list based on the  
inputs. but we'll have to stop after 3 hits

'''
import random
import time
class blackjack:

  #declaring class variables
  suit=('clubs','hearts','spades','diamonds')
  ranks=('ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king')
  values={'ace':11,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10}
  
  filler=[]
  def randomcard(self):
    #this function calls a card from our deck and adds it to the filler, filler ensures no card in repated again within a game.
    self.face=random.choice(self.suit)
    self.val=random.choice(self.ranks)
    self.facevalue=f'{self.val} of {self.face}'
    
    if self.val=='ace':
      choose=int(input(f'You\'ve got an {self.facevalue}, choose (11 or 1):- '))
      while choose!=1 and choose!=11:
        print ('invalid input')
        choose=int(input('Choose your value for Ace (11 or 1):- '))
      self.numvalue=choose
    else:
      self.numvalue=self.values[self.val]
    if self.facevalue not in self.filler:
      self.filler.append(self.facevalue)
      return (self.facevalue,self.numvalue)
    else:
      return self.randomcard() 
    
    
  
  def player_input(self):
    #takes players input until he decides to hit or stay
    print ('\n\n')
    print ('Player\'s turn:-')
    self.flag=True
    self.player_total=0
    (a,b)=self.randomcard()
    (c,d)=self.randomcard()
    print (a)
    time.sleep(1)
    print (c)
    self.player_total=b+d
    print (f'Player\'s total:- {self.player_total}')
    while self.player_total<=21:
      choice=input('Enter H to Hit or S to stay:- ').lower()
      if choice=='h':
        (e,f)=self.randomcard()
        print (e)
        self.player_total+=f
        print (f'Player\'s total:- {self.player_total}')
      elif choice=='s':
        print ('Player Stays')
        break
    else:
      print ('Player1 has busted, Dealer Wins!')
      self.flag=False


  def dealer_input(self):
    #takes dealers input until he wins/ties or busts
    print ('Dealer\'s turn:-')
    self.dealer_total=0
    (a,b)=self.randomcard()
    print (a)
    self.dealer_total+=b
    print (f'Dealer\'s total:- {self.dealer_total}')
    print ('\n')
    self.player_input()
    if self.flag==True:
      print ('\n\n')
      print ('Dealer\'s turn:-')
      print (a)

      while self.dealer_total<=21:
        (c,d)=self.randomcard()
        print (c)
        self.dealer_total+=d
        #print (self.dealer_total)
        time.sleep(1)
        if self.dealer_total==self.player_total and self.dealer_total<=21:
          print (f'Dealer\'s total:- {self.dealer_total}')
          print (f'Game tied at {self.dealer_total}. Dealer wins, Player loses!')
          break
        elif self.dealer_total>self.player_total and self.dealer_total<=21:
          print (f'Dealer\'s total:- {self.dealer_total}')
          print ('Dealer has won, Player loses!')
          break
      else:
        print (self.dealer_total)
        print ('Dealer has busted, Player wins!')





#just two functions here, one to initialize the game one to call the dealer's first input, which inturn calls the player_input as well

tester=blackjack()
tester.dealer_input()



