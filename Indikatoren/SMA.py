# Indikator SMA


def sma(data, n=12):

    i = 0
    smaL = []

    for idata in data:
        sma = 0
        m = i - n + 1
        if m < 0:
            m = 0
        for j in range(i-m+1):    # => range(n)
            sma = sma + data[i-j]
        sma = sma / (i-m+1)    # => /n
        smaL.append(sma)
        i += 1

    return smaL
