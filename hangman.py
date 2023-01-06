"""
File: hangman.py
Name: Joanne
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    get a random vocabulary, compute the length of vocabulary and print the initial intro,
    get input guess and start distinguish whether the guess is wrong or right
    """
    vocab = random_word()
    length = start(vocab)
    print('The word looks like: ' + length)
    print('You have ' + str(N_TURNS) + ' guesses left.')

    # define variables
    ans_update = length
    n_turns = N_TURNS

    while True:
        word = input('Your guess: ').upper()

        # check input format
        if len(word) != 1 or not word.isalpha():
            print('illegal format.')

        # wrong guess
        elif vocab.find(word) == -1:
            n_turns -= 1
            print('There is no ' + word + '\'s in the word.')
            if n_turns == 0:
                print('You are completely hung:( ')
                print('The word was: ' + vocab)
                break
            else:
                print('The word looks like: ' + ans_update)
                print('You have ' + str(n_turns) + ' guesses left.')

        # correct guess
        elif vocab.find(word) != -1:
            ans = correct(vocab, word, ans_update)
            ans_update = ans
            print('You are correct!')
            if ans_update == vocab:
                print('You win!!')
                print('The word was: ' + vocab)
                break
            else:
                print('The word looks like: ' + ans)
                print('You have ' + str(n_turns) + ' guesses left.')


def start(vocab):
    """
    param vocab: string, random word
    return: string, the first 'the word looks like'
    """
    length = ''
    for i in range(len(vocab)):
        length += '-'
    return length


def correct(vocab, word, ans_update):
    """
    param vocab: string, random word
    param word: string, input guess
    param ans_update: string, previous 'the word looks like'
    return: string: string, newest 'the word looks like'
    """
    ans = ''
    for i in range(len(vocab)):
        ch = vocab[i]
        if ch == word:
            ans += word
        elif ans_update[i] != '-':
            ans += ans_update[i]
        else:
            ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
