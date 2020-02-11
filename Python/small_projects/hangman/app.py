

guess_word = input("Choose word to guess: ")
chars_guessed = ""
lives = 5
win = False
hidden_word = ["_"]*len(guess_word)

print("Remaining lives: " + str(lives))

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


while lives != 0 and not win:
    current_guess = input("Choose a letter: ")
    if len(current_guess) != 1 or not current_guess.isalpha():
        print("That's not a letter")
    if current_guess in chars_guessed:
        print("You've already guessed that letter!")
        break
    if current_guess not in guess_word:
        chars_guessed += current_guess
        lives -= 1
        print("Remaining lives: " + str(lives))
        print("That letter is not in the word")
        print("".join(hidden_word))
    if current_guess in guess_word:
        print("That letter is in the word!")
        for i in range(guess_word.count(current_guess)):
            hidden_word[findnth(guess_word,current_guess,i)] = current_guess
        chars_guessed += current_guess
        print("".join(hidden_word))
    if "_"  not in hidden_word:
        print ("YOU WIN!")
        win = True



