class UnderstandingSelf:

    def __init__(self):
        n1 = int(input('enter first number: '))
        self.num1 = n1
        self.num2 = int(input('enter second number: '))
        operator = input('enter type of operation (+ or -): ')

        if operator == '+':
            print(self.summing())
        elif operator == '-':
            print('Subtraction is: ', self.sub())
        else:
            print('enter correct operator')


    def summing(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

obj1 = UnderstandingSelf()
# obj2 = UnderstandingSelf()
# obj3 = UnderstandingSelf()