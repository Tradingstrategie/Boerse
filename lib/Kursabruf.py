# Klasse Kursabruf:


from yahoo_finance import Share


class Kursabruf(object):

    def __init__(self, wertpapier):
        self.wertpapier = wertpapier



# Kursabruf von yahoo funktioniert nicht mehr

    def yahoo_aktuell(self):
        #symbol = '^NDX'
        # symbol = 'FB'
        wp = Share(self.wertpapier.ric)
        open = wp.get_open()
        high = wp.get_days_high()
        low = wp.get_days_low()
        close = wp.get_price()
        time = wp.get_trade_datetime()
        # MEZ:  +1 Stunde
        #  MESZ: +2 Stunden
        #  Close KO:  Uhrzeit: 2017-04-04 20:00:00 UTC+0000   => 22 Uhr
        #  Close NDX: Uhrzeit: 2017-04-04 21:15:00 UTC+0000   => 23:15 Uhr
        print('Symbol:', self.wertpapier.ric, 'Kursdaten:', open, high, low, close )
        print('Uhrzeit:', time)


    def yahoo_historisch(self):
        pass

