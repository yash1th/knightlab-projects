import random

def guess_number():
    num = random.randint(-100,100)
    numberOfGuesses = 0
    while True:
        print('enter your guess : ',end='')
        try:
            guess = int(input())
            numberOfGuesses += 1
        except ValueError:
            print('Please enter an integer')
            continue
        if guess<num:
            print('your guess is lesser than the answer')
        elif guess>num:
            print('your guess is greater than the answer')
        else:
            print('Congratulations!!,{} is right'.format(guess))
            if numberOfGuesses==1:
                print('You just took {} guess. Must be feeling awesome, eh? ;)'.format(numberOfGuesses))
                return
            print('You took {} guesses'.format(numberOfGuesses))
            return


if __name__ == '__main__':
    guess_number()
