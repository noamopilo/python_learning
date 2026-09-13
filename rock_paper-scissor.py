from random import randint

while True:

  choice = input("Rock, paper, or scissors? (r/p/s): ").lower()

  if choice == "r":
   print('You choose ROCK') 
  elif choice == "p":
   print('You choose PAPER')
  elif choice == "s":
   print('You choose SCISSORS')
  else:
   print('Invalid choice!')
   continue

  number = randint(1,3)

  if number == 1:
   computer_choice = 'ROCK'
  elif number == 2:
   computer_choice = 'PAPER'
  elif number == 3:
   computer_choice = 'SCISSORS'

  print(f'Computer choose {computer_choice}')

  if choice == "r":
   if computer_choice == "ROCK":
    print("It's a tie!")
   elif computer_choice == "PAPER":
    print("You lose!")
   elif computer_choice == "SCISSORS":
    print("You win!")
  elif choice == "p":
   if computer_choice == "ROCK": 
    print("You win!")
   elif computer_choice == "PAPER":
    print("It's a tie!")
   elif computer_choice == "SCISSORS":
    print("You lose!")
  elif choice == "s":
   if computer_choice == "ROCK":
    print("You lose!")
   elif computer_choice == "PAPER":
    print("You win!")
   elif computer_choice == "SCISSORS":
    print("It's a tie!")

  if input("Continue? (y/n): ").lower() == "n":
    break 