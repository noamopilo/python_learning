from random import randint

rolls = 0

while True:
    response = input("Roll the dice? (y/n)").lower()

    if response == "y":
     random_number1 = randint(1, 6)
     random_number2 = randint(1, 6)
     print(random_number1,", ",random_number2)
     rolls += 1
    elif response == "n":
     print("Thanks for playing!")
     print("You rolled the dice", rolls, "times.")
     exit()
    else: 
     print("Invalid choice!")
     