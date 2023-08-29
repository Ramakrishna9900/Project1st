from main.calc.subtractmethod import Subtraction

class Execution(Subtraction):     # child

    def __init__(self):

        self.printing()
        # enter first number
        num1 = int(input('enter first number: '))
        # Enter second number
        num2 = int(input('enter second number: '))

        # ask for operation (+ or -)
        operator = input('enter type of operation (+ or -): ')

        if operator == '+':
            print('Sum is: ', self.summing(num1, num2))
        elif operator == '-':
            print('Subtraction is: ', self.sub(num1, num2))
        else:
            print('enter correct operator')


calc = execution()


# addition -> subtraction -> Execution
# summing   : sub    ->

# what will happen if the summing method is there in both Addition and subtraction class??
# class Execution(Addition, Subtraction):  Multiple inheritanc