# importing required random module
import random
print("The Rules of Rock paper scissor game will be follows: 
"
+"Rock vs paper --> paper wins 
"
+"Rock vs scissor --> Rock wins 
"
+"paper vs scissor --> scissor wins 
")
while True:
print("Now please enter your choice no. 
 1. Rock 
 2. paper 
 3. scissor 
")
# take the input from user
ch = int(input("Now Your turn: "))
while ch> 3 or ch< 1:
   ch = int(input("Enter your valid input here: "))
if ch == 1:
   choice_name = 'Rock'
elifch == 2:
   choice_name = 'paper'
else:
   choice_name = 'scissor'
# print user given choice
   print("Your choice is: " + choice_name)
print("
Now its computer turn to initiate.......")
# Computer will select randomly any number
# among values 1, 2 and 3. Using randint method
# of random module
comp_choice = random.randint(1, 3)
# loopingwill continue until comp_choice value
# is equal to the choice value
while comp_choice == ch:
comp_choice = random.randint(1, 3)
# initialize value of the variable comp_choice_name
# variable corresponding to the choice value
if comp_choice == 1:
   comp_choice_name = 'Rock'
elifcomp_choice == 2:
   comp_choice_name = 'paper'
else:
   comp_choice_name = 'scissor'
   print("So computer choice is: " + comp_choice_name)
print(choice_name + " V/s " + comp_choice_name)
   # condition for winning the game
if((ch == 1 and comp_choice == 2) or
   (ch == 2 and comp_choice ==1 )):
print("paper wins => ", end = "")
   final_result = "paper"
elif((ch == 1 and comp_choice == 3) or
   (ch == 3 and comp_choice == 1)):
print("Rock wins =>", end = "")
   final_result = "Rock"
else:
   print("scissor wins =>", end = "")
   final_result = "scissor"
   # Printing either user or computer wins
if final_result == choice_name:
   print("<== You are the winner ==>")
else:
   print("<== Computer wins ==>")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
if ans == 'n' or ans == 'N':
   break
   # after exiting from the while loop
print("
Thanks for sharing time with us...")
