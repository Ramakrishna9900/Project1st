from main.calc.basecalculation import BaseCalculator
from main.calc.anotherbasecalculation import AnotherBaseCalculator

# MRO -  Method Resolution Order
class ScientificCalculator(AnotherBaseCalculator, BaseCalculator):
    def __init__(self):
        self.a = int(input('enter first number : '))
        self.b = int(input('enter second number : '))

    def add(self):
        print("from scientific class: ")
        return self.a * self.b


    def square(self):
        return self.a * self.a

    def squareroot(self):
        return self.a / 2


calc1 = ScientificCalculator()
print("the square of number is : " , calc1.square())
print(ScientificCalculator.__mro__)


# (<class '__main__.ScientificCalculator'>,
# <class 'main.calc.anotherbasecalculation.AnotherBaseCalculator'>,
# <class 'main.calc.basecalculation.BaseCalculator'>,
# <class 'object'>)