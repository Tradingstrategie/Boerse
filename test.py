#!/usr/bin/python
import sys # System Funktionen
import lib.DataBase as Boerse # Unsere Datenbank

if len(sys.argv) != 2:
  print('test.py <datafile.txt>')
  sys.exit(1)

print("Import DataBase from {}...".format(sys.argv[1]))
db = Boerse.DataBase(sys.argv[1])
print("Database \"{}\" imported.".format(db.name))
for entry in db.entries:
  print("Datum: {} Open: {:.2f} Close: {:.2f}".format(entry.date, entry.open, entry.close))
