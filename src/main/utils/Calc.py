class Calc:

    TABLE_NAME = 'Test Table'

    def __init__(self, connection):
        self.conn = connection

    def updateRecord(self, query):
        print("in update record method with db conn as :", self.conn)
        print("in update query :", query)
        pass

    def insertRecord(self, query):
        print("in insert record method with db conn as :", self.conn)
        print("in insert query :", query)
        pass

    @staticmethod
    def createRecord(query):
        print("in create record method with db conn as :", query)

    def deleteRecord(self, query):
        print("in delete record method with db conn as :", self.conn)
        pass

# def to_upper_case(inputString: str):
#     return inputString.upper()

# we have a function that takes list of names and returns upper case of its name


