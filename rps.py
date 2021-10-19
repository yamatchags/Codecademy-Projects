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
'''
ROADMAP:

1. Enable actions
'''

#######################################
#              MODULES                #
#######################################

import random


#######################################
#              CLASSES                #
#######################################

class Choose:

  def __init__(self,name,win,lose,article=""):
    self.name = name
    self.win = win
    self.lose = lose
    self.article = article

class Player:

  def __init__(self,name,hp=10):
    self.name = name
    self.hp = hp
    self.win = 0
    self.lost = 0
    self.stage = 0
    self.power_actions = False
    self.desperate_actions = False
  
  def __add__(self,value):
    self.win += value

  def __sub__(self,value):
    self.lost += value

  # The history contains all information about what the player had picked.
  # For choose history, 0 : [0,1,0] means that the player has battled 3 
  # different contenders, where player had picked 2 rocks, and 1 paper for 
  # the starting choice.
  # For action history, 0: [0,1,0] means that the player didn't win the first 
  # round for the first and third battle. However, the player won the first 
  # round in the second battle, and has chosen strike for the first action.
  # def choose_history(self,choose):
  #   self.choose = choose
  #   choose_history
  #   return choose_history

  # def action_history(self,action):
  #   self.action = action

  #   return action_history

class Bot(Player):

  def __init__(self,name,hp=10):
    super().__init__(name,hp)

#######################################
#            INITIALIZE               #
#######################################

rock = Choose("rock","scissors","paper","a ")
paper = Choose("paper","rock","scissors","a ")
scissors = Choose("scissors","paper","rock")

# Simple rock, paper, scissors game
choose = ["rock", "paper", "scissors"]
action = ["strike", "heal", "guard", "sabotage"]
# choose_history = {}
# action_history = {}






#######################################
#         UTILITY FUNCTIONS           #
#######################################

def pause():
  pause = "(Press Enter to continue...)\n"
  return input(pause)

# This function exits the game
def exit_game():
  invalid_input = True

  while invalid_input == True:
    user_input = input("Are you sure you want to exit? (Y/N):  ")
    if user_input.strip().upper() == "Y":
      print("You walked away and forfeited the game.")
      invalid_input = False
      exit()
    elif user_input.strip().upper() == "N":
      print()
      invalid_input = False
    else:
      print("Please select Y (yes) or N (no)!")

def continue_game():
  invalid_input = True

  while invalid_input == True:
    user_input = input("Would you like to continue? (Y/N):  ")
    if user_input.strip().upper() == "Y":
      invalid_input = False
      game()
    elif user_input.strip().upper() == "N":
      invalid_input = False
      exit()
    else:
      print("Please select Y (yes) or N (no)!")


#######################################
#         IN-GAME FUNCTIONS           #
#######################################

# Inquires user to input their name
def player_name():
  player_name = input("What is your name? (40 characters max): \n")
  return player_name

def instruction():
  header = "Please choose one of the following:\n"
  opt1 = "1. Rock\n"
  opt2 = "2. Paper\n"
  opt3 = "3. Scissors\n"
  opt0 = "0. Exit\n"
  
  instruction = "{} {} {} {} {}".format(header, opt1, opt2, opt3, opt0)
  return instruction

def player_choose():
  invalid_input = True
  player_choose = None
  border = "================================================="
  print(border + "\n" + instruction())

  while invalid_input == True:
    try:
      player_choose = int(input("Option No.:  "))
    except:
      print("Please select the correct option (1, 2, 3, or 0 to exit)!\n")
    else:
      if player_choose == 0:
        exit_game()
      elif 1 <= player_choose <= 3:
        player_choose = int(player_choose)
        player_choose = choose[player_choose-1]
        invalid_input = False
        return player_choose
      else:
        print("Please select the correct option (1, 2, 3, or 0 to exit)!\n")

def ai_choose():
  ai_choose = random.choice(choose)
  return ai_choose

def ai_profile():
  if player.stage == 0:
    return [emily.hp, emily.name]
  elif player.stage == 1:
    return [leo.hp, leo.name]
  elif player.stage == 2:
    return [blitz.hp, blitz.name]
  else:
    return [sayaka.hp, sayaka.name]

def ai_introduction():
  ai_name = ai_profile()[1]

  if ai_name == "Emily":
    intro1 = "Emily: Hello and nice to meet you, {}!".format(player.name)
    intro2 = "Emily: Shall we begin?"
    print(intro1) ; pause()
    print(intro2) ; pause()

def game():
  # global choose_history
  # global action_history
  player_stage = player.stage
  player_hp = player.hp
  ai_hp, ai_name = ai_profile()[0], ai_profile()[1]
  player_score = 0
  ai_score = 0

  print()
  ai_introduction()

  while player_hp > 0 and ai_hp > 0:
    player_choice = player_choose()
    ai_choice = ai_choose()
    player_result = ""
    game_round = 0

    if eval(player_choice).win == ai_choice:
      player_score += 1
      ai_hp -= 1
      player_result = "You won!"
    elif eval(player_choice).lose == ai_choice:
      ai_score += 1
      player_hp -= 1
      player_result = "You lost!"
    else:
      player_result = "It's a tie!"
    game_round += 1

    player_article = eval(player_choice).article
    ai_article = eval(ai_choice).article
    player_choice_name = eval(player_choice).name
    ai_choice_name = eval(ai_choice).name

    result = "\nYou throw {}{} while {} throws {}{}. {}".format(
            player_article,player_choice_name,ai_name,ai_article,ai_choice_name,player_result
            )
    stats = "\n{}'s HP: {} \n{}'s HP: {}\n".format(player.name,player_hp,ai_name,ai_hp)
    border = "----------------------------------------"
    print(result)
    print("\n" + border + stats + border + "\n")
    pause()
  
  if player_hp > 0 and ai_hp <= 0:
    player.win += 1
    player.stage += 1
    print("You've won the game!")
  elif player_hp <= 0 and ai_hp > 0:
    player.lost += 1
    print("You've lost the game...")
  else:
    print("It's a draw...")
  
  continue_game()


#######################################
#         INITIALIZE PLAYERS          #
#######################################


player = Player(player_name(),3)
emily = Bot("Emily",3)
leo = Bot("Leo")
blitz = Bot("Blitz")
sayaka = Bot("Sayaka")


game()


  






































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




