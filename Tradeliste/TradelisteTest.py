# Testdatei Tradeliste

import lib.DataBase_U as Boerse
from Tradeliste import *
from TradelisteMulti import *

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


test_function = tradeliste(name, datum, open, high, low, close, signalL)
#test_function = tradelisteMulti(name, datum, open, high, low, close, signalLMulti)

for x in test_function:
    print(x)
