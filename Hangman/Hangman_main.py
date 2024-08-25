# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
length_of_chword = len(chosen_word)
# for a in range(0,length_of_chword):


word_in_progress = length_of_chword * "_"
word_in_progress = list(word_in_progress)
print(''.join(word_in_progress))



guess = input("Guess a letter: ").lower()

for i in range(length_of_chword):
    if guess == chosen_word[i]:
        word_in_progress[i] = guess
print(''.join(word_in_progress))

guess = input("Guess a letter: ").lower()

for i in range(length_of_chword):
    if guess == chosen_word[i]:
        word_in_progress[i] = guess
print(''.join(word_in_progress))


guess = input("Guess a letter: ").lower()

for i in range(length_of_chword):
    if guess == chosen_word[i]:
        word_in_progress[i] = guess
print(''.join(word_in_progress))


