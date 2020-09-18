import random
r = random.randint(1,100)
count = 0
while True:
    count = count + 1
    num = input("Please enter a number to guess: ")
    num = int(num)
    if num == r:
        print('You have guessed the correct number.')
        print('This is your', count, 'time/s')
        break
    elif num > r:
        print('too big!')
        print('Please try again!')
    elif num < r:
        print('too small!')
        print('Please try again!')
    print('This is your', count, 'time/s')
