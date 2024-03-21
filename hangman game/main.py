import random
from words import word_list

selected_word = random.choice(word_list)
word_length = len(selected_word)

end_of_game = False
lives = 6

from hangman import logo,stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess the Letter: ").lower()

    if  guess in display:
        print(f"You  have already guessed {guess}")


    for postion in range(word_length):
        letter = selected_word[postion]

        if letter == guess:
            display[postion] = letter

    if guess not in selected_word:
        print(f"you guessed {guess}that not in the word list. you lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True  
            print("sorry you lost")

    print(f"{''.join(display)}") 

    if "_" not in display:
        end_of_game = True
        print("you saved the man")

    from hangman import stages
    print(stages[lives])                       

