import random

select_range_num = input('Choose a max range number: ')

if select_range_num.isdigit():
    select_range_num = int(select_range_num)
    if select_range_num <= 0:
        print('Please choose a number larger than 0 next time')
        quit()
else:
    print('Please choose a valid number next time')
    quit()

random_num = random.randint(0, select_range_num)
guess_count=0
while True:
    guess_count += 1
    guess_num = input('Make a guess: ')
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print('Please select a valid number next time')
        continue

    if guess_num == random_num:
        print('You got it!' )
        break
    elif guess_num > random_num:
        print("You were above the random number!")
    else:
        print('You were below the random number!')
print('\n You got it in' , guess_count, 'guesses')

