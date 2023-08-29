print("Welcome to my computer Quiz Game!")
play = input("Do you want to play Quiz game? ")

if play.lower() == "yes" or play.lower() == "y":
    print("OK, let's play!")
else:
    print("Good bye!")
    quit()

score = 0

answer = int(input('4*4 = ? '))
if answer == 16:
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = int(input('5*7 = ? '))
if answer == 35:
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = int(input('8*7 = ? '))
if answer == 56:
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = int(input('9*8 = ? '))
if answer == 72:
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = int(input('8*6 = ? '))
if answer == 48:
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " correct answers!")
print("You got " + str((score / 5) * 100) + " %.")
