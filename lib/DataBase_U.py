import os

# Basis Pfad zur Datenbank
base_dir = r"C:\Users\Uli\Documents\GitHub\Boerse\Wertpapiere"
#base_dir="C:\\Users\\tkoehler\\Documents\\GitHub\\Boerse\\Wertpapiere"


# Datenbank fuer ein Wertpapier oder Index
class DataBase:

    name = "" # Name der Datenbank/Wertpapier
    #  Eintraege
    date = [] # Datum "dd.mm.yyyy"
    open = [] # Eroeffnungskurs
    high = [] # Hoechstkurs
    low = [] # Tiefstkurs
    close = [] # Schlusskurs

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
                self.date.append(values[0]) # an Datenbank anhaengen
                self.open.append(float(values[1]))
                self.high.append(float(values[2]))
                self.low.append(float(values[3]))
                self.close.append(float(values[4]))

        self.name = os.path.splitext(os.path.basename(filename))[0]
