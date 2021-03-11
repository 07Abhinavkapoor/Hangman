import random
from words import words
import playsound
import string
import _thread
import time


def get_word(words):
    """
    To get a word at random from the list of words.

    Parameters:
    words(list): list of words from which a word is to be selected.

    Returns:
    string: the selected word in upper case.
    """
    word = random.choice(words)
    word = word.replace("-", "/")
    return word.upper()


def play_sound(argument_to_thread):
    """
    To play the sound in a new thread.

    Parameters:
    argument_to_thread(string): A string specifying the path to the sound which is to played.

    Returns: None
    """
    _thread.start_new_thread(playsound.playsound, argument_to_thread)


def correct_guess():
    """
    To play a sound when the user's guess is correct.

    Parameters: None

    Returns None
    """
    argument_to_thread = ("sounds/correct_guess.wav", )
    # Since the second argument is required to be a tuple
    play_sound(argument_to_thread)


def wrong_guess():
    """
    To play a sound when the user's guess is incorrect.

    Parameters: None

    Returns: None
    """
    argument_to_thread = ("sounds/wrong_guess.mp3", )
    play_sound(argument_to_thread)


def all_lives_over():
    """
    To play a sound when no lives are left.

    Parameters: None

    Returns: None
    """
    argument_to_thread = ("sounds/life_over.wav", )
    play_sound(argument_to_thread)


def winner():
    """
    To play a sound when the user successfull guess the whole word.

    Parameters: None

    Returns: None
    """
    argument_to_thread = ("sounds/win.wav", )
    play_sound(argument_to_thread)


def stats(used_letters, lives):
    """
    To print the number of lives left and the letters which have already been guessed.

    Parametes:
    used_letters(set): The letters which are already guessed.
    lives(int): The number of lives remaining.

    Returns: None
    """
    print(f"You have {lives} life left.")
    print("Guessed Letters: ", " ".join(used_letters))


def play():
    """
    The main game.

    A word is fetched from the list of words and the user has to guess the word.

    Parameters: None

    Returns: None
    """
    word = get_word(words)
    lives = 6

    word_letters = set(word)  # To keep track of unguessed letters
    used_letters = set()  # To keep track of guessed letters
    valid_letters = set(string.ascii_uppercase)

    while len(word_letters) > 0 and lives > 0:
        stats(used_letters, lives)

        display_letters = [
            letter if letter in used_letters or letter == "/" else "-" for letter in word]
        print("\t"*2, " ".join(display_letters))

        user_input = input("Enter a character: ").upper()

        if user_input in valid_letters - used_letters:
            used_letters.add(user_input)

            if user_input in word_letters:
                correct_guess()
                word_letters.remove(user_input)
            else:
                wrong_guess()
                lives = lives - 1
                print(f"{user_input} in not in the word.")
                if(lives > 0):
                    print("Try Again")

        elif user_input in used_letters:
            wrong_guess()
            print("Letter is already guessed")

        else:
            wrong_guess()
            print("Enter a valid character")

        print("\n"*3)

    # while loop ends here. It ends when either the user guesses the word correctly
    # or loses all the lives.

    if lives == 0:
        all_lives_over()
        print(f"All Lives Over. You Lost. The word was {word}.")
        time.sleep(1)
    else:
        winner()
        print(f"Congratulations. You guessed {word} right")
        time.sleep(1)


if __name__ == "__main__":
    play()
