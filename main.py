print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Flow chart -https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
# Plan
# Ask the user if they want to go left or right and store in a varaible [done]
  # Ensure users answer is not case sensitive and create a variable[done]
# if the user selects right then the user falls in a hole Game Over or any other input if the user selects left then move onto the next stage of game 
# Ask user if they want to swim or wait and store in variable
  # Ensure users answer is not case sensitive
# if answer is swim then user is attacked by trout Game Over and if wait move onto next stage of the game
# Ask the user to choose a door and store in a varaible 
  # Ensure users answer is not case sensitive
# if user chooses Blue Eaten by beasts Game Over . if the user chooses red Burned by fire Game Over . If user chooses Yellow then they win . Any Other answer would result in game over  
direction = input("You're at a crossroad. Where do you want to go? Type left or Type right:\n").lower()

if direction  == "left":
   direction_answer = input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across:\n").lower()
else:
   print("You Fall into a hole . Game Over!\n")
if direction_answer == 'wait':
  boat_answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose:\n").lower();     
else:
  print("Attacked by a mysterious beast that inhabits the lake. Game over")      
if boat_answer == 'yellow':
   print("Congratualtions you chose the correct door. The Treasure is in this room, you win!!") 
elif boat_answer == 'red':
  print("You are burned by fire. Game Over ")
elif boat_answer == 'blue':
  print("You are Eaten by beasts. Game Over ")
else:
  print("Invalid Answer Game over")
