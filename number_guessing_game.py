from random import randint

number = randint(1,100)
answer = input('Guess the number between 1 and 100: ')

while True:
    if answer.isdigit():
        if int(answer) < number:
            print('Too low!')
        elif int(answer) > number:
            print('Too high!')
        else:
            print('Congratulations you guessed the number!')
            print(f'The number was: {number}')
            break
    else:
        print('Please enter a valid number')
