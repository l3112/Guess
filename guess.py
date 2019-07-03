import random
GuessNum = random.randint(1,40)
print('Hi - What\'s your name?')
name = input()
print('Okay,' + name + 'I\'m thinking of a number between 1 and 40')

for guessTake in range(1,20):
    print('Guess!')
    guess int(input())
    if guess < GuessNum:
        print('Too low')
    elif guess > GuessNum:
        print('Too high')
    else:
        break 
if guess == GuessNum:
    print('Nicely done' + name)
else:
    print('The number was' str(GuessNum))