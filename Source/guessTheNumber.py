import random

secretNumber = random.randint(1, 20)
print('1-20,guess one')
print('youb have 6times to guess')

for i in range(1, 7):
    print('take a guess')
    guessNumber = input('input your number')
    if int(guessNumber) < secretNumber:
        print('your guess is too low')
        print('you have guessed ' + str(i) + ' times')
    elif int(guessNumber) > secretNumber:
        print('your guess is too high')
        print('you have guessed ' + str(i) + ' times')
    elif int(guessNumber) == secretNumber:
        print('you got it')
        print('you have guessed ' + str(i) + ' times')
        break
    if i == 6:
        print('you waste your times')
        print('the correct number is ' + str(secretNumber))
