# Klasse Wertpapier:


class Wertpapier(object):

    def __init__(self, kürzel):
        self.kürzel = kürzel
        self.symbol = ''
        self.ric = ''
        self.wertpapiername = ''
        self.wertpapiertyp = ''

    def __str__(self):
        return self.kürzel + ' (' + self.wertpapiername + ')'

    def wpanlegen(self):
        self.wertpapiername = input('Gib den Wertpapiernamen ein: ')
#        self.wertpapiertyp = input('Gib den WP-Typ ein: ')
        self.kürzel = input('Gib das Kürzel ein: ')
#        self.symbol = input('Gib das Symbol ein: ')
        self.ric = input('Gib den RIC ein: ')

    def wpanzeigen(self):
        pass

    def wpändern(self):
        pass

