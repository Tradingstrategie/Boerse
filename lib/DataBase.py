import os

# Basis Pfad zur Datenbank
base_dir="C:\\Users\\tkoehler\\Documents\\GitHub\\Boerse\\Wertpapiere"

# Datenbank Eintrag
class Entry:
  date = "" # Datum "dd.mm.yyyy"
  open = 0 # Eroeffnungskurs
  high = 0 # Hoechstkurs
  low = 0 # Tiefstkurs
  close = 0 # Schlusskurs

  # Constructur
  def __init__(self, date, open, high, low, close):
    self.date = date
    self.open = float(open)
    self.high = float(high)
    self.low = float(low)
    self.close = float(close)


# Datenbank fuer ein Wertpapier oder Index
class DataBase:
  name = "" # Name der Datenbank/Wertpapier
  entries = [] # Eintraege

  # Constructor von Datei
  def __init__(self, filename):
    # Test ob Dateiname relativ oder absolut ist
    if not os.path.isfile(filename):
      filename = os.path.join(base_dir, filename)

    # Datenbank laden
    with open(filename) as f:
      for line in f.readlines(): # alle Zeile einlesen
        line = line.replace(',', '.') # 123,45 => 123.45
        values = line.split() # in Liste splitten
        entry = Entry(values[0], values[1], values[2], values[3], values[4])
        self.entries.append(entry) # an Datenbank anhaengen

    self.name = os.path.splitext(os.path.basename(filename))[0]
