#Hangman game 
import random
from Hangman_art import logo,stages
from Hangman_words import word_dict
           
def main():
   #LOGO
    print(logo)
    print('*'*40)

    choosen_word=random.choice(list(word_dict.keys()))
    lives=6
    stage=6
    guessed_letters = set()
    print(f'HINT ----> {choosen_word}')
    print('*'*40)

    temp_word=list('_'*len(word_dict[choosen_word]))
    print(f'Word to guess has {len(word_dict[choosen_word])} letters: {"".join(temp_word)}')


    while lives>0 and "".join(temp_word)!=word_dict[choosen_word]:
        print(f' {'*'*40} Lives left: {lives} {'*'*40}')

        guess=input('Guess a letter -->  ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)

        if guess in word_dict[choosen_word]:
            for index,value in enumerate(word_dict[choosen_word]):
                if value == guess:
                    temp_word[index]=guess
            print("Current word:", " ".join(temp_word))
        else:
            lives-=1
            stage-=1
            print(stages[stage])

    if lives == 0:
        print('Better luck next time !!!')
    else:
        print('Congrats u won!')

if __name__ == "__main__":
    main()