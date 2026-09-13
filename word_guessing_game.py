import random

hangman = [
    """
    -----
      ;   
      
     
      
     
    _____
    """,
    """
    -----
      ;   
      O
     
      
     
    _____
    """,
    """
    -----
      ;   
      O
      |
      |
     
    _____
    """,
    """
    -----
      ;   
      O
     /|
      |
     
    _____
    """,
    """
    -----
      ;   
      O
     /|\\
      |
     
    _____
    """,
    """
    -----
      ;   
      O
     /|\\
      |
     / 
    _____
    """,
    """
    -----
      ;   
      O
     /|\\
      |
     / \\
    _____
    """
]

hangman.reverse()

word_bank_easy = ["chat", "chien", "papa", "maman", "ami",
    "eau", "pain", "lait", "pomme",
    "soleil", "lune", "arbre", "fleur"]

word_bank_difficult = ["aventure", "mystere", "voyage", "histoire",
    "liberte", "courage", "silence", "danger",
    "bonheur", "tristesse"]

word_bank_mix = ["aventure", "mystere", "voyage", "histoire",
    "liberte", "courage", "silence", "danger",
    "bonheur", "tristesse", "chat", "chien", "papa", "maman", "ami",
    "eau", "pain", "lait", "pomme",
    "soleil", "lune", "arbre", "fleur"]


def play_game():
    answer = input('Wich level do you want to play?(Easy(E) or Difficult(D) or Mix(M))?: ')

    if answer == "E":
     word = random.choice(word_bank_easy)
    elif answer == "D":
      word = random.choice(word_bank_difficult)
    elif answer == "M":
     word = random.choice(word_bank_mix)
    else:
     input('Please enter a valid letter. Wich level do you want to play?(Easy(E) or Difficult(D) or Mix(M))?: ')

    print('The word is in French!')

    guessword = ['_'] * len(word)

    attempts = len(hangman) - 1
    wrong = 0

    while attempts > 0:
        print('\n' + hangman[wrong])
        print('\nCurrent word: '+' '.join(guessword))
        guess = input('Enter a letter: ').lower()
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                 guessword[i] = guess
                 print('Great guess!')
        else:
             attempts -= 1
             wrong += 1
             print('Wrong guess! Attempt left: ' + str(attempts))
    
        if '_' not in guessword:
             print('\nCongratulations!! You guessed the word: ' + word)
             break
        
        
    
    if  attempts == 0 and '_' in guessword:
        print('\nYou\'ve run out of attempts! The word was: ' + word)
        print(hangman[6])
        
while True:
    play_game()
    
    restart = input('\nDou you want to restart?(Y/N): ').strip().upper()
    if restart != 'Y':
        print('Thanks for playing!')
        break