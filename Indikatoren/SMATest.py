import lib.DataBase as Boerse # Unsere Datenbank
from SMA import *


db = Boerse.DataBase('testdaten.txt')

# Testdaten aus testdaten.txt als Liste anstatt db:
testdaten = [6337.874, 6263.7012, 6265.111, 6293.0535, 6316.2778, 6344.5685, 6393.8882, 6383.6522, 6394.6665, 6389.9068, 6466.3204, 6513.2684, 6480.6676, 6472.4825, 6472.6877, 6465.1657, 6433.162, 6435.1521, 6441.4205, 6396.4222, 6511.3424, 6575.8027, 6584.5778, 6653.2905, 6676.6314, 6677.9355, 6662.6583, 6708.4923, 6758.541, 6737.1371, 6810.2834, 6811.3781, 6834.3294, 6906.2781, 6963.463, 6919.3525, 6916.3043, 7022.9712, 6988.3154, 6930.7273, 6949.9868, 6901.5039, 6760.2899, 6495.9189, 6665.9789, 6582.0225, 6306.0999, 6412.6803, 6523.8513, 6553.8643, 6675.0315, 6794.922, 6770.6635, 6779.6949, 6759.2601, 6761.8546, 6896.6012, 6989.0971, 6900.3504, 6854.4174]


data = []
n = 9


data = testdaten

testsma = sma(data, n)
#testsma = sma(data)

for x in testsma:
    print(x)
