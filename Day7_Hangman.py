# My_Logic 
word_list = ["cattle","buffalo","camel","honeybee","Goose",'turkey','rabbit','donkey']

import random
chosen_word = random.choice(word_list)
display = []
words_len = len(chosen_word)
print(f'Testing, the solution is {chosen_word}.')

for _ in range(words_len):
	display += "_"

print(display)

guess = input("Guess a letter : ").lower()

for position in range(words_len):
	letter = chosen_word[position]
	if guess == letter:
		display[position] = letter
	

print(display)

'''

# Mentor's Logic
#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for letter in chosen_word:
    if letter == guess:
        display.append(guess)
    else:
    	display.append('_')

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
'''