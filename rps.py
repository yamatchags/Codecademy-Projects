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
power_action = ["power strike", "power heal", "power guard", "power sabotage"]
desperate_action = ["desperate strike", "desperate heal", "desperate guard", "desperate sabotage"]
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

def instruction_choose():
  header = "Please choose one of the following:\n"
  opt1 = "1. Rock\n"
  opt2 = "2. Paper\n"
  opt3 = "3. Scissors\n"
  opt0 = "0. Exit\n"
  
  instruction_choose = "{} {} {} {} {}".format(header, opt1, opt2, opt3, opt0)
  return instruction_choose

def instruction_action():
  header = "Please choose one of the following:\n"
  opt1 = "1. Strike\n"
  opt2 = "2. Heal\n"
  opt3 = "3. Guard\n"
  opt4 = "4. Sabotage\n"
  opt0 = "0. Help on Actions\n"

  instruction_action = "{} {} {} {} {} {}".format(header, opt1, opt2, opt3, opt4, opt0)
  return instruction_action

def instruction_power_action():
  header = "Please choose one of the following:\n"
  opt1 = "1. Power Strike\n"
  opt2 = "2. Power Heal\n"
  opt3 = "3. Power Guard\n"
  opt4 = "4. Power Sabotage\n"
  opt0 = "0. Help on Power Actions\n"

  instruction_power_action = "{} {} {} {} {} {}".format(header, opt1, opt2, opt3, opt4, opt0)
  return instruction_power_action

def instruction_desperate_action():
  header = "Please choose one of the following:\n"
  opt1 = "1. Desperate Strike\n"
  opt2 = "2. Desperate Heal\n"
  opt3 = "3. Desperate Guard\n"
  opt4 = "4. Desperate Sabotage\n"
  opt0 = "0. Help on Depserate Actions\n"

  instruction_desperate_action = "{} {} {} {} {} {}".format(header, opt1, opt2, opt3, opt4, opt0)
  return instruction_desperate_action

def player_choose():
  invalid_input = True
  player_choose = None
  border = "================================================="
  print(border + "\n" + instruction_choose())

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

def player_action():
  invalid_input = True
  player_action = None
  border = "================================================="
  print(border + "\n" + instruction_action())

  while invalid_input == True:
    try:
      player_action = int(input("Action No.:  "))
    except:
      print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")
    else:
      if player_action == 0:
        help01 = "1. Strike reduces opponent's HP by 1.\n"
        help02 = "2. Heal restores own HP by 1.\n"
        help03 = "3. Guard has a 50%\ chance of nullifying opponent's \
          next strike. If the guard is successful, a counter will be \
            performed, which reduces opponent's HP by 1. Overwrites any existing Guard stance.\n"
        help04 = "4. Sabotage has a 33%\ chance of failing oppponent's next action. \
          If the action failed, opponent loses 1 HP as well as any Guard stance. \
            Overwrites any existing pending sabotage on opponent."
        help_action = "{} {} {} {}".format(help01,help02,help03,help04)
      elif 1 <= player_action <= 4:
        player_action = int(player_action)
        player_action = action[player_action-1]
        invalid_input = False
        return player_action
      else:
        print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")

def player_power_action():
  invalid_input = True
  player_action = None
  border = "================================================="
  print(border + "\n" + instruction_power_action())

  while invalid_input == True:
    try:
      player_action = int(input("Action No.:  "))
    except:
      print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")
    else:
      if player_action == 0:
        help01 = "1. Power Strike reduces opponent's HP by 2.\n"
        help02 = "2. Power Heal restores own HP by 2.\n"
        help03 = "3. Power Guard has a 80%\ chance of nullifying opponent's \
          next strike and a counter will be performed, which reduces opponent's \
            HP by 1. Overwrites any existing Guard stance.\n"
        help04 = "4. Power Sabotage has a 66%\ chance of failing oppponent's next action. \
          If the action failed, opponent loses 2 HP as well as any Guard \
          stance. Overwrites any existing pending sabotage on opponent.\n"
        help_action = "{} {} {} {}".format(help01,help02,help03,help04)
      elif 1 <= player_action <= 4:
        player_action = int(player_action)
        player_action = action[player_action-1]
        invalid_input = False
        return player_action
      else:
        print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")

def player_desperate_action():
  invalid_input = True
  player_action = None
  border = "================================================="
  print(border + "\n" + instruction_desperate_action())

  while invalid_input == True:
    try:
      player_action = int(input("Action No.:  "))
    except:
      print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")
    else:
      if player_action == 0:
        help01 = "1. Desperate Strike reduces opponent's HP by 1 and recovers own HP by 1.\n"
        help02 = "2. Desperate Heal restores own HP by 3, but reduces own HP by 1 for the \
          next 2 turns.\n"
        help03 = "3. Desperate Guard nullifies opponent's next strike. If the \
          guard is successful, a counter strike will be performed, which \
          reduces opponent's HP by 1. Overwrites any existing Guard stance.\n"
        help04 = "4. Desperate Sabotage has a 25%\ chance of failing oppponent's next action. \
          If the action failed, opponent loses all HP but 1 as well as any Guard \
          stance.\n"
        help_action = "{} {} {} {}".format(help01,help02,help03,help04)
      elif 1 <= player_action <= 4:
        player_action = int(player_action)
        player_action = action[player_action-1]
        invalid_input = False
        return player_action
      else:
        print("Please select the correct action (1, 2, 3, 4, or 0 for help)!\n")

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
  ai_hp = ai_profile()[0]
  ai_name = ai_profile()[1]
  player_score = 0
  ai_score = 0
  player_power_actions = False
  ai_power_actions = False
  player_desperate_actions = False
  ai_desperate_actions = False
  player_power_actions_count = 0
  ai_power_actions_count = 0
  player_desperate_actions_count = 0
  ai_desperate_actions_count = 0

  print()
  ai_introduction()

  while player_hp > 0 and ai_hp > 0:

    if player_score % 5 == 0:
      player_power_actions = True
    elif player_hp <= 2:
      player_desperate_actions = True 
    if ai_score % 5 == 0:
      ai_power_actions = True
    elif ai_hp <= 2:
      ai_desperate_actions = True
    
    player_choice = player_choose()
    ai_choice = ai_choose()
    player_result = ""
    game_round = 0

    if eval(player_choice).win == ai_choice:
      player_score += 1
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




