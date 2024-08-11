
import random

def print_blanks(length: int):
    print("_" * length)

def word_has_letter(word: str, char: chr) -> bool:
    for a in word:
        if a == char:
            return True
    return False


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print_blanks(len(chosen_word))

guess_line = input("Guess a letter: ").lower()
guess = guess_line[0]

print(word_has_letter(chosen_word, guess))


