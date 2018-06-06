import lib.DataBase_U as Boerse # Unsere Datenbank


db = Boerse.DataBase('testdaten.txt')

print('Test neue Datenbank:')
print('Name: ', db.name)
print('Datum: ', db.date)
print('Open: ', db.open)
print('High: ', db.high)
print('Low: ', db.low)
print('Close: ', db.close)
print('Test Ende.')
