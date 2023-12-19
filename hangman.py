import random, os

def printImg(imagenum):
    if imagenum == 6:
        print('''
                 ________________________________________________
                |                                                |
                |                                                |
                |                                                |
                |                                                |   
                |                   Welcome to                   |
                |                                                |
                |                    HANGMAN!                    |
                |                                                |   
                |                                                |
                |                                                |       
                |________________________________________________|
                \n\n''')
    elif imagenum == 5:
        print('''
                 ________________________________________________
                |                                                |
                |           |                                    |
                |           |                                    |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')
    elif imagenum == 4:
        print('''
                 ________________________________________________
                |           _______________                      |
                |           | /                                  |
                |           |/                                   |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')
    elif imagenum == 3:
        print('''
                 ________________________________________________
                |           _______________                      |
                |           | /           |                      |
                |           |/            |                      |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')
    elif imagenum == 2:
        print('''
                 ________________________________________________
                |           _______________                      |
                |           | /           |                      |
                |           |/           _|_                     |
                |           |           /* *\                    |
                |           |           \___/                    |   
                |           |                                    |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')
    elif imagenum == 1:
        print('''
                 ________________________________________________
                |           _______________                      |
                |           | /           |                      |
                |           |/           _|_                     |
                |           |           /* *\                    |
                |           |           \___/                    |   
                |           |          \__|__/                   |
                |           |                                    |
                |           |                                    |   
                |           |                                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')
    elif imagenum == 0:
        print('''
                 ________________________________________________
                |           _______________                      |
                |           | /           |                      |
                |           |/           _|_                     |
                |           |           /x x\     YOU LOST       |
                |           |           \___/     YOU LOST       |   
                |           |          \__|__/    YOU LOST       |
                |           |             |       YOU LOST       |
                |           |            / \      YOU LOST...    |   
                |           |           /   \                    |
                |      _____|_____                               |       
                |_____/___________\______________________________|
                \n\n''')

def clear_terminal():
    # Check the system platform
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Mac and Linux
        _ = os.system('clear')

def choose_doc():
    docs = os.listdir("wordlists")

    wordlists = []

    for doc in docs:
        suffix = doc.split(sep = ".")
        if suffix[1] == "txt":
            wordlists.append(doc)
    
    print(f"Choose a list of words to use from the ones below!")
    for i in range(len(wordlists)):
        print(f"({i}): {wordlists[i]}")
    index = int(input("Enter the index of the list you want to use: "))
    return wordlists[index]

def getWord():
    chosen_doc = choose_doc()
    with open(f"wordlists/{chosen_doc}") as word_table:
        words = word_table.read().lower().split()
    wordstring = random.choice(words)
    word = [x for x in wordstring]
    # print(wordstring, word)
    return word, wordstring

def main():
    wordforms = getWord()
    word, wordstring = wordforms[0], wordforms[1]
    hidden_word = []
    guessed_letters = []
    missing_letters = len(word)

    clear_terminal()
    printImg(6)

    for i in range(len(word)):
        hidden_word.append("_")
    
    attempts = 5
    while attempts > 0:
        alreadyGuessed = False
        letterInWord = False
        positions = []

        if missing_letters == 0:
            print("Congratulations! You won!")
            print(f"The word was {wordstring.capitalize()}")
            break

        if attempts != 5:
            printImg(attempts)

        if len(guessed_letters) > 0:
            print(f"Guesses: {guessed_letters}")

        print(hidden_word, "\n")

        guess = input(f"You have {attempts} attempts left. Guess here: ").lower()

        clear_terminal()

        if attempts == 5:
            printImg(attempts)

        if len(guess) > 1:
            guess_list = [x for x in guess]
            if guess_list == word:
                missing_letters = 0
            else:
                print("Wrong guess!")
                attempts -= 1
            guessed_letters.append(guess)
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    letterInWord = True
                    positions.append(i)

            if letterInWord == True:
                print("Correct guess!")
                for position in positions:
                    hidden_word[position] = guess.capitalize()
                    letterInWord = False
            else:
                print("Wrong guess!")
                attempts -= 1

        for i in range(len(guessed_letters)):
            if guess.capitalize() == guessed_letters[i]:
                alreadyGuessed = True
                print(f"You already guessed {guess.capitalize()}")

        if alreadyGuessed == False:
            guessed_letters.append(guess.capitalize())
            missing_letters -= len(positions)
        
        # print(hidden_word, "\n")
    
    if attempts == 0:
        printImg(attempts)
        print("You lost! You ran out of attempts!")
        print(f"The word was {wordstring.capitalize()}")



if __name__ == "__main__":
    main()