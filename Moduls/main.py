from random import randrange
from Hangman_filter import list_words, get_url
from Validator import Validator

#### GETTING WORD TO GUESS ####
print("""\nSelect Category:\n
   1 - Days of the week
   2 - Months of the year
   3 - Animals
   4 - The Whole words
   5 - Words from my .txt file: (Copy-Paste a .txt files URL\n""")

menu = Validator.intoptions("Category: ", "Please select a number from 1 to 4 only",range(1,6))
if menu in range(1,5):
    file = get_url(menu)
elif menu == 5:
    good_url = Validator.url()
    file = list_words(good_url, "Users_Words.txt")

print(f"\nYou Selected {file.replace('_',' ', ).replace('.txt', ' Category')}!!!")
print("-"*36)
words_list = open(file,"r")
words = words_list.read()
words_list.close()

words = words.split()
index = randrange(len(words))

word = words[index]
cleaned_word = {
    ord(",",):None,
    ord("'",):None,
    ord("["):None,
    ord("]"):None}
word = word.translate(cleaned_word)

#### GAME STARS!!! ####
attempts = 5

print (f"Guess this word!!! you have {attempts} attempts:\n")
lines = ["_" for i in range(len(word))]
lines3 = "".join(lines)
print(lines3)
guessed = ""
hits = 0
wrong = ""

while attempts > 0:
    if hits == len(word):
        print(word,  "\nYOU WIN!!!")
        break
    letter = input("Fill in a letter: ")
    print('\n')
    correct_entry = Validator.letters(letter)
    good_letter = correct_entry.upper()
    
    if good_letter in word and good_letter not in guessed:
        guessed += good_letter + " "
        
        for i in range(len(word)):  
            if good_letter == word[i]:
                hits += 1     
                lines[i] = good_letter
    else:
        wrong += good_letter + " " 
        attempts -= 1
    lines3 = "".join(lines)
    print(f"Attempts: {attempts}\n{lines3}\n Guessed: {guessed}\n Wrong: {wrong}")
        
if attempts == 0:
        print("You lost... The word was", word)