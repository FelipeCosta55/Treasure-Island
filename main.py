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

print("Welcome to Treasure Island. You entered a pirate's zone to find their treasure. Use you intuition to find it!")
print("")
print("")

first_choice = input("There is a fork in front of you. Do you choose to go to the RIGHT or LEFT path?\n")

if first_choice.lower() == "left":
  second_coice = input("It seems to be the right one. You found a big river. Do you choose to SWIM agains the flow to reach the border or WAIT for something to happen?\n")

  if second_coice.lower() == "wait":
    third_choice = input("A log came down the river and you used it to move. You find a mysterios temple with 3 doors: RED, YELLOW AND BLUE. Wich one do you choose?\n")
    
    if third_choice.lower() == "yellow":
      print("Yellow reminded you of gold color. It was the right door! You found the treasure! Congratulations!")
    elif third_choice.lower() == "red":
      print("Red is the color of... fire. You got into a fire trap. Game Over.")
    elif third_choice.lower() == "blue":
      print("You entered a dark room in wich there are dozens of beast inside. Game over.")
    else:
      print("Take a real decision next time. Game over.")
    
  else:
      print("You are in a tropical island! Didn't you think about the crocodiles? Game Over")
  
else:
    print("You stepped into a trap. Game Over")