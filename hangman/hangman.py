import random
words=["apple","vanu","ball","idiot","python","mummy"]
word=random.choice(words)
guessed_letter=[]
incorrect_guesses=0
max_incorrect_guesses=6
print("welcome to hangman!")
while incorrect_guesses < max_incorrect_guesses:
    display_word=""
    for letter in word:
        if letter in guessed_letter:
            display_word+=letter+" "
        else:
            display_word+="_ "
    print("word:",display_word)
    if "_"not in display_word:
        print("congrats! you guessed it ",word)
        break
    guess=input("enter the letter:")
    if len(guess)!=1 or not guess.isalpha():
        print("invalid input enter proper letter")
        continue
    if guess in guessed_letter:
        print("you already guessed it ")
        continue
    guessed_letter.append(guess)
    if guess not in word:
        incorrect_guesses+=1
        print("wrong guess")
        print(f"you have {max_incorrect_guesses-incorrect_guesses} guesses left")
else:
     print("game over")
     print("the word was:",word)
                
                        