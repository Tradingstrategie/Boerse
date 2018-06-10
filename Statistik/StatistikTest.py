# Testdatei Statistik

import lib.DataBase_U as Boerse
from Tradeliste.Tradeliste import *
from Tradeliste.TradelisteMulti import *
from Statistik import *

db = Boerse.DataBase('testdaten.txt')
#db = Boerse.DataBase('NDX.txt')
name = db.name
datum = db.date
open = db.open
high = db.high
low = db.low
close = db.close


# ========== Modulbeispiel: =======================
from Module.TT_RSL_EMA import *

n = 12
thresNc = 104
thresNp = 97

n2 = 9
thresNc2 = 102
thresNp2 = 98

signalL = tt_rsl_ema(close, n, thresNc, thresNp)
signalL2 = tt_rsl_ema(close, n2, thresNc2, thresNp2)
signalLMulti = [signalL, signalL2]
# ========== Ende Modulbeispiel. ==================


#tradeL = tradeliste(name, datum, open, high, low, close, signalL)
tradeL = tradelisteMulti(name, datum, open, high, low, close, signalLMulti)


# Testausgaben:
print('Test Tradeliste:')
for x in tradeL:
    print(x)
print('Test Statistik:')
print()


statistik(name, tradeL, beginn='01.01.1990', ende='31.12.2019')
#statistik(name, tradeL, beginn='01.01.2010', ende='31.12.2019')




#===================================================================================

#anzahlJahr = [12, 15.0 , 30, 5]
#print(anzahlJahr[0])
#print('Jahr1: ' + str("{:6d}".format(int(anzahlJahr[1]))))
#print('Jahr2: ' + str("{:5d}".format(int(anzahlJahr[2]))))
#print('Jahr2a: ' + str("{:5d}".format(anzahlJahr[1])))
#print('Jahr3:' + str("{:6.0f}".format(anzahlJahr[2])))
