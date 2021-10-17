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

choose = ["rock", "paper", "scissors"]


# Classes
class Player():

    def __init__(self,hp):
      self.hp = hp

    def chosen(self,choose):
      self.choose = choose

# Create players

player = Player(10)
print(player.hp)

