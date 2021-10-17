'''
  ____            _        ____                         ____       _                        
 |  _ \ ___   ___| | __   |  _ \ __ _ _ __   ___ _ __  / ___|  ___(_)___ ___  ___  _ __ ___ 
 | |_) / _ \ / __| |/ /   | |_) / _` | '_ \ / _ \ '__| \___ \ / __| / __/ __|/ _ \| '__/ __|
 |  _ < (_) | (__|   < _  |  __/ (_| | |_) |  __/ |_    ___) | (__| \__ \__ \ (_) | |  \__ \
 |_| \_\___/ \___|_|\_( ) |_|   \__,_| .__/ \___|_( )  |____/ \___|_|___/___/\___/|_|  |___/
                      |/             |_|          |/                                        


'''
'''
Battle against computer: Rock, Paper, Scissors.

Everytime you win, you have a chance to select an action:
Heal, Defend, Strike, Sabotage

Strike = Deals 1 HP damage
Heal = Recovers 1 HP
Defend = Guard against opponent's next strike
Sabotage = The next time opponent wins, that opponent has 33% chance of failing to perform the action. If the action failed, opponent lose 1 HP.

Everytime you win 5 times, your next action will be upgraded to Power versions:

Power Strike = Deals 3 HP damage
Power Heal = Recovers 3 HP
Power Defend = Guard against opponent's next two strikes
Power Sabotage = The next time opponent wins, that opponent has 50% chance of failing to perform the action. If the action failed, the opponent lose 1 HP for 2 turns.

The first time your HP is reduced down to 1, your next action will be upgraded to Desperate versions:

Desperate Strike = Deals 2 HP damage and recovers 2 HP
Desperate Heal = Recovers 2 HP for two turns.
Desperate Defend = Guard against opponent's next strike, and counters the enemy with 1 HP damage.
Desperate Sabotage = The next time opponent wins, that opponent has 66% chance of failing to perform the action. If the action failed, opponent's HP will be reduced to 1.

You and your opponent starts with 5 HP.

'''

#######################################
#               MODULES               #
#######################################

import random

class Choose:

  def __init__(self,name,win,lose,article=""):
    self.name = name
    self.win = win
    self.lose = lose
    self.article = article

rock = Choose("rock","scissors","paper","a ")
paper = Choose("paper","rock","scissors","a ")
scissors = Choose("scissors","paper","rock")

# Simple rock, paper, scissors game
choose = ["rock", "paper", "scissors"]

def instruction():
  det = "Please choose one of the following (enter the option number): \n"
  opt1 = "1. Rock \n"
  opt2 = "2. Paper \n"
  opt3 = "3. Scissors \n"
  
  instruction = "{} {} {} {}".format(det, opt1, opt2, opt3)
  return instruction

def player_choose():
  player_choose = int(input(instruction()))
  player_choose = choose[player_choose]
  return player_choose

def ai_choose():
  ai_choose = random.choice(choose)
  return ai_choose

def game():
  player_choice = player_choose()
  ai_choice = ai_choose()
  player_score = 0
  ai_score = 0
  player_result = ""

  if eval(player_choice).win == ai_choice:
    player_score += 1
    player_result = "You won!"
  elif eval(player_choice).lose == ai_choice:
    ai_score += 1
    player_result = "You lost!"
  else:
    player_result = "It's a tie!"

  player_article = eval(player_choice).article
  ai_article = eval(ai_choice).article
  player_choice_name = eval(player_choice).name
  ai_choice_name = eval(ai_choice).name

  result = "You throw {}{} while AI throws {}{}. {}".format(
           player_article,player_choice_name,ai_article,ai_choice_name,player_result
           )
  return result

print(game())
  



  # player_win = None
  # player_article = None
  # ai_article = None
  # result = ""

  # if player == "rock":
  #   if ai == "scissors":
  #     player_score += 1
  #     player_win = True
  #   else:
  #     ai_score += 1
  # elif player == "paper":
  #   if ai == "rock":
  #     player_score += 1
  #     player_win = True
  #   else:
  #     ai_score += 1
  # elif player == "scissors"
  #   if ai == "paper":
  #     player_score += 1
  #     player_win = True
  #   else:
  #     ai_score += 1
  
  # result = "You threw {} {} while AI threw {} {}".format()

  # if player_win = True:
  #   result = "You "


  # return player_score, ai_score
  





  






































### TRASH CODES

### TRASH 1
# choose_options = ["rock", "paper", "scissors"]
# player_turn = ""

# # Classes
# class Player():

#     def __init__(self,hp):
#       self.hp = hp

#     def chosen(self,choose):
#       self.choose = choose

# # Create players

# player = Player(10)
# ai = Player(10)

# # Game




# def choose():
#   if player_turn == "player":
#     info_0 = "Please choose one of the following (enter the option no.):"
#     info_1 = "1. Rock"
#     info_2 = "2. Paper"
#     info_3 = "3. Scissors"
#     nl = "\n"
#     choose = ""

#     player_choose = input(info_0 + nl + info_1 + nl + info_2 + nl + info_3 + nl)

#     if player_choose == 1:
#       choose = "rock"
#     elif player_choose == 2:
#       choose = "paper"
#     elif player_choose == 3:
#       choose = "scissors"
#     else:




