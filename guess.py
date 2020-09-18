import random
r = random.randint(1,100)
while True:
    num = input("Please enter a number to guess: ")
    num = int(num)
    if num == r:
        print('You have guessed the correct number.')
        break
    elif num > r:
        print('too big!')
        print('Please try again!')
    elif num < r:
        print('too small!')
        print('Please try again!')
