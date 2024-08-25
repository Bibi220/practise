# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = ""
placeholder = ""
guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
length_of_chword = len(chosen_word)
# for a in range(0,length_of_chword):
# placeholder = length_of_chword * "_"
# print(placeholder)
for b in range(length_of_chword):
    placeholder += "_"
print(placeholder)

for i in range(length_of_chword):
    if guess == chosen_word[i]:
        placeholder[i] = guess
print(placeholder)










