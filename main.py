#21
#21 Dec 2021
#Ryan Cullen        

from count import f_count # The values of the cards.
from random import sample
from deck import l_deck # The card deck.
from time import sleep

cardcount = 0 # Reset variables.
done = 0
pscore = 0
cscore = 0
phand = {}
chand = {}

def f_playerhand() :  # Draw one card to the player.
  global pkey, psums, phand, cardcount # Allow the function to modify the variables.
  
  phand[shuffle[cardcount]] = f_count(shuffle[cardcount]) # Add card to the player's hand (dictionary). The card is the key, and its value is the value.
  cardcount += 1 # The next selected card will be the following card in the deck.
  pkey = list(phand.keys()) # List of the dictionary keys so they can be returned to the player.
  psums = sum(phand.values()) # Sum the values to check the total count of the hand.

def f_computerhand() : # Draw one card to the computer.
  global cardcount, csums, chand, ckey # Allow the function to modify variables. 

  chand[shuffle[cardcount]] = f_count(shuffle[cardcount]) # Set the card as the key and the count of the card as the value of a dictionary. 
  cardcount += 1 # The next selected card will be the following card in the deck.
  ckey = list(chand.keys()) # List of the keys of the dictionary so they can be read out.
  csums = sum(chand.values()) # Sum the values to check the total count of the hand.

def f_pacevalues() : # If the player exceeded 21, check if they have an ace that can be changed from 11 to 1 and replace it.
  global phand, psums # Allow the function to change these variables.
  if "Ace of Spades" in phand :
    phand["Ace of Spades"] = 1
  elif "Ace of Clubs" in phand :
    phand["Ace of Clubs"] = 1
  elif "Ace of Hearts" in phand :
    phand["Ace of Hearts"] = 1
  elif "Ace of Diamonds" in phand :
    phand["Ace of Diamonds"] = 1
  psums = sum(phand.values()) # Refresh the sum of the values.

def f_cacevalues() : # The same as f_pacevalues() but for the computer.
  global chand, csums 
  if "Ace of Spades" in chand :
    chand["Ace of Spades"] = 1
  elif "Ace of Clubs" in chand :
    chand["Ace of Clubs"] = 1
  elif "Ace of Hearts" in chand :
    chand["Ace of Hearts"] = 1
  elif "Ace of Diamonds" in chand :
    chand["Ace of Diamonds"] = 1
  csums = sum(chand.values())

def f_pstand() : 
  global done, pscore, cscore # Let function manipulate variables.
  while True : # Repeat until person wins / looses or stands.
    if psums == 21 : # If player wins increase the score.
      print("\nYou win!! You have 21 points!")
      pscore += 1
      done = 1 # Tell the program the result of the round has already been determined.
      break
    elif psums > 21 : # If player exceeds 21, check if they have an ace that can be reduced.
      f_pacevalues()
      if psums > 21 : # If player still exceeds 21, they loose. 
        print("\nComputer wins!! You exceeded 21 points!")
        cscore += 1
        done = 1 # Tell the program the result of the round has already been determined.
        break
    choice = input("\nStand or hit? ") # If player hasn't ended game already, let player stand or hit.
    sleep(0.5)
    if choice.lower() == "stand" :
      print("\nComputer's turn.")
      break
    elif choice.lower() == "hit" :
      f_playerhand() # Give card to player.
      print("\nYour cards are", pkey) # Read new hand to player.
  sleep(0.5) # Delay that makes reading outputs easier.

def f_cstand() :
  global done, cscore, pscore # Let function manipulate variables.
  while True :  
    if csums == 21 : # If computer reached 21, increase its score.
      print("\nComputer Wins!! It has 21 points!")
      cscore += 1
      done = 1 # Tell the program a result has already been reached.
      break
    elif csums > 21 :
      f_cacevalues() # Replace any aces that caused the computer to go over.
      if csums > 21 : # If computer still over, player wins.
        print("\nYou win! The computer exceeded 21 points! ")
        pscore += 1
        done = 1 # Tell progaram a result has already been reached.
        break
    if csums >= 17 :
      break # If computer has more than or equal to 17, don't pick anymore.
    elif csums < 17 :
      f_computerhand() # If computer has less than 17, pick a new card and tell the player the computer's new hand.
      print("\nComputer cards are", ckey)
      sleep(0.5) # Make reading the outputs easier.

def whowon() :
  global pscore, cscore
  com = 21 - csums # How far is the computer from 21.
  plr = 21 - psums # How far is the player from 21.
  if com < plr :
    print("\nComputer wins!! You're farther from 21.")
    cscore += 1 # If player is farther, computer wins.
  elif com > plr :
    print("\nYou win!! You're closer to 21.")
    pscore += 1 # If computer is farther, player wins.
  elif com == plr :
    print("\nIt's a tie!! You and the computer have the same number.") # It's a tie.
  sleep(0.5) # Reading output easier.

print("Instructions:\nThe goal of the game is to reach 21 points. It is a best of 5. Each card is worth it's number, except for the ace, and face cards. The ace is worth either 1 or 11, and the face cards are all worth 10. If anybody exceeds 21, the other player wins. If you hit 21 exactly, you win. At the start, both players get 2 cards. One of the computer's cards will be shown to you. If nobody has 21 points, you get the option to hit (get a new card), or stand (keep your current cards). Once you stand, it's the computer's turn. If it has 17 points or higher, it must stand, and if not, it must hit. If nobody reaches or exceeds 21, whoever's closer will win.") # Instructions.

while pscore < 3 and cscore < 3 : # Repeat until somebody reaches a score of three.
  
  cardcount = 0 # Reset variables for each round.
  done = 0
  phand = {}
  chand = {}
  
  shuffle = sample(l_deck, k = 52) # Shuffle deck for each round.

  print("\n\nNEW ROUND\n") # Clear formatting between rounds.

  sleep(0.5) # Make reading easier.
  
  while cardcount < 4 : # Deal first four cards.
    f_playerhand()
    f_computerhand()

  print("\nYour hand:", pkey[0], ",", pkey[1], "\nComputer's turned up card:", ckey[1]) # Print player hand, and one of the computer's cards.

  if psums == 21 : # Check if somebody won at the start of the game.
    print("\nYou win!! You have 21 points.") 
    done = 1 # Program knows a result has already been reached.
  elif csums == 21 :
    print('\nComputer wins!! It has 21 points.') 
    done = 1

  if done == 0 :
    f_pstand() # If no result has been reached, let player start picking cards.

  if done == 0 :
    f_cstand() # If no result has been reached, let computer start picking cards.

  if done == 0 :
    whowon() # If still no result has been reached, see who's closer to 21.

  print("\nYour hand:", pkey, "\nComputer's hand:", ckey) # Print out the final hands.
  
  print("\nYour score:", pscore, "Computer score:", cscore) # Print out the players' game scores.

if pscore == 3 : # Tell the player who won the game and end the program.
  print("\n\n\nYou won! You had", pscore, "points, and the computer had", cscore, "points.\n\n\n")
elif cscore == 3 :
  print("\n\n\nComputer won! You had", pscore, "points, and the computer had", cscore, "points.\n\n\n")
  