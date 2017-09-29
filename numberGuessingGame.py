#Diego Aspinwall
#9-29-17
#numberGuessingGame.py

from random import randint

num = randint(1,100)
run = 0

while True:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess == num:
        run+=1
        break
    if guess > num:
        run+=1
        print('too high')
    if guess < num:
        run+=1
        print('too low')
print('You got it in', run, 'tries!')
