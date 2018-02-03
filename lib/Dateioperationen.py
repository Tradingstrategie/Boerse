# Klasse Dateioperationen zum Lesen/Schreiben der Daten:


import os.path
import glob
import csv
import json
import pickle


class Dateioperationen(object):

    def __init__(self, data_directory):
        self.data_directory = data_directory


    def check_data_directory(self):
        if not os.path.exists(self.data_directory):
            #print('Fehler! Verzeichnis existiert nicht.')
            return False
        elif os.path.isfile(self.data_directory):
            #print('Fehler! Pfadangabe verweist auf Datei, kein Ordner.')
            return False
        elif os.path.isdir(self.data_directory):
            #print('OK!')
            return True
        else:
            #print('Unbekannter Fehler!')
            return False


    # Daten mit verschiedenen Formanten schreiben

    def write_wertpapier_txt(self, wertpapier):
        self.wertpapier = wertpapier
        textfile = open(os.path.join(self.data_directory, str(self.wertpapier.kürzel) + '.txt'), 'w')

            # noch offen
            #            pickle.dump(self.wertpapier, textfile)
            # noch offen

        textfile.close()


    def write_wertpapier_csv(self, wertpapier):
        self.wertpapier = wertpapier

        csvfile = open(os.path.join(self.data_directory, str(self.wertpapier.kürzel) + '.csv'), 'w')
        csvdata = self.wertpapier

# ===== Zeile noch falch ====================
        csv.dump(csvdata, csvfile)
        csvfile.close()


    def write_wertpapier_json(self, wertpapier):
        self.wertpapier = wertpapier
        jsonfile = open(os.path.join(self.data_directory, str(self.wertpapier.kürzel) + '.txt'), 'w')
        jsondata = {
            'Kuerzel': self.wertpapier.kürzel,
            'WPName': self.wertpapier.wertpapiername
        }
        json.dump(jsondata, jsonfile)
        jsonfile.close()


    def write_wertpapier_pickle(self, wertpapier):
        self.wertpapier = wertpapier
        picklefile = open(os.path.join(self.data_directory, str(self.wertpapier.kürzel) + '.dat'), 'bw')
        pickledata = self.wertpapier
        pickle.dump(pickledata, picklefile)
        picklefile.close()


    # Daten mit verschiedenen Formanten lesen


    def read_wertpapier_txt(self, kürzel):
        self.kürzel = kürzel
        wertpapier = {}

        #textfile = open(os.path.join(self.data_directory, str(self.kürzel) + '.txt'), 'r')
        wertpapier = open(os.path.join(self.data_directory, str(self.kürzel) + '.txt')).readlines()

        #wertpapier = readlines(textfile)

        #textfile.close()
        return wertpapier


    def read_wertpapier_csv(self, kürzel):
        self.kürzel = kürzel
        csvfile = os.path.join(self.data_directory, str(self.kürzel) + '.csv')
        with open(csvfile, 'r') as csvfile:
            #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)


    def read_wertpapier_json(self, kürzel):
        self.kürzel = kürzel
        #wertpapier = {}
        jsonfile = open(os.path.join(self.data_directory, str(self.kürzel) + '.txt'), 'r')
        wertpapier = json.load(jsonfile)
        jsonfile.close()
        return wertpapier


    def read_wertpapier_pickle(self, kürzel):
        self.kürzel = kürzel
        #wertpapier = ''
        picklefile = open(os.path.join(self.data_directory, str(self.kürzel) + '.dat'), 'rb')
        wertpapier = pickle.load(picklefile)
        picklefile.close()
        return wertpapier



    # alle Wertpapiere aus Datenbank einlesen


    def read_wertpapiere(self):
        wertpapiere_list = []
        file_list = glob.glob(os.path.join(self.data_directory, '*.dat'))
        for i in range(len(file_list)):
            picklefile = open(file_list[i], "rb")
            wertpapiere_list.append(pickle.load(picklefile))
            picklefile.close()
        return wertpapiere_list



    # Datei löschen

    def remove_wertpapier(self, kürzel):
        self.kürzel = kürzel
        pathname = os.path.join(self.data_directory, str(self.kürzel) + '.dat')
        os.remove(pathname)

