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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
input1 = input(
    "You're at a crossroad. Where do you want to go(left or right)? ")
input1_lower = input1.lower()
if input1_lower == 'left':
    
    print("You've reached a lake and you see an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat OR 'swim' to swim across")
    input2 = input(" Do you want to wait for a boat or swim across?" )

    input2_lower = input2.lower()
    if input2_lower == 'wait':
        
        print("You have reached the Island safely.")
        print(" Now you see an old dilapidated house at a distance.")
        print("The house has 3 doors(Red,Yellow and Blue) to enter.")
        input3 = input("Which one will you choose? ")
        input3_lower=input3.lower()
        if input3_lower=='red':
          print("It's a room full of Fire. You get burnt.Game over")
        elif input3_lower=='blue':
          print("You get eaten by beasts. Game over")
        elif input3_lower=='yellow':
          print("You found the Treasure. You win!!!")
        else:
          print("Game over!!")
      
    elif input2_lower == 'swim':
      print("You got eaten over by Crocodiles.Game Over")
    else:
      print("Anything else. Game over!!")
elif input1_lower=='right':
  print("You fell into a hole. Game over")
else:
  print("Anything else.Game over")






