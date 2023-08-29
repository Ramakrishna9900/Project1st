class BaseCalculator:

    def add(self):
        print("from base class: ")
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b
