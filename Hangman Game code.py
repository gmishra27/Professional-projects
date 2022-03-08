#Step 5
from replit import clear
import random
import hangman_words as HW
import hangman_art as HA

chosen_word = random.choice(HW.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(HA.logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        
        
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        
        print(f"You guessed {guess}, this is not in the word, You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The correct answer is {chosen_word}")

    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(HA.stages[lives])