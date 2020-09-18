import random
start = input('please enter start of a random number range: ')
end = input('please enter end of a random number range: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
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
