# HANGMAN

# !!! FINISHED !!!

hangman_pics = [''' 






========= ''', '''

      |
      |
      |
      |
      |
========= ''', '''
  +---+
  |   |
      |
      |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# this will only contain '_' for every letter
transparent_word__ = []

# to move across hangman_pics list
kolkaty_pic = -1
# to move across guessing_word list
kolkaty_letter = 0

# this will contain letter which has already been added to the transparent_word list and it's already been guessed
already_guessed_letters_in_word = []
# this will contain letter which is not at all in our guessing_word list and it's already been guessed
already_guessed_letters_not_in_word = []


def hangman():
    global kolkaty_pic, kolkaty_letter, transparent_word__, already_guessed_letters_in_word, already_guessed_letters_not_in_word
    # ask player to type a guessing word and then right after convert it into list, each letter is an element
    guessing_word = list(input('Type a word which is going to be for guessing: '))

    # if one of those characters player just input contain an integer(number) then call an exception
    for each_char in guessing_word:
        try:
            integer = int(each_char)
            if type(integer) == int:
                print('')
                print('!!! Your word must not contain any numbers, try again !!!')
                hangman()
        except ValueError:
            pass

    # if it contains multiple words with containing space, then don't add '_' for space but only add ' ' for space
    # otherwise just add for every letter '_'
    for index, letter in enumerate(guessing_word):
        if letter == ' ':
            transparent_word__.insert(index, ' ')
        else:
            transparent_word__.insert(index, '_')


    # this is the number of characters of a guessing word player input
    number_of_charac = len(guessing_word)
    # but if that word contains spaces(' ') then the number of characters wil reduce by number of spaces
    if ' ' in guessing_word:
        number_of_charac -= guessing_word.count(' ')


    def guess_letter_hangman():
        global kolkaty_pic, kolkaty_letter, hangman_pics, transparent_word__, already_guessed_letters_in_word, already_guessed_letters_not_in_word

        # if the hangman pics have already been called then call it
        if kolkaty_pic >= 0:
            print(hangman_pics[kolkaty_pic])
        else:
            pass

        print('')
        # .join from that list to make a word readable
        print('  '.join(transparent_word__))

        # run this program till kolkaty_letter is less than number of characters in that guessing word
        # and run this program till kolkaty_pic is less than number of hangman pictures in hangman_pic list minus 1 'cause the indexing starts at 0 not 1 like len
        while kolkaty_letter < number_of_charac and kolkaty_pic < len(hangman_pics) - 1:
            print('')
            # ask for a letter
            guess_letter = input('Guess a letter: ')


            # if that letter has already been guesses remind him
            # CHECK FOR ALL EXCEPTIONS !!!
            if guess_letter in already_guessed_letters_in_word:
                print('')
                print('!!! You have already tried this letter, try another one !!!')
                kolkaty_letter -= guessing_word.count(guess_letter)

            elif guess_letter in already_guessed_letters_not_in_word:
                print('')
                print('!!! You have already tried this letter, try another one !!!')
                kolkaty_pic -= 1

            elif len(guess_letter) != 1:
                print('')
                print('!!! You must guess 1 letter, but not more or less than 1, try again !!!')
                guess_letter_hangman()

            # Check if that guess_letter input will contain a number, if it does then call an exception
            try:
                type_int = int(guess_letter)
                if type(type_int) == int:
                    print('')
                    print('!!! Your guess letter must not be any number, try again !!!')
                    guess_letter_hangman()
            except ValueError:
                pass


            # if that letter appears more than one in that guessing word, then add every letter not just one
            if guessing_word.count(guess_letter) > 1:

                for index, letter in enumerate(guessing_word):
                    if letter == guess_letter:
                        # remove the position where that letter is going to put
                        transparent_word__.pop(index)
                        # and right after make that position where that letter is going to put
                        # 'cause we don't wont to add a letter to the same place where '_' already is, we first need to remove it, seen above
                        transparent_word__.insert(index, letter)

                # add to the kolkaty_letter the number how many times the letter occurs in that guessing word
                kolkaty_letter += guessing_word.count(guess_letter)
                # and right after add that letter to the list where it's already been guessed and added to the transparent_word list
                already_guessed_letters_in_word.append(guess_letter)

                # if the hangman pics have already been called then call it
                if kolkaty_pic >= 0:
                    print(hangman_pics[kolkaty_pic])
                else:
                    pass

                print('')
                print('  '.join(transparent_word__))

            # if that letter appears just one in that guessing word list
            elif guess_letter in guessing_word:
                # add to the kolkaty_letter the number how many times the letter occurs in that guessing word, could have just add 1, but it don't matter
                kolkaty_letter += guessing_word.count(guess_letter)

                # and right after add that letter to the list where it's already been guessed and added to the transparent_word list
                already_guessed_letters_in_word.append(guess_letter)
                # and in that position where that letter is, add that letter where '_' is, just add it to the position where it supposed to be
                transparent_word__[guessing_word.index(guess_letter)] = guess_letter

                # if the hangman pics have already been called then call it
                if kolkaty_pic >= 0:
                    print(hangman_pics[kolkaty_pic])
                else:
                    pass

                print('')
                print('  '.join(transparent_word__))

            # if that letter is not in that guessing word at all
            elif guess_letter not in guessing_word:
                # add one to the kolkaty_pic 'cause we want to move in that hangman_pics list
                kolkaty_pic += 1

                # and right after add that letter to the list where it's already been guessed and is not in transparent_word list
                already_guessed_letters_not_in_word.append(guess_letter)

                # call hangman_pics list
                print(hangman_pics[kolkaty_pic])

                print('')
                print('  '.join(transparent_word__))


            # if all characters have been fulled, then the player has won
            if kolkaty_letter == number_of_charac:
                print('')
                print('!!! GOOD JOB, You have won it was:', ''.join(guessing_word))
                exit()

            # but if the hangman_pic have just printed his last element(full hangman picture), then the player has lost
            if kolkaty_pic == len(hangman_pics) - 1:
                print('')
                print('!!! YOU HAVE LOST, the right answer was:', ''.join(guessing_word))
                exit()

    guess_letter_hangman()


hangman()
