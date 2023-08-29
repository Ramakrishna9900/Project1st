from main.utils.Calc import Calc

connection = 'our_oracle_conn_string'

# calc = Calc(connection)

Calc.createRecord('create query here')

print(Calc.TABLE_NAME)

