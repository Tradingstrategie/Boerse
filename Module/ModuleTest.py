# Testdatei für Module

import lib.DataBase_U as Boerse

# importieren der zu testenden Module:
from Module.TT_RSL_EMA import *

# verwendete Untermodule:
#from Indikatoren.RSL_EMA import *


db = Boerse.DataBase('testdaten.txt')
data = db.close

n = 12
thresNc = 105
thresNp = 97
#thresNp = 10 # bedeutet nur Calls aktiv


test_function = tt_rsl_ema(data, n, thresNc, thresNp)
#test_function = tt_rsl_ema(data)

i=0
for x in test_function:
    print(db.date[i], x)
    i +=1
